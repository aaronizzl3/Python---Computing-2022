from abc import ABC, abstractmethod


class Shape(ABC):
    def PrintSides(self):
        print(f"You have {self.sides} sides")

    @abstractmethod
    def CalculateArea(self):
        pass


class Square(Shape):
    sides = 0

    def __init__(self, sides):
        self.sides = sides

    def CalculateArea(self):
        print("Width x Length")


class Triangle (Shape):
    sides = 0

    def __init__(self, sides):
        self.sides = sides

    def CalculateArea(self):
        print("Base * Height / 2")



# Objects
myShape = Square(4)
myShape.PrintSides()
myShape.CalculateArea()

ShapeTwo = Triangle(3)
ShapeTwo.PrintSides()
ShapeTwo.CalculateArea()

