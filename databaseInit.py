import sqlite3
from sqlite3 import Error

students  = """
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  year INTEGER,
  house TEXT,
  maths TEXT,
  hums TEXT,
  science TEXT,
  adt TEXT,
  genshin TEXT,
  uni TEXT,
  f1 TEXT,
  sport TEXT,
  tutorMath TEXT,
  tutorEng TEXT,
  tutorHums TEXT,
  tutorScience TEXT,
  tutorAdt TEXT,
  friends INTEGER
);
"""

def create_connection(path):
    global connection
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
        print("\n\nConnection to SQLite DB successful.", "\nDatabase: ", path)
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def delete_all_tasks(conn):
    """
    Delete all rows in the tasks table
    :param conn: Connection to the SQLite database
    :return:
    """
    sql = 'DELETE FROM '
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()


create_connection("data.sqlite")
execute_query(connection, students)  
#delete_all_tasks(connection)
