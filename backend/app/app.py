import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
import json
import models
from db import initialize_db
import implementations

app = Flask(__name__, instance_relative_config=True)
app.config["SQLALCHEMY_DATABASE_URI"] ="sqlite:///movies.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

initialize_db(app)

@app.route('/')
def home():
    return '';

@app.route('/titles', methods=['GET'])
@cross_origin()
def get_titles():
    results = implementations.get_all_titles();
    return process_response(results)


@app.route('/names', methods=['GET'])
def get_names():
    results = implementations.get_all_names();
    return process_response(results)

@app.route('/load-titles', methods=['GET'])
def load_data_title():
    results = implementations.insert_data_title();
    return results

@app.route('/load-names', methods=['GET'])
def load_data_names():
    results = implementations.insert_data_name();
    return results

def process_response(results=[]):
    return jsonify({
        'data': [result.serialize for result in results]
    });

if __name__ == "__main__":
    app.run(debug=True)
