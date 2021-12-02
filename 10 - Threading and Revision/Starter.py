
"""
Create a class called conversion.

This should have the following traits:
A constructor which sets nth number of hours
Method which converts the hours to seconds
Method which converts the hours to minutes

You should create an object which passes in the number of hours, and then call both methods on the object.
"""


class Conversion:
    hours = None

    def __init__(self, hours):
        self.hours = hours

    def conversion_seconds(self):
        return self.hours * 3600

    def conversion_minutes(self):
        return self.hours * 60


myObject = Conversion(3)
print(myObject.conversion_seconds())
print(myObject.conversion_minutes())
