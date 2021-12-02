# Imports
import tkinter as tk
import random
import time
from tkinter import ttk


# Functions
def diceRoll(dye):
    for x in range(10):
        myResult = random.randint(1, dye)
        if dye == 8:
            lbl_d8.config(text=str(myResult))
        elif dye == 12:
            lbl_d12.config(text=str(myResult))
        elif dye == 20:
            lbl_d20.config(text=str(myResult))

        root.update()
        time.sleep(0.1)

    if dye == 8:
        lbl_d8.config(text=str(myResult))
        if myResult == dye:
            lbl_d8.config(foreground="green")
        else:
            lbl_d8.config(foreground="black")
    elif dye == 12:
        lbl_d12.config(text=str(myResult))
        if myResult == dye:
            lbl_d12.config(foreground="green")
        else:
            lbl_d12.config(foreground="black")
    elif dye == 20:
        lbl_d20.config(text=str(myResult))
        if myResult == dye:
            lbl_d20.config(foreground="green")
        else:
            lbl_d20.config(foreground="black")


# Windows
root = tk.Tk()
root.title = "Dice Roller"

# Frames
frm_d8 = ttk.Frame(root)
frm_d8.pack(side="top", expand=True, fill="both")


frm_d12 = ttk.Frame(root)
frm_d12.pack(side="top", expand=True, fill="both")

frm_d20 = ttk.Frame(root)
frm_d20.pack(side="top", expand=True, fill="both")

# Generate Widgets
btn_d8 = ttk.Button(frm_d8, text="Roll D8", command=lambda: diceRoll(8))
lbl_d8 = ttk.Label(frm_d8, text="")

btn_d12 = ttk.Button(frm_d12, text="Roll D12", command=lambda: diceRoll(12))
lbl_d12 = ttk.Label(frm_d12, text="")

btn_d20 = ttk.Button(frm_d20, text="Roll D20", command=lambda: diceRoll(20))
lbl_d20 = ttk.Label(frm_d20, text="")

# Pack Widgets
btn_d8.pack(side="left")
lbl_d8.pack(side="left", padx=(10, 0))

btn_d12.pack(side="left")
lbl_d12.pack(side="left", padx=(10, 0))

btn_d20.pack(side="left")
lbl_d20.pack(side="left", padx=(10, 0))

# Style
frameStyle = ttk.Style()
frameStyle.configure("TFrame", background="#97bab9")

labelStyle = ttk.Style()
labelStyle.configure("TLabel", background="#5f9e9c")

buttonStyle = ttk.Style()
buttonStyle.configure("TButton", background="#5f9e9c")

# Run Loop
root.mainloop()