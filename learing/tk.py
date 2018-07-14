#!/usr/bin/env python3
from tkinter import *
import sys

root = Tk()
root.geometry('300x130')
e1 = Button(root,text='First',fg='red')
e2 = Button(root,text='Second',fg='blue')
e1.grid(row=0, column=0,padx =4,pady =3)
e2.grid(row=1, column=0)

# l1 = Label(root,text='test',height =4,width =23,fg ='yellow')
# l1.grid(row =1,column = 0)

root.mainloop()
