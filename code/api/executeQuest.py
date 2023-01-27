## requirements
# ! pip install cffi
# ! pip install numpy
# ! pip install torch
# ! pip install tqdm
# ! pip install fairseq

## libraries
from SPARQLWrapper import SPARQLWrapper, JSON
import generator_utils as utils
import subprocess
import sys  


def predict_sparql(question):
    with open("source.txt", "w") as text_file:
        # Write the input to a file
        text_file.write("%s" % question)

    # Define the command to run the machine learning model
    bashCommand = "fairseq-interactive  --path output/models/checkpoint_best.pt  data/monument_600/fairseq-data-bin --beam 5 --source-lang en --target-lang sparql     --tokenizer moses  --input=source.txt"
    # Run command line process to run the input through the model
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    # Decode the output and split it into lines
    output, error = process.communicate()
    outputs = output.decode("utf-8").split('\n')
    # Extract the SPARQL query from the output
    query = outputs[2].split('	')[2]
    query = utils.decode(query)
    # query = query.replace('<', '').replace('>', '')
    # Send the SPARQL query to DBpedia
    try:
        results = None
        error = None
        sparql = SPARQLWrapper("http://dbpedia.org/sparql")
        sparql.setReturnFormat(JSON)

        sparql.setQuery(query)  # the previous query as a literal string
        results = sparql.query().convert()
    except Exception as e:
        print('Failed Error: '+ str(e))
        error=  str(e)
    # Print the results
    return {"questionEncoding": outputs[0],
            "queryEncoding": outputs[2].split('	')[2],
            "sparql": query,
            "dbpediaResult": results,
            "error": error}