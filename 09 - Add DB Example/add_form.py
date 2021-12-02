import sqlite3
import tkinter as tk
from tkinter import ttk
from db_class import Database_Handler


# Functions
def add_role(r):
    try:
        myDB = Database_Handler("aquarium.db")
        conn, curs = myDB.create_connection()
        myDB.add_role(conn, curs, r)
        print("Added successfully.")
    except sqlite3.Error as error:
        print(f"Error: {error}")


def run_add():
    # Window
    root = tk.Tk()
    root.title("Add Role")
    root.geometry("300x100")
    root.resizable(width=False, height=False)

    # Variables
    role = tk.StringVar()

    # Frames

    # Widgets
    lbl_role = ttk.Label(root, text="Enter Role:")
    ent_role = ttk.Entry(root, textvariable=role)
    btn_add = ttk.Button(root, text="Add", command=lambda: add_role(role.get()))

    # Pack
    lbl_role.pack(side="left", padx=(10, 10))
    ent_role.pack(side="left", padx=(0, 10))
    btn_add.pack(side="left")

    # Run
    root.mainloop()