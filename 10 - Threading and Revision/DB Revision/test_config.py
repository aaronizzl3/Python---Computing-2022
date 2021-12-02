import sqlite3

# Create Connection and Cursor
try:
    connection = sqlite3.connect("sqlite_python.db")
    cursor = connection.cursor()
except sqlite3.Error as error:
    print(f"Error: {error}")


# Test Functions
def check_users(curs):
    query = '''SELECT * FROM tblusers'''
    curs.execute(query)
    rows = curs.fetchall()
    for x in rows:
        print(x)


# Test Logic
check_users(cursor)