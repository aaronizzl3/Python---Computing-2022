import sqlite3
import tkinter as tk
from tkinter import ttk
from db_class import Database_Handler


# Functions
def delete_role(r):
    try:
        myDB = Database_Handler("aquarium.db")
        conn, curs = myDB.create_connection()
        myDB.delete_role(conn, curs, r)
        print("Delete successful.")
    except sqlite3.Error as error:
        print(f"Error: {error}")


def run_delete():
    # Window
    root = tk.Tk()
    root.title("Delete Role")
    root.geometry("300x100")
    root.resizable(width=False, height=False)

    # Variables
    role = tk.StringVar()

    # Frames

    # Widgets
    lbl_role = ttk.Label(root, text="Enter Role ID:")
    ent_role = ttk.Entry(root, textvariable=role)
    btn_delete = ttk.Button(root, text="Delete", command=lambda: delete_role(role.get()))

    # Pack
    lbl_role.pack(side="left", padx=(10, 10))
    ent_role.pack(side="left", padx=(0, 10))
    btn_delete.pack(side="left")

    # Run
    root.mainloop()