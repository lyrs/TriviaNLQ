# Libraries
import collections
import http.client
import json
import logging
import re
import sys
import urllib.request, urllib.parse, urllib.error
import urllib.request, urllib.error, urllib.parse
from functools import reduce

# Define the endpoint and graph for the DBpedia SPARQL query
ENDPOINT = "http://dbpedia.org/sparql"
GRAPH = "http://dbpedia.org"

def log_statistics( used_resources, special_classes, not_instanced_templates ):
    """
    Log information about the resources used in the query.
    :param used_resources: a dictionary of resources and their usage count.
    :param special_classes: a dictionary of classes and the resources they contain.
    :param not_instanced_templates: a dictionary of templates that were not instanciated.
    """
    # Count the total number of resources used and the total number of filled placeholder positions
    total_number_of_resources = len(used_resources)
    total_number_of_filled_placeholder_positions = sum(used_resources.values())
    # Count the number of examples per instance
    examples_per_instance = collections.Counter()
    for resource in used_resources:
        count = used_resources[resource]
        examples_per_instance.update([count])
    # Log the information
    logging.info('{:6d} used resources in {} placeholder positions'.format(total_number_of_resources, total_number_of_filled_placeholder_positions))
    for usage in examples_per_instance:
        logging.info('{:6d} resources occur \t{:6d} times \t({:6.2f} %) '.format(examples_per_instance[usage], usage, examples_per_instance[usage]*100/total_number_of_resources))
    for cl in special_classes:
        logging.info('{} contains: {}'.format(cl, ', '.join(special_classes[cl])))
    logging.info('{:6d} not instanciated templates:'.format(sum(not_instanced_templates.values())))
    for template in not_instanced_templates:
        logging.info('{}'.format(template))


def save_cache ( file, cache ):
    """
    Save the cache to a file.
    :param file: the file to save the cache to.
    :param cache: the cache to save.
    """
    # Order the cache by usage count
    ordered = collections.OrderedDict(cache.most_common())
    # Write the cache to the file
    with open(file, 'w') as outfile:
        json.dump(ordered, outfile)


def query_dbpedia( query ):
    """
    Execute a SPARQL query against the DBpedia endpoint.
    :param query: the SPARQL query to execute.
    :return: the JSON response from the endpoint.
    """
    # Set the parameters for the query
    param = dict()
    param["default-graph-uri"] = GRAPH
    param["query"] = query
    param["format"] = "JSON"
    param["CXML_redir_for_subjs"] = "121"
    param["CXML_redir_for_hrefs"] = ""
    param["timeout"] = "600" # ten minutes - works with Virtuoso endpoints
    param["debug"] = "on"
    try:
        # Send the query to the endpoint and return the JSON response
        resp = urllib.request.urlopen(ENDPOINT + "?" + urllib.parse.urlencode(param))
        j = resp.read()
        resp.close()
    except (urllib.error.HTTPError, http.client.BadStatusLine):
        logging.debug("*** Query error. Empty result set. ***")
        j = '{ "results": { "bindings": [] } }'
    sys.stdout.flush()
    return json.loads(j)


def strip_brackets(s):
    """
    Strip brackets from a string and return the resulting string.
    :param s: the string to strip brackets from.
    :return: the stripped string.
    """
    # Remove any text within parentheses
    s = re.sub(r'\([^)]*\)', '', s)
    if "," in s:
        s = s[:s.index(",")]
    return s.strip().lower()

