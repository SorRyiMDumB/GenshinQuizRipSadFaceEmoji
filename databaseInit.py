import sqlite3
from sqlite3 import Error
from userdata import userdataraw

'''students contains the table columns '''
students  = """
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  yearlevel INTEGER,
  house TEXT,
  classes TEXT,
  genshin TEXT,
  uni TEXT,
  course TEXT,
  f1 TEXT,
  sport TEXT,
  tutorMath TEXT,
  tutorEng TEXT,
  tutorHums TEXT,
  tutorScience TEXT,
  friends INTEGER
)
"""

def create_connection(path):
    '''
        Creates a connection to a database named data.sqlite, if not found a new database is created 
    '''
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
    '''
        Function takes in a connection and a query and places it in the connection
    '''
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def execute_read_query(connection, query):

    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")



create_connection("data.sqlite")
cursor = connection.cursor()
cursor.execute("DROP TABLE users")
execute_query(connection, students)
execute_query(connection, userdataraw)   
