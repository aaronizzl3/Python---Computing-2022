""" Database Class for all functionality.
Should be made more efficient.
Must run db_init to create the tables."""

# Import appropriate libraries
import sqlite3

# TODO: Make a separate class for certain tables?


class Database_Handler:
    """This class is responsible for handling
    CRUD capabilities within any application.
    db_name - database name
    connection - specify the database
    cursor - used as a pointer for queries"""

    # Assign DB Name
    def __init__(self, db_name):
        self.db_name = db_name

    # Create Connection and Cursor
    # TODO: Make connection and cursor fields for class
    def create_connection(self):
        try:
            connection = sqlite3.connect(self.db_name)
            cursor = connection.cursor()
            return connection, cursor
        except sqlite3.Error as error:
            print(f"Error initialising connection: {error}")

    # Database Initialisation
    # TODO: Pass through an SQL file to be read and ran
    # TODO: Alternatively, pass through a create query
    def db_init(self, connection, cursor):
        myQueries = []

        query = '''CREATE TABLE tblRole(
        id integer PRIMARY KEY,
        Role TEXT NOT NULL)'''
        myQueries.append(query)

        query = '''CREATE TABLE tblUsers(
        id integer PRIMARY KEY,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        role INTEGER,
        FOREIGN KEY (role) REFERENCES tblRole (id))'''
        myQueries.append(query)

        for x in myQueries:
            try:
                cursor.execute(x)
                connection.commit()
                print("Table created.")
            except sqlite3.Error as error:
                print(f"Error: {error}")

    # TODO: Close DB function
    def close_db(self, connection):
        if connection:
            connection.close()
            print("Connection closed.")

    ''' CRUD FUNCTIONALITY'''
    def add_role(self, connection, cursor, name):
        query = '''INSERT INTO tblRole (Role) VALUES (?)'''

        try:
            data = [name]
            cursor.execute(query, data)
            connection.commit()
            print("Query successful.")
        except sqlite3.Error as error:
            print(f"Error: {error}")

    def view_role(self, connection, cursor):
        query = '''SELECT * FROM tblRole'''
        cursor.execute(query)
        result = cursor.fetchall()

        for x in result:
            print(x)

    def update_role(self):
        pass

    def delete_role(self, connection, cursor, id):
        query = '''DELETE FROM tblRole WHERE id=?'''
        data = [id]

        try:
            cursor.execute(query, data)
            connection.commit()
            print("Data deleted.")
        except sqlite3.Error as error:
            print(f"Error: {error}")


