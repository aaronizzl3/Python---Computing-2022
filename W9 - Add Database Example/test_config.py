import sqlite3
from db_class import Database_Handler


# Select Data from Roles
def Select_Data():
    myDB = Database_Handler("aquarium.db")
    conn, curs = myDB.create_connection()
    query = "SELECT * FROM tblRole"
    curs.execute(query)
    results = curs.fetchall()

    for x in results:
        print(x)


Select_Data()