from flask import Flask, jsonify, request, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
import json
import models
import implementations
from flask_expects_json import expects_json
from app import create_app


route_blueprint = Blueprint('route_blueprint', __name__)


@route_blueprint.route('/')
def home():
    return '';

@route_blueprint.route('/movies', methods=['GET'])
@cross_origin()
def get_movies():
    search = request.args.get('search')
    filterBy = request.args.get('filterBy')
    if request.args.get('page') is None:
        return 'Page parameter necessary'
    else:
        page = request.args.get('page')
    results, total = implementations.get_all_movies(search, filterBy, page);
    return process_response(results, total)

@route_blueprint.route('/movies/by-year', methods=['GET'])
@cross_origin()
def get_top_movies_by_yeaar():
    year = request.args.get('year')
    if request.args.get('page') is None:
        return 'Page parameter necessary'
    else:
        page = request.args.get('page')    
    results, total = implementations.get_movies_by_year(year, page);
    return process_response(results, total)


@route_blueprint.route('/movies/names', methods=['GET','POST'])
def get_names():
    tconst = request.args.get('tconst')
    results, total = implementations.get_all_names(tconst);
    return process_response(results, total)

def process_response(results=[], total='Unknown'):
    return jsonify({
        'data': [result.serialize for result in results],
        'totalItems': total
    });
    

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
