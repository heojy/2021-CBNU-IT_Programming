from tkinter import *
import random

window= Tk()
w= Canvas(window, width =1000, height = 800)
w.pack()

for i in range(1,10):
    color = ["red","orange","yellow","green","blue","violet"]
    fill_color = random.choice(color)
    w.create_rectangle(random.randint(0,900), random.randint(0,700), 
                       random.randint(100,1000), random.randint(100,800), fill = fill_color)
    
window.mainloop()
