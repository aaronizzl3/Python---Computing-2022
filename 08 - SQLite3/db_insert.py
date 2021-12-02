# Imports
import sqlite3

# Connection
try:
    connection = sqlite3.connect("sqlite_python.db")
    cursor = connection.cursor()

    # Query
    query = '''INSERT INTO tblUsers
    (username, password) 
    VALUES
     (?, ?)'''

    data = ("SuperUser", "Qwerty123")

    cursor.execute(query, data)
    connection.commit()

except sqlite3.Error as error:
    print(f"Error: {error}")
finally:
    if connection:
        connection.close()
        print("Connection closed.")