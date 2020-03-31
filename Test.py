import tkinter as tk
from tkinter import filedialog as fd 

def callback():
    name = fd.askopenfilename()
    print(name) 
    print(name.rfind('/'))
    file_name = name[name.rfind('/')+1:len(name)]
    print(file_name)
    
errmsg = 'Error!'
tk.Button(text='Click to Open File', 
       command=callback).pack(fill=tk.X)
tk.mainloop()