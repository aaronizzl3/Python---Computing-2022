import sqlite3
from db_class import Database_Handler

myDB = Database_Handler("aquarium.db")
conn, curs = myDB.create_connection()


# Select Role Test
def Select_Data():
    query = "SELECT * FROM tblRole"
    curs.execute(query)
    results = curs.fetchall()

    for x in results:
        print(x)


# Delete Test
def Delete_Data(id):
    query = '''DELETE FROM tblRole WHERE id=?'''
    data = [id]
    curs.execute(query, data)
    conn.commit()


# Run Tests
Select_Data()