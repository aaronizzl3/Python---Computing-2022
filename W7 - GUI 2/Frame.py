import tkinter as tk
from tkinter import ttk

# Window
root = tk.Tk()
root.geometry("600x400")

# Frame
main = ttk.Frame(root)
main.pack(side="left", fill="both", expand=True)

# Labels
lbl_one = tk.Label(main, text="Label One", bg="black", fg="white")
lbl_two = tk.Label(main, text="Label Two", bg="red", fg="blue")
lbl_three = tk.Label(main, text="Label Three", bg="yellow", fg="Red")

# Pack
lbl_one.pack(side="top", expand=True, fill="both")
lbl_two.pack(side="top", expand=True, fill="both")
lbl_three.pack(side="top", expand=True, fill="both")

# Run
root.mainloop()