from models import Title, Name
from models import db
import pandas as pd
import gzip
import os
from sqlalchemy import create_engine, or_, text

package_dir = os.path.dirname(os.path.realpath(__file__+'\..\..'))

def get_engine():
    return create_engine("sqlite:///movies.db")

def get_all_titles(search='', filterBy='primaryTitle'):
    filters = add_is_adult_check('' if search == None else filterBy + " like '%"+search+"%' ")
    return db.session.query(Title).filter(text(filters)).limit(1000)

def get_titles_by_year(year=''):
    filters = add_is_adult_check('' if year == None else " startYear="+year)
    return db.session.query(Title).filter(text(filters)).order_by(Title.averageRating.desc()).limit(10)

def get_all_movies(search='', filterBy='primaryTitle', page=0, page_size=4):
    filters = add_movie_filter(add_is_adult_check(search if search == None else filterBy + " like '%"+search+"%' "))
    query = db.session.query(Title).filter(text(filters))
    return query.limit(int(page_size)).offset(int(page)*int(page_size)), query.count()

def get_movies_by_year(year='',  page=0, page_size=4):
    if year is None:
        get_all_movies()
    else:
        filters = add_movie_filter(add_is_adult_check("startYear="+year))
        return db.session.query(Title).filter(text(filters)).order_by(Title.averageRating.desc()).limit(10).offset(int(page)*int(page_size)), 10

def get_all_names(tconst):
    return db.session.query(Name).filter(Name.knownForTitles.like(tconst)), db.session.query(Name).filter(Name.knownForTitles.like(tconst)).count()

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
    df.to_sql('name', engine, if_exists='append', index=False)
    return 'Table loaded'

def read_ratings_data():
    file_to_search_ratings =  os.path.join(package_dir,'dataset\\title.ratings.tsv.gz')
    with gzip.open(file_to_search_ratings,'r') as file_ratings:
        df_ratings = pd.read_csv(file_ratings, sep="\t")
        print('Removing ratings lower than 6')
        df_ratings = df_ratings[df_ratings['averageRating'] >= 6]
    return df_ratings

def add_is_adult_check(arg):
    return "isAdult=0 " if arg is None else arg+" and isAdult=0 "
        
def add_movie_filter(arg):
    return "titleType = 'movie' " if arg is None else arg+" and titleType = 'movie' "
