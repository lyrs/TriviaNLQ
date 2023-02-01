import os 
import string
from SPARQLWrapper import SPARQLWrapper, JSON
from fairseq.models.transformer import TransformerModel
from tntspa.generator_utils import decode

"""The core methods of our project."""


def load_model(model_path, data_path, is_gpu=False):
    """Loads model from a checkpoint.

    model_path: path to a chekcpoint i.e. models/Monument/checkpoint_best.pt
    data_path: path to a fairseq bin i.e. data/Monument/fairseq-data-bin
    is_gpu: boolean, if cuda runs on gpu
    """
    model_dir, model_file = os.path.split(model_path)
    model = TransformerModel.from_pretrained(
        model_dir, checkpoint_file=model_file,
        data_name_or_path=data_path, is_gpu=is_gpu).cuda()
    return model


def gen_sparql(question, model):
    """Generates SPARQL query from a natural language question.

    question: string, question in natural language
    model: transformer text-to-sparql model
    """
    question = ''.join(c for c in question.lower() if c in string.ascii_lowercase + "' ")
    enc_query = model.translate(question)
    query = decode(enc_query)
    return query, enc_query


def ask_dbpedia(query):
    """Query DBpedia"""
    result = None
    error = None
    try:
        endpoint = SPARQLWrapper("http://dbpedia.org/sparql")
        endpoint.setReturnFormat(JSON)
        endpoint.setQuery(query)
        result = endpoint.query().convert()
    except Exception as e:
        print('Failed: ' + str(e))
        error = str(e)
    return result, error
