import tkinter as tk
from tkinter import ttk


def get_answer(operation):
    x = num_one.get()
    y = num_two.get()

    if operation == "+":
        ans = x + y
    elif operation == "-":
        ans = x - y
    elif operation == "/":
        ans = x / y
    elif operation == "*":
        ans = x * y

    lbl_answer.config(text=str(ans))


def reset():
    ent_num_one.delete(0, 'end')
    ent_num_two.delete(0, 'end')
    lbl_answer.config(text="0")


root = tk.Tk()

num_one = tk.IntVar(value="")
num_two = tk.IntVar(value="")

ent_num_one = ttk.Entry(root, textvariable=num_one)
ent_num_one.pack()
ent_num_two = ttk.Entry(root, textvariable=num_two)
ent_num_two.pack()

lbl_answer = ttk.Label(root, text="0", padding=(10,10))
lbl_answer.pack()

btn_add = ttk.Button(root, text=" + ", command=lambda: get_answer("+")).pack()
btn_subtract = ttk.Button(root, text=" - ", command=lambda: get_answer("-")).pack()
btn_divide = ttk.Button(root, text=" / ", command=lambda: get_answer("/")).pack()
btn_multiply = ttk.Button(root, text=" * ", command=lambda: get_answer("*")).pack()

btn_reset = ttk.Button(root, text="Reset", command=reset).pack()

root.mainloop()