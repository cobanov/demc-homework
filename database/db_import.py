# Module Imports
import mariadb
import sys

# Connect to MariaDB Platform


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


def append_db(conn, query, data):

    # Get Cursor
    cur = conn.cursor()
    cur.execute(query, (data, ))


def read_data():
    pass
