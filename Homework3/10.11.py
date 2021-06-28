# Mauricio Corado 1254732

class FoodItem:
    def __init__(self, name='None', fat=0.0, carbs=0.0, protein=0.0):  # Created the class and initialized it
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein
# Given Code

    def get_calories(self, num_servings):
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings
        return calories

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))

# Code under a Main method
if __name__ == "__main__":
    Food1 = FoodItem()
# takes input
    item_name = input()
    numFat = float(input())
    numCarbs = float(input())
    numProtein = float(input())

    Food2 = FoodItem(item_name, numFat, numCarbs, numProtein)

    num_servings = float(input())

    cals1 = Food1.get_calories(num_servings)
    cals2 = Food2.get_calories(num_servings)
# Print portion of code
    Food1.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings, cals1))
    print('')
    Food2.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings, cals2))

