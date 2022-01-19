from tkinter import *

window = Tk()

tryID, trypassword = StringVar(), StringVar()

Label(window, text ="아이디").grid(row=0,column=0)
Label(window, text ="패스워드").grid(row=1,column=0)
e1 = Entry(window, textvariable= tryID).grid(row=0, column=1, columnspan=10)
e2 = Entry(window, textvariable = trypassword).grid(row=1, column=1,columnspan=10)



def log_in():
    if tryID.get() == "정보기술" and trypassword.get() == "프로그래밍":
        print("로그인 되었습니다.")
        
    else:
        print("로그인 실패했습니다.")
        
def Cancle():
    e1.delete(0,END)
    e2.delete(0,END)

Button(window, text="로그인", command = log_in).grid(row=2, column=0)
Button(window, text="취소", command = Cancle).grid(row=2, column=1)

window.mainloop()

