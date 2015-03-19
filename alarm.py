# -*- coding: utf-8 -*-
from Tkinter import *
import datetime
import pygame
root = Tk()

def time(event):
    lbl["text"] = datetime.datetime.now().time().strftime("%H:%M:%S") # https://docs.python.org/2/library/datetime.html#strftime-strptime-behavior

def alarm_sound(event):
    pygame.init()
    pygame.mixer.music.load("mlg.mp3")
    pygame.mixer.music.play(-1, 0.0)

    
lbl = Label(root, text = " ", width=30,height=2, bg = "black", fg = "white")
lbl.pack()
btn = Button(root,                  #родительское окно
             text="Click me",       #надпись на кнопке
             width=30,height=5,     #ширина и высота
             bg="white",fg="black") #цвет фона и надписи
btn.bind("<Button-1>", time)       #при нажатии ЛКМ на кнопку вызывается функция Time
btn.pack()                          #расположить кнопку на главном окне
btn1 = Button(root,                 
             text="Click for MLG",       
             width=30,height=5,    
             bg="white",fg="black") 
btn1.bind("<Button-1>", alarm_sound)       
btn1.pack()  

root.mainloop()