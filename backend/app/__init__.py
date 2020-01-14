from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config["SQLALCHEMY_DATABASE_URI"] ="sqlite:///../movies.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from flask_cors import CORS
    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'

    from models import initialize_db
    initialize_db(app)

    from routes import route_blueprint
    app.register_blueprint(route_blueprint)

    return app