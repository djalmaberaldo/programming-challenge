from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] ="sqlite://"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

genres = db.Table ('genres',
    db.Column('genre_id', db.Integer, db.ForeignKey('genre.id'), primary_key=True),
    db.Column('title_id', db.Integer, db.ForeignKey('title.id'), primary_key=True)
)

class Title(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titleIdentifierd = db.Column(db.String(80), unique=True, nullable=False)
    titleType = db.Column(db.String(80), unique=False, nullable=False)
    primaryTitle = db.Column(db.String(80), unique=True, nullable=False)
    originalTitle = db.Column(db.String(80), unique=True, nullable=False)
    isAdult = db.Column(db.Boolean, default=False)
    startYear = db.Column(db.Integer, unique=False, nullable=False)
    endYear = db.Column(db.Integer, unique=False, nullable=False)
    runtimeMinutes = db.Column(db.Integer, unique=False, nullable=False)
    genres = db.relationship('Genre', secondary=genres, backref=db.backref('title', lazy=True), lazy="subquery") 

    def __repr__(self):
        return '<Title %r>' % self.primaryTile

class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    
    def __repr__(self):
        return '<Genre %r>' % self.name


class TitleRatings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numVotes = db.Column(db.Integer, unique=False, nullable=False)
    averageRating = db.Column(db.Float, unique=False, nullable=False)
    titleId = db.Column(db.Integer, db.ForeignKey('title.id'))

    def __repr__(self):
        return '<TitleRatings %r>' % self.numVotes

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

    def __repr__(self):
        return '<Name %r>' % self.tconst

class Profession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return '<Profession %r>' % self.name

@app.route("/")
def home():
    return '';

if __name__ == "__main__":
    app.run(debug=True)