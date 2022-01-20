# Imports
import sqlite3
from tkinter import ttk
import tkinter as tk

'''
Everything has been made into one class. I would recommend using two classes:
One for handling the database and one for handling the GUI. You would need to use
objects within these so that they can work together. If you have difficulty with this,
stick with one class.'''

class Login:
    # Class Constructor - sets up elements for our connection, cursor and an empty session
    # The session will be used to store user elements
    def __init__(self, name):
        self.connection = sqlite3.connect(name)
        self.cursor = self.connection.cursor()
        self.session = []

    # DB Initialisation - edit this function to design new tables, and call it to create them
    def db_init(self):
        try:
            # Store our create query
            query = '''CREATE TABLE tblUsers(
            id integer PRIMARY KEY,
            username TEXT NOT NULL,
            password TEXT NOT NULL);'''
            try:
                self.cursor.execute(query)
                self.connection.commit()
                print("Table created.")
            except sqlite3.Error as error:
                print(f"Error: {error}")

        except sqlite3.Error as error:
            print(f"Error: {error}")

        try:
            # Store our create query
            query = '''CREATE TABLE tblPosts(
            id integer PRIMARY KEY,
            title TEXT NOT NULL,
            userID TEXT NOT NULL,
            FOREIGN KEY (userID) REFERENCES tblUsers (id));'''
            try:
                self.cursor.execute(query)
                self.connection.commit()
                print("Table created.")
            except sqlite3.Error as error:
                print(f"Error: {error}")

        except sqlite3.Error as error:
            print(f"Error: {error}")

    # Manually add a user to tblUsers through the console
    def add_user(self):
        try:
            query = '''INSERT INTO tblUsers (username, password) VALUES (?, ?)'''
            username = input("Enter username: ")
            password = input("Enter password: ")
            data = (username, password)
            self.cursor.execute(query, data)
            self.connection.commit()
        except sqlite3.Error as error:
            print(f"Error: {error}")

    # Manually add a post to tblPosts through the console
    def add_post(self):
        try:
            query = '''INSERT INTO tblPosts (title, userID) VALUES (?, ?)'''
            title = input("Enter title: ")
            userID = input("Enter userID: ")
            data = (title, userID)
            self.cursor.execute(query, data)
            self.connection.commit()
        except sqlite3.Error as error:
            print(f"Error: {error}")

    # Manually view users in the console, good for testing purposes
    def view_users(self):
        try:
            query = '''SELECT * FROM tblUsers'''
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            for line in rows:
                print(line)
        except sqlite3.Error as error:
            print(f"Error: {error}")

    # Manually view posts in the console, good for testing purposes
    def view_posts(self):
        try:
            query = '''SELECT * FROM tblPosts'''
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            for line in rows:
                print(line)
        except sqlite3.Error as error:
            print(f"Error: {error}")

    # Function is called when the login button is pressed, trying to find matching details
    def login2(self):
        # 1 - Collects data from our entry fields and adds them to the query
        query = '''SELECT * FROM tblUsers WHERE username=? AND password=?'''
        data = (self.entry_username.get(), self.entry_password.get())
        self.cursor.execute(query, data)
        try:
            # 2 - Looks for matches from our resulting query, if there is, the user is authorised
            rows = self.cursor.fetchall()
            if len(rows) > 0:
                # 3 - Destroy the login window, add the ID and username to the session
                self.login.destroy()
                self.session.append(rows[0][0])
                self.session.append(rows[0][1])
                # 4 - Open up the menu screen
                self.menu_screen()
            else:
                print("USER NOT FOUND")
        except sqlite3.Error as error:
            print(f"Error: {error}")

    # Login GUI, we call this to open as our first screen
    def login_screen(self):
        self.login = tk.Tk()
        self.login.title("LOGIN")

        self.frm_username = ttk.Frame(self.login)
        self.frm_username.pack(expand=True, pady=(10,10))
        self.frm_password = ttk.Frame(self.login)
        self.frm_password.pack(expand=True, pady=(10,10))
        self.frm_submit = ttk.Frame(self.login)
        self.frm_submit.pack(expand=True, pady=(10,10))

        self.lbl_username = ttk.Label(self.frm_username, text="Username")
        self.lbl_username.pack(side="left", padx=(10,10))
        self.entry_username = ttk.Entry(self.frm_username)
        self.entry_username.pack()

        lbl_password = ttk.Label(self.frm_password, text="Password")
        lbl_password.pack(side="left", padx=(10,10))
        self.entry_password = ttk.Entry(self.frm_password)
        self.entry_password.pack()

        self.button_submit = ttk.Button(self.frm_submit, text="Login", command=self.login2)
        self.button_submit.pack()

        self.login.mainloop()

    # Menu GUI, we call this when the user has been successfully logged in
    def menu_screen(self):
        # This code will find all matching posts to the UserID and print them to the console
        self.cursor.execute("SELECT * FROM tblPosts WHERE userID=?", [self.session[0]])
        myPosts = self.cursor.fetchall()
        for line in myPosts:
            print(line)

        self.root = tk.Tk()
        self.label_welcome = ttk.Label(self.root, text=f"Welcome {self.session[0]}! Your ID is {self.session[1]}!")
        self.label_welcome.pack()
        self.root.mainloop()


# Create an object of our class, passing in the DB name, we then open the login
MyObject = Login("myDatabase.db")
MyObject.login_screen()
