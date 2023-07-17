from tkinter import *
windows = Tk()
windows.geometry("500x500")

e = Entry(windows, width=50 , borderwidth=5 )
e.place(x=10 , y=0)

def click(num):
   result = e.get()
   e.delete(0,END)
   e.insert(0 , str(result) + str(num))


b = Button(windows, text='1' , width=12 , command=lambda:click(1))
b1 = Button(windows, text='2' , width=12, command=lambda:click(2))
b2 = Button(windows, text='3' , width=12, command=lambda:click(3))
b3 = Button(windows, text='4' , width=12, command=lambda:click(4))
b4 = Button(windows, text='5' , width=12, command=lambda:click(5))
b5 = Button(windows, text='6' , width=12, command=lambda:click(6))
b6 = Button(windows, text='7' , width=12, command=lambda:click(7))
b7 = Button(windows, text='8' , width=12, command=lambda:click(8))
b8 = Button(windows, text='9' , width=12, command=lambda:click(9))
b9 = Button(windows, text='0' , width=12, command=lambda:click(0))
b.place(x=10 , y=60)
b1.place(x=80 , y=60)
b2.place(x=170 , y=60)
b3.place(x=10 , y=120)
b4.place(x=80 , y=120)
b5.place(x=170 , y=120)
b6.place(x=10 , y=180)
b7.place(x=80 , y=180)
b8.place(x=170 , y=180)
b9.place(x=10 , y=240)
#operator
def add():
   n1=e.get()
   global math
   math = "addition"
   global i
   i=int(n1)
   e.delete(0, END)
bu = Button(windows, text='+' , width=12 , command=add)
bu.place(x=80 , y=240)
def sub():
   n1=e.get()
   global math
   math = "subtraction"
   global i
   i=int(n1)
   e.delete(0, END)
bu = Button(windows, text='-' , width=12 , command=sub)
bu.place(x=170 , y=240)
def mul():
   n1=e.get()
   global math
   math = "multiplication"
   global i
   i=int(n1)
   e.delete(0, END)
bu = Button(windows, text='*' , width=12 , command=mul)
bu.place(x=10 , y=300)
def div():
   n1=e.get()
   global math
   math = "division"
   global i
   i=int(n1)
   e.delete(0, END)
bu = Button(windows, text='/' , width=12 , command=div)
bu.place(x=80 , y=300)
def equal():
   n2=e.get()
   e.delete(0, END)
   if math == "addition":
      e.insert(0,i + int(n2))
   elif(math == "subtraction"):
      e.insert(0,i - int(n2))
   elif (math == "multiplication"):
      e.insert(0, i * int(n2))
   elif (math == "division"):
      e.insert(0, i / int(n2))


bu = Button(windows, text='=' , width=12, command=equal)
bu.place(x=170 , y=300)
def clear():
   e.delete(0, END)
bu = Button(windows, text='clear' , width=12 , command=clear)
bu.place(x=80 , y=360)
mainloop()