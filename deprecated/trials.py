import sqlalchemy
import csv
import mariadb
import sys
import pandas as pd
from sqlalchemy import create_engine
import pymysql
import numpy

basics_path = './datasets/title.basics.tsv'
akas_path = './datasets/title.akas.tsv'
crew_path = './datasets/title.crew.tsv'
episode_path = './datasets/title.episode.tsv'
principals_path = './datasets/title.principals.tsv'
ratings_path = './datasets/title.ratings.tsv'

basics_query = "INSERT INTO basics VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
akas_query = "INSERT INTO akas (first_name,last_name) VALUES (?, ?)"
crew_query = "INSERT INTO crew (first_name,last_name) VALUES (?, ?)"
episode_query = "INSERT INTO episode (first_name,last_name) VALUES (?, ?)"
principals_query = "INSERT INTO principals (first_name,last_name) VALUES (?, ?)"
ratings_query = "INSERT INTO ratings (first_name,last_name) VALUES (?, ?)"


datasets = {basics_path: basics_query,
            akas_path: akas_query,
            crew_path: crew_query,
            episode_path: episode_query,
            principals_path: principals_query,
            ratings_path: ratings_query}

# for path, query in datasets.items():
#     print(path, query)


def connect_db():
    try:
        conn = mariadb.connect(
            user="root",
            password="55347314",
            host="127.0.0.1",
            port=3306,
            database="imdb"

        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
    return conn


SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:55347314@127.0.0.1/imdb'

# Test if it works
# engine = sqlalchemy.create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
# data = pd.read_csv(basics_path, delimiter='\t')
# print('data has been read')
# # data = data.replace(r'\N', numpy.nan)
# # print('data has been replaced')v

# conn = connect_db()
# print('connected')

# cur = conn.cursor()
# for x, y in data.iterrows():
#     print(x, '/', data.shape[0])
#     print(tuple(y))
#     cur.execute(basics_query, tuple(y))
# conn.commit()


conn = connect_db()
print('connected')
cur = conn.cursor()

file = open(basics_path)
csv_data = csv.reader(file, delimiter='\t')

skipHeader = True
csv_data.__next__()
i=0
for row in csv_data:
    i += 1
    cur.execute(basics_query, tuple(row))
    print(i )

conn.commit()
