import tkinter as tk
from tkinter import ttk

root = tk.Tk()

myList = [
    ["Aaron Hussain", "Computing Lecturer"],
    ["Murray Lambert", "Games Lecturer"],
    ["Neil Layfield", "Cyber Security Lecturer"],
    ["Bernard Murphy", "Networking Lecturer"]
]

for row in myList:
    tk.Label(root, text=f"Name: {row[0]}\nRole: {row[1]}\n \n").pack(side="top")

root.mainloop()
