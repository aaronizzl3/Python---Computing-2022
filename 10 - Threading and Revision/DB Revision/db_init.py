# Imports
import sqlite3

# Connection
try:
    connection = sqlite3.connect("sqlite_python.db")
    cursor = connection.cursor()

    # Store our create query
    query = '''CREATE TABLE tblUsers(
    id integer PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL);'''
    try:
        cursor.execute(query)
        connection.commit()
        print("Table created.")
    except sqlite3.Error as error:
        print(f"Error: {error}")

except sqlite3.Error as error:
    print(f"Error: {error}")
finally:
    if connection:
        connection.close()
        print("Connection closed.")