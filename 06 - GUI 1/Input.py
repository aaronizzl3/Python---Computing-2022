import tkinter as tk
from tkinter import ttk


def say_hello():
    print(f"Hello, {name.get() or 'mysterious stranger!'}")


def quit_application():
    root.destroy()


root = tk.Tk()
root.geometry("400x200")

name = tk.StringVar()

lbl_name = ttk.Label(root, text="Name: ")
lbl_name.pack(side="left", padx=(0, 15))

ent_name = ttk.Entry(root, width=20, textvariable=name)
ent_name.pack(side="left")

btn_hello = ttk.Button(root, text="Say Hello!", command=say_hello)
btn_hello.pack(side="left")

root.mainloop()