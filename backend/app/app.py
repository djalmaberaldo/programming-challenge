import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
import json
import models
import implementations
from flask_expects_json import expects_json

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
    page = request.args.get('page')       
    results, total = implementations.get_all_movies(search, filterBy, page);
    return process_response(results, total)

@app.route('/movies/by-year', methods=['GET'])
@cross_origin()
def get_top_movies_by_yeaar():
    year = request.args.get('year')
    page = request.args.get('page')       
    results, total = implementations.get_movies_by_year(year, page);
    return process_response(results, total)

@app.route('/movies/names', methods=['GET','POST'])
def get_names():
    tconst = request.args.get('tconst')
    results, total = implementations.get_all_names(tconst);
    return process_response(results, total)

@app.route('/load-titles', methods=['GET'])
def load_data_title():
    results = implementations.insert_data_title();
    return results

@app.route('/load-names', methods=['GET'])
def load_data_names():
    results = implementations.insert_data_name();
    return results

def process_response(results=[], total='Unknown'):
    return jsonify({
        'data': [result.serialize for result in results],
        'totalItems': total
    });

if __name__ == "__main__":
    app.run(debug=True)
