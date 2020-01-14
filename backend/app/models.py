from flask_sqlalchemy import SQLAlchemy

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
