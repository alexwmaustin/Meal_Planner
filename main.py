import os
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

#def read_ingredients():
    #reads ingredient list given
    #copies contents of ingredients
    #saves into folder with the name of the meal

# def read_recipe():
    #reads recipe_path txt
    #copies, moves, and formats recipe_path content
    #saves into folder with the name of the meal

#def get_meals():
    #grabs the list of meals and displays them

#def make_plan():
    #randomizes the different meals
    #creates weekly plan
    #creates ingredient list

class Main_GUI:
    def __init__(self,master):
        self.master = master
        self.master.title("Meals on wheels")

        # self.ingredient_list_path = " "
        # self.recipe_path = " "
        # self.meal_dir = " "
        # self.meal_name = " "
        # self.recipe_dest = " "
        # self.ingredients_dest = " "

        ###########################################################################################
        #Tab1
        ###########################################################################################
        self.tab_control = ttk.Notebook(self.master)
        self.tab_control.pack()
        self.tab1 = tk.Frame(self.tab_control)
        self.tab1.pack()
        self.tab2 = tk.Frame(self.tab_control)
        self.tab2.pack()
        self.tab_control.add(self.tab1, text = "Add Meal")
        self.tab_control.add(self.tab2, text = "Plan")

        self.main_lbl = tk.Label(self.tab1, text="New Meal Entry")
        self.main_lbl.grid(column=1, row=0)
        self.name_lbl = tk.Label(self.tab1, text="Meal name")
        self.name_lbl.grid(column=0, row=1)
        self.recipe_lbl = tk.Label(self.tab1, text="Path to recipe")
        self.recipe_lbl.grid(column=0, row=2)
        self.ingredients_lbl = tk.Label(self.tab1, text="Path to ingredients list")
        self.ingredients_lbl.grid(column=0, row=3)

        self.name_txt = tk.Entry(self.tab1,width=30)
        self.name_txt.grid(column=1, row=1)
        self.recipe_btn = tk.Button(self.tab1, text="Find recipe", command=self.recipe_getpath)
        self.recipe_btn.grid(column=1, row=2)
        self.ingredients_btn = tk.Button(self.tab1, text="Find Ingredients", command=self.ingredients_getpath)
        self.ingredients_btn.grid(column=1, row=3)
        self.btn = tk.Button(self.tab1, text="Enter", command=self.meal_add)
        self.btn.grid(column=2, row=4)

        ###########################################################################################
        #Tab2
        ###########################################################################################



    def recipe_getpath(self):
        self.recipe_path = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = [("all files","*.*")])

    def ingredients_getpath(self):
        self.ingredient_list_path = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = [("all files","*.*")])

    def meal_add(self):
        self.meal_name = self.name_txt.get()

        self.meal_dir = f"Meals/{self.meal_name}"
        os.mkdir(self.meal_dir)

        self.recipe_dest = f"{self.meal_dir}/{self.meal_name}_recipe.txt"
        self.ingredients_dest = f"{self.meal_dir}/{self.meal_name}_ingredients.txt"

        
        shutil.move(self.recipe_path,self.recipe_dest)
        shutil.move(self.ingredient_list_path,self.ingredients_dest)

        meal_list = open("Meals/meal_list.txt", "a")
        meal_list.write(self.meal_name)
        meal_list.close()


if __name__ == "__main__":
    root = tk.Tk()
    Main_gui = Main_GUI(root)
    root.mainloop()