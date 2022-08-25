import tkinter
from tkinter import *

top = tkinter.Tk()
top.title("Calculator App")

# Input a number or operation on btn_click()
# Note: btn_click function updates the input field whenever
# a number is entered. Any button pressed will act as a button click update:
def button_click(item):
    global expression
    expression=expression+str(item)
    input_text.set(expression)

# Clear the input on btn_clear()
def button_clear():
    global expression
    expression=""
    input_text.set("")
# Calculate the input on btn_equal()
def button_equal():
    global expression
    calc = str(eval(expression))
    input_text.set(calc)
    expression=""

expression=""

input_text=StringVar()

frame1 = Frame(top, width=312, height=50)
frame1.pack()

result = Entry(frame1,bg="white", justify=RIGHT,font=('arial', 10, 'bold'), textvariable=input_text)
result.grid(row=0, column=0,pady=5,ipadx=98,ipady=15)
# result.place(width=310,height=90)
# result.pack(pady=10)

frame3 = Frame(top, width=312, height=274)
frame3.pack()

clear = Button(frame3, text="C", fg="black", bg = "lightblue", width=34, height=3, command=lambda: button_clear()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)
divide = Button(frame3, text="/", fg="black", bg = "pink", width=10, height=3, command=lambda: button_click('/')).grid(row=0, column=3, padx=1, pady=1)

seven = Button(frame3, text="7", fg="black", bg = "lightblue", width=10, height=3, command=lambda: button_click(7)).grid(row=1, column=0, padx=1, pady=1)
eight = Button(frame3, text="8", fg="black", bg = "lightblue", width=10, height=3, command=lambda: button_click(8)).grid(row=1, column=1, padx=1, pady=1)
nine = Button(frame3, text="9", fg="black", bg = "lightblue", width=10, height=3, command=lambda: button_click(9)).grid(row=1, column=2, padx=1, pady=1)
multiplication = Button(frame3, text="*", bg = "pink", fg="black", width=10, height=3, command=lambda: button_click('*')).grid(row=1, column=3, padx=1, pady=1)

four = Button(frame3, text="4", fg="black", bg = "lightblue", width=10, height=3, command=lambda: button_click(4)).grid(row=2, column=0, padx=1, pady=1)
five = Button(frame3, text="5", fg="black", bg = "lightblue", width=10, height=3, command=lambda: button_click(5)).grid(row=2, column=1, padx=1, pady=1)
six = Button(frame3, text="6", fg="black", bg = "lightblue", width=10, height=3, command=lambda: button_click(6)).grid(row=2, column=2, padx=1, pady=1)
subtraction = Button(frame3, text="-", bg = "pink", fg="black", width=10, height=3, command=lambda: button_click('-')).grid(row=2, column=3, padx=1, pady=1)

one = Button(frame3, text="1", fg="black", bg = "lightblue", width=10, height=3, command=lambda: button_click(1)).grid(row=3, column=0, padx=1, pady=1)
two = Button(frame3, text="2", fg="black", bg = "lightblue", width=10, height=3, command=lambda: button_click(2)).grid(row=3, column=1, padx=1, pady=1)
three = Button(frame3, text="3", fg="black", bg = "lightblue", width=10, height=3, command=lambda: button_click(3)).grid(row=3, column=2, padx=1, pady=1)
addition = Button(frame3, text="+", fg="black", bg = "pink", width=10, height=3, command=lambda: button_click('+')).grid(row=3, column=3, padx=1, pady=1)

zero = Button(frame3, text="0", fg="black", bg = "lightblue", width=22, height=3, command=lambda: button_click(0)).grid(row=4, column=0,columnspan=2, padx=1, pady=1)
fullstop = Button(frame3, text=".", fg="black", bg = "pink", width=10, height=3, command=lambda: button_click(".")).grid(row=4, column=2, padx=1, pady=1)
equalto = Button(frame3, text="=", fg="black", bg = "pink", width=10, height=3, command=lambda: button_equal()).grid(row=4, column=3, padx=1, pady=1)



top.geometry("340x360")
top.mainloop()