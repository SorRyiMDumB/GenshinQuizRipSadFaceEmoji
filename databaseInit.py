import sqlite3
from sqlite3 import Error

create_users  = """
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  age INTEGER,
  gender TEXT,
  nationality TEXT
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
    sql = 'DELETE FROM create_users'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()


create_connection("data.sqlite")
execute_query(connection, create_users)  
delete_all_tasks(connection)
