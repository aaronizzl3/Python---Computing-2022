# Imports
import sys

# Globals
accounts = [
    ["Lemon", "password12"],
    ["Aaron", "qwerty123"],
    ["Admin", "Poophead"]
]

# Classes
class User:
    username = ""
    auth = None
    role = ""

    def __init__(self, username, auth, role="Standard"):
        self.username = username
        self.auth = auth
        self.role = role


class Menu:
    userObject = None

    def __init__(self, userObject):
        self.userObject = userObject

        if self.userObject.auth:
            print(f"Welcome {self.userObject.username}!\n1 - Say Hello\n2 - Exit")
            option = int(input("Option: "))

            if option == 1:
                self.sayHello()
            elif option == 2:
                self.exitProgram()
            else:
                print("Invalid input.")
        else:
            print("Unauthorised access.")
            sys.exit()

    def sayHello(self):
        print(f"Hello {self.userObject.username}! Welcome to the matrix.")

    def exitProgram(self):
        print("Exitng program.")
        sys.exit()


# Main Logic
username = input("Enter username: ")
password = input("Enter password: ")

for i in accounts:
    if i[0] == username and i[1] == password:
        userObject = User(i[0], True)
        running = Menu(userObject)
        break