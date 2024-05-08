from tkinter import *
root=Tk()
root.title("CALCULATOR")
e=Entry(root,width=45,borderwidth=5)
e.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

def Button_click(num):
    new=e.get()
    e.delete(0,END)
    e.insert(0,str(new)+str(num))

def Button_clear():
    e.delete(0,END)

def Button_add():
    num1=e.get()
    global f_num
    global Choice
    Choice="Addition"
    f_num=int(num1)
    e.delete(0,END)

def Button_sub():
    num1=e.get()
    global f_num
    global Choice
    Choice="Subtraction"
    f_num=int(num1)
    e.delete(0,END)

def Button_mul():
    num1=e.get()
    global f_num
    global Choice
    Choice="Multiplication"
    f_num=int(num1)
    e.delete(0,END)

def Button_div():
    num1=e.get()
    global f_num
    global Choice
    Choice="Division"
    f_num=int(num1)
    e.delete(0,END)

def Button_equal():
    num2=int(e.get())
    e.delete(0,END)
    if Choice=="Addition":
        e.insert(0,f_num+num2)
    if Choice=="Subtraction":
        e.insert(0,f_num-num2)
    if Choice=="Multiplication":
        e.insert(0,f_num*num2)
    if Choice=="Division":
        e.insert(0,f_num/num2)
    
Button_1=Button(root,text="1",padx=40,pady=20,command=lambda:Button_click(1))
Button_2=Button(root,text="2",padx=40,pady=20,command=lambda:Button_click(2))
Button_3=Button(root,text="3",padx=40,pady=20,command=lambda:Button_click(3))
Button_4=Button(root,text="4",padx=40,pady=20,command=lambda:Button_click(4))
Button_5=Button(root,text="5",padx=40,pady=20,command=lambda:Button_click(5))
Button_6=Button(root,text="6",padx=40,pady=20,command=lambda:Button_click(6))
Button_7=Button(root,text="7",padx=40,pady=20,command=lambda:Button_click(7))
Button_8=Button(root,text="8",padx=40,pady=20,command=lambda:Button_click(8))
Button_9=Button(root,text="9",padx=40,pady=20,command=lambda:Button_click(9))
Button_0=Button(root,text="0",padx=40,pady=20,command=lambda:Button_click(0))
Button_add=Button(root,text="+",padx=38,pady=20,command=Button_add)
Button_sub=Button(root,text="-",padx=40,pady=20,command=Button_sub)
Button_mul=Button(root,text="x",padx=39,pady=20,command=Button_mul)
Button_div=Button(root,text="/",padx=40,pady=20,command=Button_div)
Button_equal=Button(root,text="=",padx=38,pady=20,command=Button_equal)
Button_clear=Button(root,text="AC",padx=36,pady=20,command=Button_clear)

Button_7.grid(row=1,column=0)
Button_8.grid(row=1,column=1)
Button_9.grid(row=1,column=2)
Button_add.grid(row=1,column=3)

Button_4.grid(row=2,column=0)
Button_5.grid(row=2,column=1)
Button_6.grid(row=2,column=2)
Button_sub.grid(row=2,column=3)

Button_1.grid(row=3,column=0)
Button_2.grid(row=3,column=1)
Button_3.grid(row=3,column=2)
Button_mul.grid(row=3,column=3)

Button_0.grid(row=4,column=0)
Button_div.grid(row=4,column=1)
Button_clear.grid(row=4,column=2)
Button_equal.grid(row=4,column=3)

root.mainloop()