import tkinter
import random
from tkinter import *

top = tkinter.Tk()
top.title("Rock Paper Scissors Game")

computer_options={
    "0":"Rock",
    "1":"Paper",
    "2":"Scissor"
}
#Disable all the Buttons after first Match
def button_disable():
    b1.config(state="disabled",fg="white")
    b2.config(state="disabled")
    b3.config(state="disabled")

def rock():
    value = computer_options[str(random.randint(0,2))]

    if value=="Rock":
        result="Match Draw"
    elif value=="Scissor":
        result="You won!!!"
    else:
        result="Computer won"
    res_label.config(text=result)
    l4.config(text="Rock")
    l5.config(text=value)
    button_disable()
def paper():
    value = computer_options[str(random.randint(0,2))]

    if value=="Paper":
        result="Match Draw"
    elif value=="Rock":
        result="You won!!!"
    else:
        result="Computer won"
    res_label.config(text=result)
    l4.config(text="Paper")
    l5.config(text=value)
    button_disable()

def scissor():
    value = computer_options[str(random.randint(0,2))]

    if value=="Scissor":
        result="Match Draw"
    elif value=="Paper":
        result="You won!!!"
    else:
        result="Computer won"
    res_label.config(text=result)
    l4.config(text="Scissor")
    l5.config(text=value)
    button_disable()

# reset the game
def reset():
    b1.config(state="active")
    b2.config(state="active")
    b3.config(state="active")
    l1.config(text="Player")
    l3.config(text="Computer")
    l4.config(text="")
    l5.config(text="")
    res_label.config(text="")

Label(top,text="Rock Paper Scissors", font="normal 18 bold" ,fg="green").pack(pady=20)

# Adding frame
frame = Frame(top)
frame.pack()

l1 = Label(frame,text="Player",bg="white",fg="black", font=10)
l2  = Label(frame,text="                  VS                  ", font="normal 13 bold")
l3  = Label(frame,text="Computer",bg="white",fg="black",font=10)

l1.pack(side=LEFT)
l2.pack(side=LEFT)
l3.pack(side=LEFT)


frame3 = Frame(top)
frame3.pack()
l4 = Label(frame3,text="", font=10)
l5  = Label(frame3,text="", font=10)
l4.pack(side=LEFT,pady=20, padx=115)
l5.pack(side=LEFT,pady=20, padx=115)

# result label
res_label = Label(top, text="",font="italic 20 bold")
res_label.pack()

# Adding next frame
frame1 = Frame(top)
frame1.pack(pady=40)

b1=Button(frame1,text="Rock",bg="orange",fg="white", font="normal 10 bold", command=rock)
b2=Button(frame1,text="Paper",bg="orange",fg="white", font="normal 10 bold", command=paper)
b3=Button(frame1,text="Scissors",bg="orange",fg="white", font="normal 10 bold", command=scissor)
b1.pack(side=LEFT, padx=15)
b2.pack(side=LEFT, padx=15)
b3.pack(padx=15)

# Reset Button
Button(top, text="Reset",command=reset).pack(pady=20)

top.geometry("750x450")

top.mainloop()