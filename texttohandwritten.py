import pywhatkit as kt
import cv2
from tkinter import *

window = Tk()
window.title("Text to Handwritten")
window.geometry('500x400')
window.configure(bg='black')
Label(window, text="Text to Handwritten\nConverter", font="algerian 22 bold", bg='OrangeRed1').pack()
Msg = StringVar()
Label(window, text="Enter Text", font='arial 15 bold', fg='white', bg='black').place(x=50, y=100)
entry = Entry(window, textvariable=Msg, font='arial 16')
entry.place(x=50, y=140, width=420, height=35)


def text():
    kt.text_to_handwriting(entry.get(), save_to='your_text.png')
    img = cv2.imread('your_text.png')
    cv2.imshow('Text To handwriting', img)


Button(window, text='Convert', font='arial 12 bold', width='10', bg='lightgreen', command=text).place(x=200, y=250)
Button(window, text='Exit', font='arial 12 bold', width='10', bg='red', command=window.destroy).place(x=200, y=300)
window.mainloop()
