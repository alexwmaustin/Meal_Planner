import os
import random
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

class Main_GUI:
    def __init__(self,master):
        self.master = master
        self.master.title("Meals on wheels")
        #self.master.minsize(400,500)


        self.tab_control = ttk.Notebook(self.master)
        self.tab_control.pack()
        self.tab1 = tk.Frame(self.tab_control)
        self.tab1.pack()
        self.tab2 = tk.Frame(self.tab_control)
        self.tab2.pack()
        self.tab_control.add(self.tab1, text = "Add Meal")
        self.tab_control.add(self.tab2, text = "Plan")

        ###########################################################################################
        #Tab1
        ###########################################################################################

        self.main_lbl = tk.Label(self.tab1, text="New Meal Entry")
        self.main_lbl.grid(column=1, row=0, columnspan=2)
        
        self.name_lbl = tk.Label(self.tab1, text="Meal name:")
        self.name_lbl.grid(column=0, row=1, sticky='W')
        self.name_txt = tk.Entry(self.tab1,width=30)
        self.name_txt.grid(column=1, row=1, padx=5, columnspan=2)

        self.recipe_lbl = tk.Label(self.tab1, text="Recipe")
        self.recipe_lbl.grid(column=0, row=2, sticky='W')
        self.recipe_btn = tk.Button(self.tab1, text="import", command=self.recipe_getpath)
        self.recipe_btn.grid(column=1, row=2, sticky='W')
        self.recipe_file_lbl = tk.Label(self.tab1, text="none")
        self.recipe_file_lbl.grid(column=2, row=2, sticky='W')

        self.ingredients_lbl = tk.Label(self.tab1, text="Ingredients")
        self.ingredients_lbl.grid(column=0, row=3, sticky='W')
        self.ingredients_btn = tk.Button(self.tab1, text="import", command=self.ingredients_getpath)
        self.ingredients_btn.grid(column=1, row=3, sticky='W')
        self.ingredients_file_lbl = tk.Label(self.tab1, text="none")
        self.ingredients_file_lbl.grid(column=2, row=3, sticky='W')


        self.btn = tk.Button(self.tab1, text="Enter", command=self.meal_add)
        self.btn.grid(column=2, row=4, sticky='E')

        ###########################################################################################
        #Tab2
        ###########################################################################################

        self.plan_lbl = tk.Label(self.tab2, text="Plan")
        self.plan_lbl.grid(column=0, row=0, sticky='W')
        self.plan_btn = tk.Button(self.tab2, text="Create", command=self.plan_create)
        self.plan_btn.grid(column=1, row=0, sticky='W')

        self.sun_lbl = tk.Label(self.tab2, text="Sun:")
        self.sun_lbl.grid(column=0, row=1, sticky='E')
        self.sun_meal =tk.Label(self.tab2, text="")
        self.sun_meal.grid(column=1,row=1, sticky='W')

        self.mon_lbl = tk.Label(self.tab2, text="Mon:")
        self.mon_lbl.grid(column=0, row=2, sticky='E')
        self.mon_meal =tk.Label(self.tab2, text="")
        self.mon_meal.grid(column=1,row=2, sticky='W')

        self.tue_lbl = tk.Label(self.tab2, text="Tue:")
        self.tue_lbl.grid(column=0, row=3, sticky='E')
        self.tue_meal =tk.Label(self.tab2, text="")
        self.tue_meal.grid(column=1,row=3, sticky='W')

        self.wed_lbl = tk.Label(self.tab2, text="Wed:")
        self.wed_lbl.grid(column=0, row=4, sticky='E')
        self.wed_meal =tk.Label(self.tab2, text="")
        self.wed_meal.grid(column=1,row=4, sticky='W')

        self.thu_lbl = tk.Label(self.tab2, text="Thu:")
        self.thu_lbl.grid(column=0, row=5, sticky='E')
        self.thu_meal =tk.Label(self.tab2, text="")
        self.thu_meal.grid(column=1,row=5, sticky='W')

        self.fri_lbl = tk.Label(self.tab2, text="Fri:")
        self.fri_lbl.grid(column=0, row=6, sticky='E')
        self.fri_meal =tk.Label(self.tab2, text="")
        self.fri_meal.grid(column=1,row=6, sticky='W')
        
        self.sat_lbl = tk.Label(self.tab2, text="Sat:")
        self.sat_lbl.grid(column=0, row=7, sticky='E')
        self.sat_meal =tk.Label(self.tab2, text="")
        self.sat_meal.grid(column=1,row=7, sticky='W')

    def recipe_getpath(self):
        self.recipe_path = filedialog.askopenfilename(initialdir = "/Users/Alex/Documents",title = "Select file",filetypes = [("all files","*.*")])
        self.recipe_file = self.recipe_path[self.recipe_path.rfind('/')+1:len(self.recipe_path)]
        self.recipe_file_lbl.config(text= self.recipe_file)

    def ingredients_getpath(self):
        self.ingredient_list_path = filedialog.askopenfilename(initialdir = "/Users/Alex/Documents",title = "Select file",filetypes = [("all files","*.*")])
        self.ingredient_file = self.ingredient_list_path[self.ingredient_list_path.rfind('/')+1:len(self.ingredient_list_path)]
        self.ingredients_file_lbl.config(text= self.ingredient_file)

    def meal_add(self):
        self.meal_name = self.name_txt.get()

        self.meal_dir = f"Meals/{self.meal_name}"
        os.mkdir(self.meal_dir)

        self.recipe_dest = f"{self.meal_dir}/{self.meal_name}_recipe.txt"
        self.ingredients_dest = f"{self.meal_dir}/{self.meal_name}_ingredients.txt"

        
        shutil.move(self.recipe_path,self.recipe_dest)
        shutil.move(self.ingredient_list_path,self.ingredients_dest)

        self.name_txt.delete(0,"end")
        self.recipe_file_lbl.config(text= "none")
        self.ingredients_file_lbl.config(text= "none")

        list_file = open("Meals/meal_list.txt", "a")
        list_file.write(f"{self.meal_name}\n")
        list_file.close()



    def plan_create(self):
        list_file = open("Meals/meal_list.txt", "r")
        meal_list = list_file.readlines()
        list_file.close()

        

        random.shuffle(meal_list)

        self.sun_meal.config(text=meal_list[0].rstrip())
        self.mon_meal.config(text=meal_list[1].rstrip())
        self.tue_meal.config(text=meal_list[2].rstrip())
        self.wed_meal.config(text=meal_list[3].rstrip())
        self.thu_meal.config(text=meal_list[4].rstrip())
        self.fri_meal.config(text=meal_list[5].rstrip())
        self.sat_meal.config(text=meal_list[6].rstrip())

        plan_file = open("Meals/meal_plan.txt","w")
        plan_file.writelines(meal_list[:7])
        plan_file.close()








if __name__ == "__main__":
    root = tk.Tk()
    Main_gui = Main_GUI(root)
    root.mainloop()