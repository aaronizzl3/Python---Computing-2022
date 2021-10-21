
class Person:
    __name = ""

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        print(f"Name: {self.__name}")

    def set_name(self, name):
        name += " - The Squid Game"
        self.__name = name


myObject = Person("Aaron")
myObject.get_name()
myObject.set_name("Vader")
myObject.get_name()