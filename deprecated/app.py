# Module Imports
import mysql.connector
import sys


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
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
    return conn


def read_data(conn, query):

    # Get Cursor
    cur = conn.cursor()
    cur.execute(query)
    results = cur.fetchall()

    print("Here is the first five examples what you got!")
    for x in results[:5]:
        print(x)

    return results


conn = connect_db()
data = read_data(conn, 'select * from episodes limit 10')
