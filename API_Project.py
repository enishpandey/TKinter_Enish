import tkinter
from tkinter import *
import requests

def next():
    url =requests.get("https://api.adviceslip.com/advice")
    data = url.json()
    adv = data['slip']['advice']
    text_box.delete('1.0', END)
    text_box.insert(END, adv)

top = tkinter.Tk()
top.title('Quote App')
top['bg']="#F94C14"

text_box = Text(top, height=20, width=40,font=("candara", 10), bd=2)
text_box.pack(pady=15)

btn1 = Button(top,text="Next",bg="lightblue",command=next)
btn1.pack(pady=10)

top.geometry("400x400")
top.mainloop()