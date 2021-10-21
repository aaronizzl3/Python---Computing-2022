import sys

class Menu:
    userObject = None

    def __init__(self, userObject):
        self.userObject = userObject

        if self.userObject.auth:
            option = int(input(f"Welcome {self.userObject.username}!\n"
                               f"1 - Say Hello\n"
                               f"2 - Exit Program\n"
                               f"Option: "))

            if option == 1:
                self.SayHello()
            elif option == 2:
                print("Exiting.")
                sys.exit()
            else:
                print("Invalid input.")

    def SayHello(self):
        print(f"Hello {self.userObject.username}!")