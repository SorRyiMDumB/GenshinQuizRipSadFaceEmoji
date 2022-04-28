import sqlite3
from sqlite3 import Error
from tkinter.messagebox import YES
from userdata import userdataraw

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

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
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
execute_query(connection, students)
execute_query(connection, userdataraw)   

select_users = "SELECT * from users"
yes = execute_read_query(connection, select_users)

for i in yes:
    print(i)

#delete_all_tasks(connection)
