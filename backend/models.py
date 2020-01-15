from flask_sqlalchemy import SQLAlchemy
import click
from flask.cli import with_appcontext
import os
import gzip
import pandas as pd
from sqlalchemy import create_engine
import zipfile


db = SQLAlchemy()
package_dir = os.path.dirname(os.path.realpath(__file__+'\..'))

def initialize_db(app):
    app.app_context().push()
    app.cli.add_command(init_db)
    db.init_app(app)

def get_engine():
    return create_engine("sqlite:///movies.db")

class Title(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tconst = db.Column(db.String(80), unique=True, nullable=False)
    titleType = db.Column(db.String(80), unique=False, nullable=False)
    primaryTitle = db.Column(db.String(80), unique=False, nullable=False)
    originalTitle = db.Column(db.String(80), unique=False, nullable=False)
    isAdult = db.Column(db.Boolean, default=False)
    startYear = db.Column(db.Integer, unique=False, nullable=False)
    endYear = db.Column(db.Integer, unique=False, nullable=False)
    runtimeMinutes = db.Column(db.Integer, unique=False, nullable=False)
    genres = db.Column(db.String(80), unique=False, nullable=False)
    averageRating = db.Column(db.Float, unique=False, nullable=False)
    numVotes = db.Column(db.Integer, unique=False, nullable=False)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'tconst': self.tconst,
            'titleType': self.titleType,
            'primaryTitle': self.primaryTitle,
            'originalTitle': self.originalTitle,
            'isAdult': self.isAdult,
            'startYear': self.startYear,
            'endYear': self.endYear,
            'runtimeMinutes': self.runtimeMinutes,
            'genres': self.genres,
            'averageRating': self.averageRating,
            'numVotes': self.numVotes   
        }

class Name(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    primaryName = db.Column(db.String(80), unique=False, nullable=False)
    birthYear = db.Column(db.Integer, unique=False, nullable=False)
    deathYear = db.Column(db.Integer, unique=False, nullable=False)
    knownForTitles = db.Column(db.String(80), unique=False, nullable=False)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'primaryName': self.primaryName,
            'birthYear': self.birthYear,
            'deathYear': self.deathYear,
            'knownForTitles': self.knownForTitles        
        }

@click.command('init-db')
@with_appcontext
def init_db():
    db.create_all()
    insert_data_title()
    insert_data_name()

def insert_data_title():
    print('Inserting title data into table')
    file_to_search =  os.path.join(package_dir,'dataset\\title.basics.tsv.gz')
    with gzip.open(file_to_search,'r') as file:
        print('Reading tsv file')
        df = pd.read_csv(file, sep="\t")
    print('Changing endYear n to 0')
    df = df.replace({'endYear': "\\N"}, 0)
    print('Removing movies out of pattern at isAdult column')
    df = df.loc[df['isAdult'].isin([0,1])]
    print('Removing null values')
    df_ratings = read_ratings_data()
    df = pd.merge(df, df_ratings, left_on="tconst", right_on='tconst')
    df = df[df['runtimeMinutes'].str.isnumeric()]
    df = df.dropna()
    print(df.head())
    df.to_sql('title', get_engine(), if_exists='append', index=False)
    return 'Table Loaded'

def read_ratings_data():
    file_to_search_ratings =  os.path.join(package_dir,'dataset\\title.ratings.tsv.gz')
    with gzip.open(file_to_search_ratings,'r') as file_ratings:
        df_ratings = pd.read_csv(file_ratings, sep="\t")
        print('Removing ratings lower than 6')
        df_ratings = df_ratings[df_ratings['averageRating'] >= 6]
    return df_ratings

def insert_data_name():
    print('Inserting title data into table')
    file_to_search =  os.path.join(package_dir,'dataset\\name.basics.tsv.gz')
    with gzip.open(file_to_search,'r') as file:
        print('Reading tsv file')
        df = pd.read_csv(file, sep="\t")
        print('Removing null values')
    df = df.dropna()
    df = df.drop(columns=['nconst','primaryProfession'])
    print(df.head())
    df = df.loc[~df['knownForTitles'].isin(["\\N"])]
    df.to_sql('name', get_engine(), if_exists='append', index=False)
    return 'Table loaded'