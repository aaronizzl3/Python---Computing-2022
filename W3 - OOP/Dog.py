
class Dog:
    name = ""
    breed = ""
    age = ""
    colour = ""

    def __init__(self, name, breed, age, colour):
        self.name = name
        self.breed = breed
        self.age = age
        self.colour = colour

    def eat(self):
        print("I've eaten food!")

    def bark(self):
        print("Woof!")


