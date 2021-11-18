# Import Library
import sqlite3

# Key Steps - Connection, Cursor, Execute, Commit, Close

# 1 - Connect
connection = sqlite3.connect("myDatabase.db")

# 2 - Cursor (this is used to point queries at the database)
cursor = connection.cursor()

# 3 - Execute our Query
try:
    query = '''SELECT * FROM tblUsers;'''
    cursor.execute(query)
    rows = cursor.fetchall()
    for x in rows:
        print(x)
except sqlite3.Error as error:
    print(f"Error: {error}")

# 4 - Commit (makes our data permanent in the database)
connection.commit()

# 5 - Close connection
connection.close()
