import tkinter as tk
from tkinter import ttk
from random import randrange
import time

def D4():
    lbl_answer.config(foreground="black")

    for x in range(10):
        answer = randrange(1, 5)
        lbl_answer.config(text=str(answer))
        root.update()
        time.sleep(0.2)

    if answer == 4:
        lbl_answer.config(foreground="purple")

    else:
        lbl_answer.config(foreground="green")

def D6():
    lbl_answer.config(foreground="black")
    for x in range(10):
        answer = randrange(1, 7)
        lbl_answer.config(text=str(answer))
        root.update()
        time.sleep(0.2)

    if answer == 6:
        lbl_answer.config(foreground="purple")

    else:
        lbl_answer.config(foreground="green")

def D8():
    lbl_answer.config(foreground="black")
    for x in range(10):
        answer = randrange(1, 9)
        lbl_answer.config(text=str(answer))
        root.update()
        time.sleep(0.2)

    if answer == 8:
        lbl_answer.config(foreground="purple")

    else:
        lbl_answer.config(foreground="green")

def D10():
    lbl_answer.config(foreground="black")
    for x in range(10):
        answer = randrange(1, 11)
        lbl_answer.config(text=str(answer))
        root.update()
        time.sleep(0.2)

    if answer == 10:
        lbl_answer.config(foreground="purple")

    else:
        lbl_answer.config(foreground="green")

def D12():
    lbl_answer.config(foreground="black")
    for x in range(10):
        answer = randrange(1, 13)
        lbl_answer.config(text=str(answer))
        root.update()
        time.sleep(0.2)

    if answer == 12:
        lbl_answer.config(foreground="purple")

    else:
        lbl_answer.config(foreground="green")

def D20():
    lbl_answer.config(foreground="black")
    for x in range(10):
        answer = randrange(1, 21)
        lbl_answer.config(text=str(answer))
        root.update()
        time.sleep(0.2)

    if answer == 20:
        lbl_answer.config(foreground="purple")

    else:
        lbl_answer.config(foreground="green")

def reset():
    lbl_answer.config(text=0, fg="Black")

root =tk.Tk()
root.title("Calculator")
root.configure(bg="#8383fa")
root.geometry("600x200")


btn_d4 = ttk.Button(root, text="D4", command=D4).pack(side="left", fill="x")

btn_d6 = ttk.Button(root, text="D6", command=D6).pack(side="left", fill="x")

btn_d8 = ttk.Button(root, text="D8", command=D8).pack(side="left", fill="x")

btn_d10 = ttk.Button(root, text="D10", command=D10).pack(side="left", fill="x")

btn_d12 = ttk.Button(root, text="D12", command=D12).pack(side="left", fill="x")

btn_d20 = ttk.Button(root, text="D20", command=D20).pack(side="left", fill="x")

btn_reset = ttk.Button(root, text="Reset", command=reset).pack(side="right", fill="x")

lbl_answer = ttk.Label(root, text="", padding=(10, 10))
lbl_answer.pack()

root.mainloop()