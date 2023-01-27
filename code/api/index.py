from flask import Flask, request 
from flask_cors import CORS, cross_origin
import json 

import executeQuest 


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/", methods=['GET', 'POST'])
@cross_origin()
def runQuery():
    data = request.get_json()
    result = executeQuest.predict_sparql(data['searchText'])
    print(result)
    return json.dumps(result)