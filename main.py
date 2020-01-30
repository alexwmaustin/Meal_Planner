class Meal:
    def __init__(self, ingredients, recipie, meal_name):
        self.ingredients = ingredients
        self.recipie = recipie
        self.meal_name = meal_name

        #save the meal name to the list
        read_ingredients(self.ingredients)
        read_recipie(self.recipie)

    def read_ingredients(self):
        #reads ingredient list given
        #copies contents of ingredients
        #saves into folder with the name of the meal

    def read_recipie(self):
        #reads recipie txt
        #copies, moves, and formats recipie content
        #saves into folder with the name of the meal

def get_meals():
    #grabs the list of meals and displays them

def new_meal():
    #this is where the meal object is created

def make_plan():
    #randomizes the different meals
    #creates weekly plan
    #creates ingredient list
    
def main():
    #Read the list of meals
    #perform replacement
    #ask for input from the user