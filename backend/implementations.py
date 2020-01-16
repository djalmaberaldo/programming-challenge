from models import Title, Name, db
import os
from sqlalchemy import create_engine, or_, text

package_dir = os.path.dirname(os.path.realpath(__file__+'\..\..'))

def get_all_titles(search='', filterBy='primaryTitle'):
    filters = add_is_adult_check('' if search == None else filterBy + " like '%"+search+"%' ")
    return db.session.query(Title).filter(text(filters)).limit(1000)

def get_titles_by_year(year=''):
    filters = add_is_adult_check('' if year == None else " startYear="+year)
    return db.session.query(Title).filter(text(filters)).order_by(Title.averageRating.desc()).limit(10)

def get_all_movies(search='', filterBy='primaryTitle', page=0, page_size=4):
    query = db.session.query(Title)
    if (filterBy=='averageRating'):
        filters = add_movie_filter(add_is_adult_check(search if search == None else "primaryTitle like '%"+search+"%' "))
        query = query.filter(text(filters)).order_by(Title.averageRating.desc())
    else:
        filters = add_movie_filter(add_is_adult_check(search if search == None else filterBy + " like '%"+search+"%' "))
        query =  query.filter(text(filters))
    return query.limit(int(page_size)).offset(int(page)*int(page_size)), query.count()

def get_movies_by_year(year='',  page=0, page_size=4):
    if year is None:
        get_all_movies()
    else:
        filters = add_movie_filter(add_is_adult_check("startYear="+year))
        query = db.session.query(Title).filter(text(filters)).order_by(Title.averageRating.desc()).limit(10).offset(int(page)*int(page_size))
        return query, query.count()

def get_all_names(tconst):
    return db.session.query(Name).filter(Name.knownForTitles.like(tconst)), db.session.query(Name).filter(Name.knownForTitles.like(tconst)).count()

def add_is_adult_check(arg):
    return "isAdult=0 " if arg is None else arg+" and isAdult=0 "
        
def add_movie_filter(arg):
    return "titleType = 'movie' " if arg is None else arg+" and titleType = 'movie' "
