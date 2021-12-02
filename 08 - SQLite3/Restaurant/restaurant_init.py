# Imports
import sqlite3


# Classes
class Database_Handler:
    db_name = None

    def __init__(self, db_name):
        self.db_name = db_name

    # Create Connection
    def create_connection(self):
        try:
            connection = sqlite3.connect(self.db_name)
            cursor = connection.cursor()
            return connection, cursor
        except sqlite3.Error as error:
            print(f"Error: {error}")

    # Create our Tables
    def initialise_db(self, connection, cursor):
        myQueries = []

        # Store our create query
        query = '''CREATE TABLE tblEmployees(
        id integer PRIMARY KEY,
        forename TEXT NOT NULL,
        surname TEXT NOT NULL,
        role TEXT NOT NULL);'''

        myQueries.append(query)

        query = '''CREATE TABLE tblShifts(
        id integer PRIMARY KEY,
        employee_id INTEGER,
        date DATE,
        startTime TEXT,
        endTime TEXT,
        FOREIGN KEY (employee_id) REFERENCES tblEmployees (id)
        );'''

        myQueries.append(query)

        for x in myQueries:
            try:
                cursor.execute(x)
                connection.commit()
                print("Table created.")
            except sqlite3.Error as error:
                print(f"Error: {error}")

    # Close Connection
    def close_connection(self, connection):
        if connection:
            connection.close()
            print("Connection closed.")
