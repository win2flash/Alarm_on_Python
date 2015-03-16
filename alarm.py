# -*- coding: utf-8 -*-
from Tkinter import *
import datetime
root = Tk()

def Time(event):
    lbl["text"] = datetime.datetime.now().time().strftime("%H:%M:%S") # https://docs.python.org/2/library/datetime.html#strftime-strptime-behavior
    
lbl = Label(root, text = " ", width=30,height=2, bg = "black", fg = "white")
lbl.pack()
btn = Button(root,                  #родительское окно
             text="Click me",       #надпись на кнопке
             width=30,height=5,     #ширина и высота
             bg="white",fg="black") #цвет фона и надписи
btn.bind("<Button-1>", Time)       #при нажатии ЛКМ на кнопку вызывается функция Time
btn.pack()                          #расположить кнопку на главном окне
root.mainloop()