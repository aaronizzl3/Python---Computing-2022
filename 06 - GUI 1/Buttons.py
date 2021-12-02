import tkinter as tk
from tkinter import ttk


def say_hello():
    print("Hello World!")


def say_goodbye():
    print("Goodbye!")
    root.destroy()


root = tk.Tk()
root.title("My Application")

btn_hello = ttk.Button(root, text="Say Hello!", command=say_hello)
btn_hello.pack()

root.mainloop()