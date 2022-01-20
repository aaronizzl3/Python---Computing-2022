
'''
1 - Import library
2 - Setup Window
3 - Create and PACK widgets
4 - Run the window
'''

# Import Libraries
from tkinter import ttk
import tkinter as tk


# Functions and Logic
def login():
    if entry_username.get() == "admin" and entry_password.get() == "password":
        print("AUTHORISED.")
        menu = tk.Tk()
        main.destroy()
        menu.mainloop()
    else:
        print("INCORRECT CREDENTIALS.")


# Setup Main Window
main = tk.Tk()
main.geometry("250x125")
main.title("Main Window")

# Setup Frames
frame_one = tk.Frame(main)
frame_one.pack(fill="both", expand=True)

frame_two = tk.Frame(main)
frame_two.pack(fill="both", expand=True)

frame_three = tk.Frame(main)
frame_three.pack(fill="both", expand=True)

# Frame One
label_username = ttk.Label(frame_one, text="Username")
label_username.pack(side="left", padx=(10,10))

entry_username = ttk.Entry(frame_one)
entry_username.pack(side="left", padx=(10,10))

# Frame Two
label_password = ttk.Label(frame_two, text="Password")
label_password.pack(side="left", padx=(10,10))

entry_password = ttk.Entry(frame_two)
entry_password.pack(side="left", padx=(10,10))

# Frame Three
button_login = ttk.Button(frame_three, text="Login", command=login)
button_login.pack()

# Run Program
main.mainloop()
