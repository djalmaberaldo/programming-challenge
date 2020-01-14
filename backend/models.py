from flask_sqlalchemy import SQLAlchemy
import click
from flask.cli import with_appcontext

db = SQLAlchemy()

def initialize_db(app):
  app.app_context().push()
  db.init_app(app)
  db.create_all()

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
    df.to_sql('title', engine, if_exists='append', index=False)
    return 'Table Loaded'