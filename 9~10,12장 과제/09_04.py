from tkinter import *

window = Tk()
window.geometry("400x140")
Label(window, text ="이름:").grid(row=0, column=0)
Label(window, text ="주소:").grid(row=1, column=0)
Label(window, text ="도:").grid(row=2, column=0)
Label(window, text ="우편번호:").grid(row=3, column=0)
Label(window, text ="국가:").grid(row=4, column=0)

e1 = Entry(window, width = 50)
e2 = Entry(window, width = 50)
e3 = Entry(window, width = 50)
e4 = Entry(window, width = 50)
e5 = Entry(window, width = 50)

e1.grid(row=0, column=1, columnspan=20)
e2.grid(row=1, column=1, columnspan=20)
e3.grid(row=2, column=1, columnspan=20)
e4.grid(row=3, column=1, columnspan=20)
e5.grid(row=4, column=1, columnspan=20)

def clear():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)

Button(window, text="clear", command = clear).grid(row=5, column=10, columnspan=12)
Button(window, text="Submit").grid(row=5, column=16, columnspan=6)


    
window.mainloop()