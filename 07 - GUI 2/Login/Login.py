import tkinter as tk
from tkinter import ttk


def authenticate(usern, passw):
    # TODO: You should use a far better method of authenticating the user.
    if usern == "Admin" and passw == "Password":
        lbl_authenticate.config(text="Authenticated", foreground="green")
    else:
        lbl_authenticate.config(text="Error.", foreground="red")


def new_window():
    # TODO: You could include some profile information on this screen.
    root.destroy()
    window_auth = tk.Tk()
    # sets the title of the
    # Toplevel widget
    window_auth.title("New Window")

    # sets the geometry of toplevel
    window_auth.geometry("650x150")


root = tk.Tk()
root.geometry("650x150")

username = tk.StringVar()
password = tk.StringVar()

lbl_username = ttk.Label(root, text="Username: ")
lbl_username.pack(side="left", padx=(0, 15))

ent_username = ttk.Entry(root, width=20, textvariable=username)
ent_username.pack(side="left")

lbl_password = ttk.Label(root, text="Password: ")
lbl_password.pack(side="left", padx=(0, 15))

ent_password = ttk.Entry(root, width=20, textvariable=password)
ent_password.pack(side="left")

btn_login = ttk.Button(root, text="Login", command=lambda: authenticate(username.get(), password.get()))
#btn_login = ttk.Button(root, text="Login", command=new_window)
btn_login.pack(side="left")

lbl_authenticate = ttk.Label(root, text="")
lbl_authenticate.pack(side="left", padx=(50, 0))

root.mainloop()