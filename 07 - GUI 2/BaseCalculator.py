import tkinter as tk
from tkinter import ttk


def addition(x, y):
    ans = x + y
    lbl_answer.config(text=str(ans))


# Main Window
root = tk.Tk()

# Inputs
num_one = tk.DoubleVar()
num_two = tk.DoubleVar()

# Frames
fr_input_one = ttk.Frame(root, padding=(5, 5))
fr_input_one.pack(fill="both")

fr_input_two = ttk.Frame(root, padding=(5, 5))
fr_input_two.pack(fill="both")

fr_answer = ttk.Frame(root)
fr_answer.pack(fill="both")

fr_buttons = ttk.Frame(root)
fr_buttons.pack(fill="both")

# Widgets
lbl_num_one = ttk.Label(fr_input_one, text="Number One: ", padding=(5, 5))
lbl_num_one.pack(side="left")

ent_num_one = ttk.Entry(fr_input_one, textvariable=num_one, width="15")
ent_num_one.pack(side="left")
ent_num_one.focus()

lbl_num_two = ttk.Label(fr_input_two, text="Number Two: ", padding=(5, 5))
lbl_num_two.pack(side="left")

ent_num_two = ttk.Entry(fr_input_two, textvariable=num_two, width="15")
ent_num_two.pack(side="left")

lbl_answer = ttk.Label(fr_answer, text="0.0", padding=(10, 10))
lbl_answer.pack()

btn_get_answer_add = ttk.Button(fr_buttons, text="Add", command=lambda: addition(num_one.get(), num_two.get()))
btn_get_answer_add.pack(side="left", fill="x")

# Run
root.mainloop()
