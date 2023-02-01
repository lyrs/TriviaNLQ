#!/usr/bin/env python3

import trivianlq

MODELPATH = "models/Monument/checkpoint_best.pt"
DATAPATH = "data/Monument/fairseq-data-bin"

print("-- This is our demo!")

model = trivianlq.load_model(MODELPATH, DATAPATH, is_gpu=True)

inp = input("-- Pose your question:\n")

query, _ = trivianlq.gen_sparql(inp, model)

print(query)

result, error = trivianlq.ask_dbpedia(query)

if error:
    print("-- Something went wrong...")
if result:
    print("-- Here's the result:")
    print([ok['a']['value'] for ok in result['results']['bindings']])
else:
    print("-- Sorry, I couldn't get the answer! :(")
