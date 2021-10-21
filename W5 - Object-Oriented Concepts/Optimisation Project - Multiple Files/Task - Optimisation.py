"""
This is an optimisation task. Previous procedural code is being updated into OOP.
"""

# Imports
from Class_User import User
from Class_Menu import Menu

# Globals
accounts = [
    ["Lemon", "Password12"],
    ["Student", "qwerty123"]
]

# Main Logic
username = input("Enter username: ")
password = input("Enter password: ")

for i in accounts:
    if i[0] == username and i[1] == password:
        myUser = User(i[0], True)
        runMenu = Menu(myUser)
        break