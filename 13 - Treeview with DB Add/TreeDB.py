from tkinter import ttk
import sqlite3
import tkinter as tk

"""
Use db_init first to initialise the db.
"""

def db_init():
    try:
        connection = sqlite3.connect("ahussain_db.db")
        cursor = connection.cursor()

        # Store our create query
        query = '''CREATE TABLE tblUsers(
        id integer PRIMARY KEY,
        username TEXT NOT NULL,
        password TEXT NOT NULL);'''
        try:
            cursor.execute(query)
            connection.commit()
            print("Table created.")
        except sqlite3.Error as error:
            print(f"Error: {error}")

    except sqlite3.Error as error:
        print(f"Error: {error}")
    finally:
        if connection:
            connection.close()
            print("Connection closed.")


def db_insert():
    try:
        connection = sqlite3.connect("ahussain_db.db")
        cursor = connection.cursor()

        # Query
        query = '''INSERT INTO tblUsers
        (username, password) 
        VALUES
         (?, ?)'''

        data = ("Admin", "Password12")

        cursor.execute(query, data)
        connection.commit()

        query = '''INSERT INTO tblUsers
        (username, password) 
        VALUES
         (?, ?)'''

        data = ("ahussain", "Password12")

        cursor.execute(query, data)
        connection.commit()

        query = '''INSERT INTO tblUsers
        (username, password) 
        VALUES
         (?, ?)'''

        data = ("student", "Password12")

        cursor.execute(query, data)
        connection.commit()

    except sqlite3.Error as error:
        print(f"Error: {error}")
    finally:
        if connection:
            connection.close()
            print("Connection closed.")


def initialise_table(iid):
    connection = sqlite3.connect("ahussain_db.db")
    cursor = connection.cursor()
    query = '''SELECT * FROM tblUsers'''
    cursor.execute(query)
    rows = cursor.fetchall()
    for x in rows:
        print(x)
        myTree.insert('', 'end', iid=iid, values=(x[0], x[1], x[2]))
        iid += 1


def add_user():
    username = ent_username.get()
    password = ent_password.get()

    try:
        connection = sqlite3.connect("ahussain_db.db")
        cursor = connection.cursor()

        # Query
        query = '''INSERT INTO tblUsers
        (username, password) 
        VALUES
         (?, ?)'''

        data = (username, password)

        cursor.execute(query, data)
        connection.commit()
    except sqlite3.Error as error:
        print(f"Error: {error}")
    finally:
        if connection:
            connection.close()
            print("Connection closed.")
        for i in myTree.get_children():
            myTree.delete(i)
        initialise_table(0)


root = tk.Tk()
root.title("Treeview with DB")
root.geometry("500x300")

myTree = ttk.Treeview(root, columns=('size', 'modified'))
myTree['columns'] = ('ID', 'Username', 'Password')
myTree['show'] = 'headings'

myTree.column('ID', width=100)
myTree.heading('ID', text='ID')

myTree.column('Username', width=100)
myTree.heading('Username', text='Username')

myTree.column('Password', width=100)
myTree.heading('Password', text='Password')

myTree.pack()

btn_add = ttk.Button(root, text="Add User", command=add_user)
btn_add.pack()

ent_username = ttk.Entry(root)
ent_password = ttk.Entry(root)
ent_username.pack()
ent_password.pack()

initialise_table(0)

root.mainloop()
