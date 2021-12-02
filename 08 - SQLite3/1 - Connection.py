# Import appropriate libraries
import sqlite3

# Connect to the DB (Creates if it does not exist)
try:
    connection = sqlite3.connect("sqlite_python.db")
    cursor = connection.cursor()
    print("Connection successful.")
except sqlite3.Error as error:
    print(f"Error creating connection. Error: {error}")
finally:
    if connection:
        connection.close()
        print("Connection has been closed.")

