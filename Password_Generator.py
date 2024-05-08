from tkinter import*
import random
import string
root=Tk()
root.title("PASSWORD GENERATOR")

def password_generator():
    try:
        len=int(e.get())
        pass_char=string.digits+string.ascii_letters+string.punctuation
        password=''.join(random.choice(pass_char) for i in range(len))
        Label_2.config(text="Generated Password:"+password)
        if len<=0:
            raise ValueError
    except ValueError:
        Label_2.config(text="invalid entry")   

Label_1=Label(root,text="Enter length of the password:")
Label_1.pack()
e=Entry(root)
e.pack()

Button_1=Button(root,text="Generate Password",command=password_generator)
Button_1.pack()

Label_2=Label(root,text="")
Label_2.pack()

root.mainloop()