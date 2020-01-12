from models import Title, Name
from db import db
import pandas as pd
import gzip
import os
from sqlalchemy import create_engine

package_dir = os.path.dirname(os.path.realpath(__file__))

def get_all_titles():
    title = Title()
    return Title.query.limit(10)

def get_all_names():
    name = Name()
    return Name.query.limit(10)

def insert_data_title():
    print('Inserting title data into table')
    engine = create_engine("sqlite:///movies.db")
    file_to_search =  os.path.join(package_dir,'../dataset/title.basics.tsv.gz')
    with gzip.open(file_to_search,'r') as file:
        print('Reading tsv file')
        df = pd.read_csv(file, sep="\t")
        print('Renaming tconst column')
        df = df.rename(columns={"tconst":"titleIdentifier"})
        print('Changing endYear n to 0')
        df = df.replace({'endYear': "\\N"}, 0)
        print('Removing movies out of pattern at isAdult column')
        df = df.loc[df['isAdult'].isin([0,1])]
        print('Removing null values')
        df = df.dropna()
        print(df.head())
        df.to_sql('title', engine, if_exists='append', index=False)
    return 'Table Loaded'

def insert_data_name():
    print('Inserting title data into table')
    engine = create_engine("sqlite:///movies.db")
    file_to_search =  os.path.join(package_dir,'../dataset/name.basics.tsv.gz')
    with gzip.open(file_to_search,'r') as file:
        print('Reading tsv file')
        df = pd.read_csv(file, sep="\t")
        print('Removing null values')
        df = df.dropna()
        print(df.head())
        df = df.loc[~df['knownForTitles'].isin(["\\N"])]
        df = df.loc[~df['primaryProfession'].isin(["\\N"])]
        df.to_sql('name', engine, if_exists='append', index=False)
    return 'Table loaded'