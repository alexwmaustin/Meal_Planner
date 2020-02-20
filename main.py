import os
import shutil
from tkinter import *
from tkinter import filedialog
from tkinter import ttk

#def read_ingredients():
    #reads ingredient list given
    #copies contents of ingredients
    #saves into folder with the name of the meal

# def read_recipie():
    #reads recipie_path txt
    #copies, moves, and formats recipie_path content
    #saves into folder with the name of the meal

#def get_meals():
    #grabs the list of meals and displays them


def new_meal(ingredients, recipie_path, meal_name):
    # assumes for now that the files are formatted to the spec
    # add functionality to check if the files were already put into the folder
    
    meal_dir = f"Meals/{meal_name}"
    os.mkdir(meal_dir)

    recipie_dest = f"{meal_dir}/{meal_name}_recipie.txt"
    ingredients_dest = f"{meal_dir}/{meal_name}_ingredients.txt"

    
    shutil.move(recipie_path,recipie_dest)
    shutil.move(ingredients,ingredients_dest)

    meal_list = open("Meals/meal_list.txt", "a")
    meal_list.write(meal_name)
    meal_list.close()


#def make_plan():
    #randomizes the different meals
    #creates weekly plan
    #creates ingredient list

def meal_add():
    meal_name = name_txt.get()

    new_meal(ingredient_list_path,recipie_path,meal_name) 

def recipie_getpath():
    global recipie_path
    recipie_path = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = [("all files","*.*")])

def ingredients_getpath():
    global ingredient_list_path
    ingredient_list_path = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = [("all files","*.*")])


window = Tk()

window.title("Meals on wheels")

tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text = "Add Meal")
tab_control.add(tab2, text = "Plan")

main_lbl = Label(tab1, text="New Meal Entry")
main_lbl.grid(column=0, row=0)
name_lbl = Label(tab1, text="Meal name")
name_lbl.grid(column=0, row=1)
recipie_lbl = Label(tab1, text="Path to recipie_path")
recipie_lbl.grid(column=0, row=2)
ingredients_lbl = Label(tab1, text="Path to ingredients list")
ingredients_lbl.grid(column=0, row=3)

name_txt = Entry(tab1,width=30)
name_txt.grid(column=1, row=1)
recipie_btn = Button(tab1, text="Find Recipie", command=recipie_getpath)
recipie_btn.grid(column=1, row=2)
ingredients_btn = Button(tab1, text="Find Ingredients", command=ingredients_getpath)
ingredients_btn.grid(column=1, row=3)

btn = Button(tab1, text="Enter", command=meal_add)
btn.grid(column=2, row=4)

tab_control.pack(expand=1, fill='both')
window.mainloop()