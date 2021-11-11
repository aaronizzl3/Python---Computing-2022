# Imports
import tkinter as tk
from tkinter import ttk

# Window
root = tk.Tk()
root.geometry("400x200")

# Generate Widgets
rectangle_1 = tk.Label(root, text="Rectangle 1", bg="black", fg="white")
rectangle_2 = tk.Label(root, text="Rectangle 2", bg="yellow", fg="red")

# Pack Widgets
rectangle_1.pack(ipadx=10, ipady=10, fill="both", expand=True, side="left")
rectangle_2.pack(ipadx=10, ipady=10, fill="both", expand=True, side="left")

# Run
root.mainloop()
