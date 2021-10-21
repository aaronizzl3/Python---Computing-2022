
# Parent Class (Base Class)
class User:
    username = ""

    def __init__(self, username):
        self.username = username

    def printProfile(self):
        print(f"Name: {self.username}")


# Child Class (Derived Class)
class Admin(User):
    def __init__(self):
        User.__init__(self,"AaronH")

    def ChangeName(self):
        self.username = input("Enter new username: ")


# Object
myObject = Admin()
myObject.printProfile()
myObject.ChangeName()
myObject.printProfile()

secondObject = User("Darth Vader")
secondObject.printProfile()
