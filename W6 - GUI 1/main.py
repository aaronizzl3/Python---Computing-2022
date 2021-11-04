import tkinter as tk
from tkinter import ttk


class MyInterface:
    root = None

    def __init__(self):
        self.root = tk.Tk()
        ttk.Label(self.root, text="Hello World!", padding=(30,10)).pack()
        ttk.Button(self.root, text="Bye bye bye!", command=self.destroy_app).pack()
        self.root.mainloop()

    def destroy_app(self):
        Responses.destroy_app(my_responses, self.root)


class Responses:
    def destroy_app(self, root):
        root.destroy()


if __name__ == '__main__':
    my_responses = Responses()
    run_interface = MyInterface()

