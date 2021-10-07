
class Chair:
    # Fields
    brand = ""
    colour = ""
    type = ""
    chair_height = 5

    # Constructor
    def __init__(self, brand, colour, type):
        self.brand = brand
        self.colour = colour
        self.type = type

    # 1 - Raise the chair by 1, no higher than 10
    def raise_seat(self):
        if self.chair_height < 10:
            self.chair_height += 1
            print(f"Chair height has been raised to {self.chair_height}.")


ChairOne = Chair("IKEA", "Black", "Office")
ChairTwo = Chair("Argos", "Cream", "Office")

ChairOne.raise_seat()
ChairTwo.raise_seat()
ChairTwo.raise_seat()








