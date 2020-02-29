import os
import shutil
import tkinter as tk
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


# def new_meal(ingredients_src, recipie_src, self.meal_name):
#     # assumes for now that the files are formatted to the spec
#     # add functionality to check if the files were already put into the folder
    
#     meal_dir = f"Meals/{self.meal_name}"
#     os.mkdir(meal_dir)

#     recipie_dest = f"{meal_dir}/{self.meal_name}_recipie.txt"
#     ingredients_dest = f"{meal_dir}/{self.meal_name}_ingredients.txt"

    
#     shutil.move(recipie_src,recipie_dest)
#     shutil.move(ingredients_src,ingredients_dest)

#     meal_list = open("Meals/meal_list.txt", "a")
#     meal_list.write(self.meal_name)
#     meal_list.close()


#def make_plan():
    #randomizes the different meals
    #creates weekly plan
    #creates ingredient list

# def meal_add():
#     self.meal_name = name_txt.get()

#     new_meal(ingredient_list_path,recipie_path,self.meal_name) 

# def recipie_getpath():
#     global recipie_path
#     recipie_path = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = [("all files","*.*")])

# def ingredients_getpath():
#     global ingredient_list_path
#     ingredient_list_path = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = [("all files","*.*")])


# window = Tk()

# window.title("Meals on wheels")

# tab_control = ttk.Notebook(window)
# self.tab1 = ttk.Frame(tab_control)
# tab2 = ttk.Frame(tab_control)
# tab_control.add(self.tab1, text = "Add Meal")
# tab_control.add(tab2, text = "Plan")

# #Tab 1
# main_lbl = Label(self.tab1, text="New Meal Entry")
# main_lbl.grid(column=1, row=0)
# name_lbl = Label(self.tab1, text="Meal name")
# name_lbl.grid(column=0, row=1)
# recipie_lbl = Label(self.tab1, text="Path to recipie")
# recipie_lbl.grid(column=0, row=2)
# ingredients_lbl = Label(self.tab1, text="Path to ingredients list")
# ingredients_lbl.grid(column=0, row=3)

# name_txt = Entry(self.tab1,width=30)
# name_txt.grid(column=1, row=1)
# recipie_btn = Button(self.tab1, text="Find Recipie", command=recipie_getpath)
# recipie_btn.grid(column=1, row=2)
# ingredients_btn = Button(self.tab1, text="Find Ingredients", command=ingredients_getpath)
# ingredients_btn.grid(column=1, row=3)

# btn = Button(self.tab1, text="Enter", command=meal_add)
# btn.grid(column=2, row=4)

# #Tab 2

# tab_control.pack(expand=1, fill='both')
# window.mainloop()



class Main_GUI:
    def __init__(self,master):
        self.master = master
        master.title("Meals on wheels")

        self.ingredient_list_path
        self.recipie_path
        self.meal_dir
        self.meal_name
        self.ingredient_list_pat
        self.recipie_dest
        self.ingredients_dest

        self.tab_control = ttk.Notebook(master)
        self.tab1 = ttk.Frame(self.tab_control)
        self.tab2 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab1, text = "Add Meal")
        self.tab_control.add(self.tab2, text = "Plan")

        self.main_lbl = tk.Label(self.tab1, text="New Meal Entry")
        self.main_lbl.grid(column=1, row=0)
        self.name_lbl = tk.Label(self.tab1, text="Meal name")
        self.name_lbl.grid(column=0, row=1)
        self.recipie_lbl = tk.Label(self.tab1, text="Path to recipie")
        self.recipie_lbl.grid(column=0, row=2)
        self.ingredients_lbl = tk.Label(self.tab1, text="Path to ingredients list")
        self.ingredients_lbl.grid(column=0, row=3)

        self.name_txt = tk.Entry(self.tab1,width=30)
        self.name_txt.grid(column=1, row=1)
        self.recipie_btn = tk.Button(self.tab1, text="Find Recipie", command=self.recipie_getpath)
        self.recipie_btn.grid(column=1, row=2)
        self.ingredients_btn = tk.Button(self.tab1, text="Find Ingredients", command=self.ingredients_getpath)
        self.ingredients_btn.grid(column=1, row=3)
        self.btn = tk.Button(self.tab1, text="Enter", command=self.meal_add)
        self.btn.grid(column=2, row=4)

    def recipie_getpath(self):
        self.recipie_path = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = [("all files","*.*")])

    def ingredients_getpath(self):
        self.ingredient_list_path = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = [("all files","*.*")])

    def meal_add(self):
        self.meal_name = self.name_txt.get()

        self.meal_dir = f"Meals/{self.meal_name}"
        os.mkdir(self.meal_dir)

        self.recipie_dest = f"{self.meal_dir}/{self.meal_name}_recipie.txt"
        self.ingredients_dest = f"{self.meal_dir}/{self.meal_name}_ingredients.txt"

        
        shutil.move(self.recipie_path,self.recipie_dest)
        shutil.move(self.ingredient_list_path,self.ingredients_dest)

        meal_list = open("Meals/meal_list.txt", "a")
        meal_list.write(self.meal_name)
        meal_list.close()

        #new_meal(self.ingredient_list_path,self.recipie_path,self.self.meal_name)

    # def new_meal(self,ingredients_src, recipie_src, self.meal_name):
    
    #     self.meal_dir = f"Meals/{self.meal_name}"
    #     os.mkdir(meal_dir)

    #     recipie_dest = f"{meal_dir}/{self.meal_name}_recipie.txt"
    #     ingredients_dest = f"{meal_dir}/{self.meal_name}_ingredients.txt"

        
    #     shutil.move(recipie_src,recipie_dest)
    #     shutil.move(ingredients_src,ingredients_dest)

    #     meal_list = open("Meals/meal_list.txt", "a")
    #     meal_list.write(self.meal_name)
    #     meal_list.close()

if __name__ == "__main__":
    window = tk.Tk()
    my_gui = Main_GUI(window)
    window.mainloop()