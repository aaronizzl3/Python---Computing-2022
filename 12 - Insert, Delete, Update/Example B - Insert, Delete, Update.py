import tkinter as tk
import tkinter.ttk as ttk


class Application(tk.Frame):
    def __init__(self, root):
        self.root = root
        self.initialize_user_interface()

    def initialize_user_interface(self):
        # Configure the root object for the Application
        self.root.title("Application")
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.config(background="green")

        # Define the different GUI widgets
        self.name_label = tk.Label(self.root, text="Name:")
        self.name_entry = tk.Entry(self.root)
        self.name_label.grid(row=0, column=0, sticky=tk.W)
        self.name_entry.grid(row=0, column=1)

        self.idnumber_label = tk.Label(self.root, text="ID")
        self.idnumber_entry = tk.Entry(self.root)
        self.idnumber_label.grid(row=1, column=0, sticky=tk.W)
        self.idnumber_entry.grid(row=1, column=1)

        self.submit_button = tk.Button(self.root, text="Insert", command=self.insert_data)
        self.submit_button.grid(row=2, column=1, sticky=tk.W)

        self.delete_button = tk.Button(self.root, text="Delete", command=self.remove_data)
        self.delete_button.grid(row=2, column=2, stick=tk.W)

        self.update_button = tk.Button(self.root, text="Update", command=self.update_form)
        self.update_button.grid(row=2, column=3, stick=tk.W)

        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.quit)
        self.exit_button.grid(row=0, column=3)

        # Set the treeview
        self.tree = ttk.Treeview(self.root, columns=('Name', 'ID'))

        # Set the heading (Attribute Names)
        self.tree.heading('#0', text='Item')
        self.tree.heading('#1', text='Name')
        self.tree.heading('#2', text='ID')

        # Specify attributes of the columns (We want to stretch it!)
        self.tree.column('#0', stretch=tk.YES)
        self.tree.column('#1', stretch=tk.YES)
        self.tree.column('#2', stretch=tk.YES)

        self.tree.grid(row=4, columnspan=4, sticky='nsew')
        self.treeview = self.tree

        self.tree.bind('<ButtonRelease-1>', self.selectItem)

        self.id = 0
        self.iid = 0

    def insert_data(self):
        self.treeview.insert('', 'end', iid=self.iid, text="Item_" + str(self.id),
                             values=(self.name_entry.get(),
                                     self.idnumber_entry.get()))
        self.iid = self.iid + 1
        self.id = self.id + 1

    def update_form(self):
        curItem = self.tree.focus()
        values = self.tree.item(curItem, 'values')
        v1 = values[0]
        v2 = values[1]
        self.entryName = tk.StringVar()
        self.entryID = tk.StringVar()

        self.update_form = tk.Tk()

        self.frm_one = ttk.Frame(self.update_form)
        self.frm_two = ttk.Frame(self.update_form)
        self.frm_three = ttk.Frame(self.update_form)
        self.frm_one.pack(side="top", pady=(10,10))
        self.frm_two.pack(side="top", pady=(10,10))
        self.frm_three.pack(side="top", pady=(10,10))

        self.lbl_name = ttk.Label(self.frm_one, text="Name: ")
        self.ent_name = ttk.Entry(self.frm_one, textvariable=self.entryName)
        self.ent_name.insert(0, v1)
        self.lbl_name.pack(side="left")
        self.ent_name.pack(side="left", padx=(10,10))

        self.lbl_id = ttk.Label(self.frm_two, text="ID: ")
        self.ent_id = ttk.Entry(self.frm_two, textvariable=self.entryID)
        self.ent_id.insert(0, v2)
        self.lbl_id.pack(side="left")
        self.ent_id.pack(side="left", padx=(10,10))

        self.btn_update = ttk.Button(self.frm_three, text="Update", command=lambda: self.update_data(self.ent_name.get(), self.ent_id.get()))
        self.btn_update.pack(side="left")

        self.update_form.mainloop()

    def update_data(self, v1, v2):
        curItem = self.tree.focus()
        values = (v1, v2)
        print(values)
        self.tree.delete(curItem)
        self.treeview.insert('', 'end', iid=curItem, text="Item_" + str(self.id),
                             values=(values))
        self.update_form.destroy()


    def remove_data(self):
        curItem = self.tree.focus()
        self.tree.delete(curItem)

    def selectItem(self, a):
        curItem = self.tree.focus()
        print(self.tree.item(curItem))


app = Application(tk.Tk())
app.root.mainloop()