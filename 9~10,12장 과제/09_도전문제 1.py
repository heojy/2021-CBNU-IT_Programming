from tkinter import *
import math

window = Tk()
window.title("My Calculator")
display = Entry(window, width = 70, bg="yellow")
display.grid(row=0, column=0, columnspan=6)
button_list = ['7', '8', '9', '/', 'C', "(",
               '4',"5","6","*","log", ")",
               "1","2","3","-","sin", "ㅠ",
               '0',"."," ","+","cos", "="]

def click(key):
    if key == "=":
        result= eval(display.get())
        s= str(result)
        display.insert(END,"="+ s)

    elif key == "C":
        display.delete(0,END)
    elif key == "log":
        display.insert(END, "math.log")
    elif key == "sin":
        display.insert(END, "math.sin(")
    elif key == "cos":
        display.insert(END, "math.cos(")
    elif key == "ㅠ":
        display.insert(END, "math.pi")
    else:
        display.insert(END, key)
        
row_index = 1
col_index = 0
for button_text in button_list:
    Button(window, text = button_text, width = 10, 
           command = lambda t = button_text : click(t)).grid(row=row_index, column=col_index)
    col_index +=1
    if col_index >5:
        row_index += 1
        col_index = 0
        
window.mainloop()