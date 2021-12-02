
# TODO: Create a class which outputs total price for meals
# TODO: Standard - £2.00 // Luxury - £3.00 // VAT = 20%
# TODO: Number of overall students is (n)

# Class Definition
class MealCalculator:
    students = None

    def __init__(self, students):
        self.students = students

    def MealType(self):
        standard_meals = int(input(f"(Total: {self.students})"
                                   f"\nHow many students will have standard meals? "))
        luxury_meals = self.students - standard_meals
        return standard_meals, luxury_meals

    def CalculatePrice(self, standard, luxury):
        total = (standard * 2) + (luxury * 3)
        total_with_vat = total * 1.2
        return total, total_with_vat

    def OutputTotals(self, total, total_with_vat):
        print(f"Price: £{total}\nPrice (with VAT): £{total_with_vat}")


# Main Logic
myTrip = MealCalculator(30)
stan, lux = myTrip.MealType()
total, vat = myTrip.CalculatePrice(stan, lux)
myTrip.OutputTotals(total, vat)
