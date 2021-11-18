# Imports
from restaurant_init import Database_Handler

# Main Logic
myObject = Database_Handler("restaurant.db")
conn, curs = myObject.create_connection()
myObject.initialise_db(conn, curs)
myObject.close_connection(conn)

