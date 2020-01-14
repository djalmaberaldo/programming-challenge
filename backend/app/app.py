import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
import json
import models
import implementations

app = Flask(__name__, instance_relative_config=True)
app.config["SQLALCHEMY_DATABASE_URI"] ="sqlite:///movies.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

models.initialize_db(app)

@app.route('/')
def home():
    return '';

@app.route('/titles', methods=['GET'])
@cross_origin()
def get_titles():
    search = request.args.get('search')
    filterBy = request.args.get('filterBy')
    results = implementations.get_all_titles(search, filterBy);
    return process_response(results)

@app.route('/titles-by-year', methods=['GET'])
@cross_origin()
def get_top_titles_by_yeaar():
    year = request.args.get('year')
    results = implementations.get_titles_by_year(year);
    return process_response(results)

@app.route('/movies', methods=['GET'])
@cross_origin()
def get_movies():
    search = request.args.get('search')
    filterBy = request.args.get('filterBy')    
    results = implementations.get_all_movies(search, filterBy);
    return process_response(results)

@app.route('/movies-by-year', methods=['GET'])
@cross_origin()
def get_top_movies_by_yeaar():
    year = request.args.get('year')
    results = implementations.get_movies_by_year(year);
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