# List of replacements to be made on the SPARQL query
REPLACEMENTS = [
    ['dbo:', 'http://dbpedia.org/ontology/', 'dbo_'], # e.g. replace 'dbo:' with 'http://dbpedia.org/ontology/' and 'dbo_' etc 
    ['dbp:', 'http://dbpedia.org/property/', 'dbp_'],
    ['dbc:', 'http://dbpedia.org/resource/Category:', 'dbc_'],
    ['dbr:', 'res:', 'http://dbpedia.org/resource/', 'dbr_'],
    ['rdf:', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#', 'rdf_'],
    ['rdfs:', 'http://www.w3.org/2000/01/rdf-schema#', 'rdfs_'],
    ['dct:', 'dct_'],
    ['geo:', 'geo_'],
    ['georss:', 'georss_'],
    ['rdf:', 'rdf_'],
    ['rdfs:', 'rdfs_'],
    ['foaf:', 'foaf_'],
    ['owl:', 'owl_'],
    ['yago:', 'yago_'],
    ['skos:', 'skos_'],
    [' ( ', '  par_open  '],
    [' ) ', '  par_close  '],
    ['(', ' attr_open '],
    [') ', ')', ' attr_close '],
    ['{', ' brack_open '],
    ['}', ' brack_close '],
    [' . ', ' sep_dot '],
    ['. ', ' sep_dot '],
    ['?', 'var_'],
    ['*', 'wildcard'],
    [' <= ', ' math_leq '],
    [' >= ', ' math_geq '],
    [' < ', ' math_lt '],
    [' > ', ' math_gt ']
]

# Dictionary of predicates and their standardized form
STANDARDS = {
        'dbo_almaMater': ['dbp_almaMater'], # e.g. replace 'dbp_almaMater' with 'dbo_almaMater' etc
        'dbo_award': ['dbp_awards'],
        'dbo_birthPlace': ['dbp_birthPlace', 'dbp_placeOfBirth'],
        'dbo_deathPlace': ['dbp_deathPlace', 'dbp_placeOfDeath'],
        'dbo_child': ['dbp_children'],
        'dbo_college': ['dbp_college'],
        'dbo_hometown': ['dbp_hometown'],
        'dbo_nationality': ['dbo_stateOfOrigin'],
        'dbo_relative': ['dbp_relatives'],
        'dbo_restingPlace': ['dbp_restingPlaces', 'dbp_placeOfBurial', 'dbo_placeOfBurial', 'dbp_restingplace'],
        'dbo_spouse': ['dbp_spouse'],
        'dbo_partner': ['dbp_partner']
}


def encode( sparql ):
    """ Encodes the input SPARQL query by replacing predicates and other keywords with their encoded form.
    """
    encoded_sparql = do_replacements(sparql) # replace predicates and keywords with their encoded form
    shorter_encoded_sparql = shorten_query(encoded_sparql) # shorten the encoded query
    normalized = normalize_predicates(shorter_encoded_sparql) #normalize the predicates to their standardized form
    return normalized


def decode ( encoded_sparql ):
    """ Decodes the encoded SPARQL query by replacing the encoded predicates and keywords with their original form. 
    """
    short_sparql = reverse_replacements(encoded_sparql) # replace encoded predicates and keywords with their original form
    sparql = reverse_shorten_query(short_sparql) # reverse the shortening of the query
    return sparql


def normalize_predicates( sparql ):
    """Normalizes the predicates to their standardized form
    """
    for standard in STANDARDS:
        for alternative in STANDARDS[standard]:
            sparql = sparql.replace(alternative, standard) # replace the alternative predicates with their standardized form

    return sparql


def do_replacements( sparql ):
    """Replaces predicates and other keywords with their encoded form
    """
    for r in REPLACEMENTS:
        encoding = r[-1]
        for original in r[:-1]:
            sparql = sparql.replace(original, encoding) # replace the original predicate/keyword with its encoded form
    return sparql


def reverse_replacements( sparql ):
    """Replaces the encoded predicates and other keywords with their original form
    """
    for r in REPLACEMENTS:
        original = r[0]
        encoding = r[-1]
        sparql = sparql.replace(encoding, original) # replace the encoded predicate/keyword with its original form
        stripped_encoding = str.strip(encoding)
        sparql = sparql.replace(stripped_encoding, original)
    return sparql


def shorten_query( sparql ):
    """Shortens the SPARQL query by removing unnecessary parts
    """
    sparql = re.sub(r'order by desc\s+....?_open\s+([\S]+)\s+....?_close', '_obd_ \\1', sparql, flags=re.IGNORECASE)
    sparql = re.sub(r'order by asc\s+....?_open\s+([\S]+)\s+....?_close', '_oba_ \\1', sparql, flags=re.IGNORECASE)
    sparql = re.sub(r'order by\s+([\S]+)', '_oba_ \\1', sparql, flags=re.IGNORECASE)
    return sparql


def reverse_shorten_query( sparql ):
    """Reverses the shortening of the SPARQL query
    """
    sparql = re.sub(r'_oba_ ([\S]+)', 'order by asc (\\1)', sparql, flags=re.IGNORECASE)
    sparql = re.sub(r'_obd_ ([\S]+)', 'order by desc (\\1)', sparql, flags=re.IGNORECASE)
    return sparql


def read_template_file(file):
    # Initialize an empty list to store the annotations
    annotations = list()
    # Keep track of the line number
    line_number = 1
    with open(file) as f:
        for line in f:
            # Split the line by ';'
            values = line[:-1].split(';')
            # Get the target classes
            target_classes = [values[0] or None, values[1] or None, values[2] or None]
            # Get the question
            question = values[3]
            # Get the query
            query = values[4]
            # Get the generator query
            generator_query = values[5]
            # Get the id, if there is one, otherwise use the line number
            id = values[6] if (len(values) >= 7 and values[6]) else line_number
            line_number += 1
            # Create an Annotation object
            annotation = Annotation(question, query, generator_query, id, target_classes)
            annotations.append(annotation)
    return annotations


class Annotation:
    def __init__(self, question, query, generator_query, id=None, target_classes=None):
        self.question = question
        self.query = query
        self.generator_query = generator_query
        self.id = id
        # Set the target classes to an empty list if they are not provided
        self.target_classes = target_classes if target_classes != None else []
        # Get the variables used in the generator query
        self.variables = extract_variables(generator_query)


def extract_variables(query):
    variables = []
    # Get the part of the query after 'where'
    query_form_pattern = r'^.*?where'
    query_form_match = re.search(query_form_pattern, query, re.IGNORECASE)
    if query_form_match:
        letter_pattern = r'\?(\w)'
        # Extract variables starting with '?'
        variables = re.findall(letter_pattern, query_form_match.group(0))
    return variables


def extract_encoded_entities( encoded_sparql ):
    # Decode the sparql
    sparql = decode(encoded_sparql)
    entities = extract_entities(sparql)
    encoded_entities = list(map(encode, entities))
    return encoded_entities


def extract_entities( sparql ):
    triples = extractTriples(sparql)
    entities = set()
    for triple in triples:
        possible_entities = [triple['subject'], triple['object']]
        # Extract entities that are not variables and contain ':'
        sorted_out = [e for e in possible_entities if not e.startswith('?') and ':' in e]
        entities = entities.union([re.sub(r'^optional{', '', e, flags=re.IGNORECASE) for e in sorted_out])
    return entities


def extract_predicates( sparql ):
    # Get all the triples in the query
    triples = extractTriples(sparql)
    predicates = set()
    # Iterate over each triple and add the predicate to the set
    for triple in triples:
        pred = triple['predicate']
        predicates.add(pred)
    return predicates


def extractTriples (sparqlQuery):
    triples = []
    # Get the part of the query inside the curly braces after 'where'
    whereStatementPattern = r'where\s*?{(.*?)}'
    whereStatementMatch = re.search(whereStatementPattern, sparqlQuery, re.IGNORECASE)
    if whereStatementMatch:
        whereStatement = whereStatementMatch.group(1)
        triples = splitIntoTriples(whereStatement)
    return triples


def splitIntoTriples (whereStatement):
    # Split the where statement into a list of triples and separators
    tripleAndSeparators = re.split('(\.[\s\?\<$])', whereStatement)
    trimmed = [str.strip() for str in tripleAndSeparators]

    def repair (list, element):
        """This function takes in a list and an element, and modifies the list by combining the last element and the current element, 
        if they are not in the list of separators. Otherwise, it appends the current element to the list."""
        if element not in ['.', '.?', '.<']:
            previousElement = list[-1]
            del list[-1]
            if previousElement in ['.', '.?', '.<']:
                cutoff = previousElement[1] if previousElement in ['.?', '.<'] else ''
                list.append(cutoff + element)
            else:
                list.append(previousElement + ' ' + element)
        else:
            list.append(element)

        return list

    tripleStatements = reduce(repair, trimmed, [''])
    triplesWithNones = list(map(splitIntoTripleParts, tripleStatements))
    triples = [triple for triple in triplesWithNones if triple != None]
    return triples


def splitIntoTripleParts (triple):
    statementPattern = r'(\S+)\s+(\S+)\s+(\S+)'
    statementPatternMatch = re.search(statementPattern, triple)

    if statementPatternMatch:
        # If the pattern is matched, return a dictionary of the subject, predicate, and object
        return {
            'subject': statementPatternMatch.group(1),
            'predicate': statementPatternMatch.group(2),
            'object': statementPatternMatch.group(3)
        }
    else:
        # If the pattern is not matched, return None
        return None