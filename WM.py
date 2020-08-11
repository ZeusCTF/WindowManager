import tkinter
from tkinter import *


def user_input():
    user_input = tkinter.Tk()
    txt=Entry(user_input, text="testing", bd=5)
    txt.place(x=40, y=50)
    mainloop()

def background():
    window = tkinter.Tk()
    window.attributes("-fullscreen", False)
    mainloop()
    user_input()
background()




