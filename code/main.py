## requirements
# ! pip install cffi
# ! pip install numpy
# ! pip install torch
# ! pip install tqdm
# ! pip install fairseq

## libraries
from SPARQLWrapper import SPARQLWrapper, JSON
import api.generator_utils as utils
import subprocess
import os


while(1):
    # Ask user for input
    question = input('write question:')
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
    # Clear the console
    # os.system('clear')
    # Print the question
    print(question)
    # Print the output from the model
    print(outputs[0 ])
    # Extract the SPARQL query from the output
    query = outputs[2].split('	')[2]
    query = query.replace('<', '').replace('>', '')
    query = utils.decode(query)
    print(query)
    # Send the SPARQL query to DBpedia
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setReturnFormat(JSON)

    sparql.setQuery(query)  # the previous query as a literal string
    results = sparql.query().convert()
    # Print the results
    if results["results"]:
        print(results["results"])
    else:
        print(results)
