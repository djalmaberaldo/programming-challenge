import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__, instance_relative_config=True)
app.config["SQLALCHEMY_DATABASE_URI"] ="sqlite:///title.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

import models
from models import initialize_db
initialize_db(app)

@app.route('/')
def home():
    return '';

@app.route('/genres', methods=['GET'])
def get_genres():
    results = models.get_all_genres();
    return process_response(results)

@app.route('/titles', methods=['GET'])
def get_titles():
    results = models.get_all_titles();
    return process_response(results)


@app.route('/names', methods=['GET'])
def get_names():
    results = models.get_all_names();
    return process_response(results)

def process_response(results=[]):
    return jsonify({
        'data': [result.serialize for result in results]
    });

if __name__ == "__main__":
    app.run(debug=True)