# Module Imports
import mysql.connector
import sys
import time


def connect_db():
    try:
        conn = mysql.connector.connect(
            user="root",
            password="55347314",
            host="127.0.0.1",
            port=3306,
            database="imdb"

        )
        print('Connected!')

    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL Platform: {e}")
        sys.exit(1)
    return conn


def read_data(conn, query):

    cur = conn.cursor()

    start = time.time()
    cur.execute(query)
    elapsed_time = time.time() - start

    results = cur.fetchall()

    for i in results[:5]:
        print(i)

    return results, elapsed_time
