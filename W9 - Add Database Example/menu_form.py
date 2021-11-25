# Imports
import tkinter as tk
from tkinter import ttk
from add_form import run_add, add_role
from delete_form import run_delete, delete_role


# Functions
def add_window():
    root.destroy()
    run_add()


def delete_window():
    root.destroy()
    run_delete()


# Window
root = tk.Tk()
root.title("Menu")
root.geometry("200x100")
root.resizable(width=False, height=False)

# Widgets
lbl_title = ttk.Label(root, text="Menu Screen")
btn_add = ttk.Button(root, text="Add Role", command=add_window)
btn_del = ttk.Button(root, text="Delete Role", command=delete_window)

# Pack
lbl_title.pack(side="top", pady=(10, 10))
btn_add.pack(side="left", padx=(10, 10))
btn_del.pack(side="left", padx=(10, 10))

# Run
root.mainloop()