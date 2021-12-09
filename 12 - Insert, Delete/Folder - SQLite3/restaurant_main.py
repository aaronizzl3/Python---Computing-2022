# Imports
import sqlite3
from restaurant_init import Database_Handler

# Main Logic
myObject = Database_Handler("restaurant.db")
conn, curs = myObject.create_connection()
myObject.initialise_db(conn, curs)

# Insert
query = '''
INSERT INTO tblEmployees
(forename, surname, role)
VALUES
(?, ?, ?);'''

data = ("Jordan", "Rutherford", "Main Man")

animalName = "Tiger"
animalAge = 28

try:
    curs.execute(query, data)
    conn.commit()
    print("Query success.")
except sqlite3.Error as error:
    print(f"Error: {error}")

# Select
query = '''SELECT * FROM tblEmployees'''
curs.execute(query)
rows = curs.fetchall()

for x in rows:
    print(x)

# Close Connection
myObject.close_connection(conn)

