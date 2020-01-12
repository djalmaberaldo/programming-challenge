from db import db

class Title(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titleIdentifier = db.Column(db.String(80), unique=True, nullable=False)
    titleType = db.Column(db.String(80), unique=False, nullable=False)
    primaryTitle = db.Column(db.String(80), unique=False, nullable=False)
    originalTitle = db.Column(db.String(80), unique=False, nullable=False)
    isAdult = db.Column(db.Boolean, default=False)
    startYear = db.Column(db.Integer, unique=False, nullable=False)
    endYear = db.Column(db.Integer, unique=False, nullable=False)
    runtimeMinutes = db.Column(db.Integer, unique=False, nullable=False)
    genres = db.Column(db.String(80), unique=False, nullable=False)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'titleIdentifier': self.titleIdentifier,
            'titleType': self.titleType,
            'primaryTitle': self.primaryTitle,
            'originalTitle': self.originalTitle,
            'isAdult': self.isAdult,
            'startYear': self.startYear,
            'endYear': self.endYear,
            'runtimeMinutes': self.runtimeMinutes,
            'genres': self.genres            
        }

class TitleRatings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numVotes = db.Column(db.Integer, unique=False, nullable=False)
    averageRating = db.Column(db.Float, unique=False, nullable=False)
    titleId = db.Column(db.Integer, db.ForeignKey('title.id'))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'numVotes': self.numVotes,
            'averageRatings': self.averageRating,
            'titleId': self.titleId
        }

professions = db.Table ('professions',
    db.Column('name_id', db.Integer, db.ForeignKey('name.id'), primary_key=True),
    db.Column('professions_id', db.Integer, db.ForeignKey('profession.id'), primary_key=True)
)

class Name(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tconst = db.Column(db.String(80), unique=False, nullable=False)
    primaryName = db.Column(db.String(80), unique=False, nullable=False)
    birthYear = db.Column(db.Integer, unique=False, nullable=False)
    deathYear = db.Column(db.Integer, unique=False, nullable=False)
    professions = db.relationship('Profession', secondary=professions, backref=db.backref('person', lazy=True), lazy="subquery")

    @property
    def serialize(self):
        return {
            'id': self.id,
            'tconst': self.tconst,
            'primaryName': self.primaryName,
            'birthYear': self.birthYear,
            'deathYear': self.deathYear,
            'professions': self.professions          
        }

class Profession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }
