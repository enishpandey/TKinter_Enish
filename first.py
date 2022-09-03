import tkinter
from tkinter import *
from tkinter import messagebox

top = tkinter.Tk()
top.title("Enish App")

# logo = PhotoImage(file="image/palastate.png")
# spin = Spinbox(top,from_=0, to=100, width=5).pack()
# Label
B = Label(top, text="Enter a link here:").place(x=40,y=100)
link_entry= Entry(top,width=65).place(x=140,y=102)


Lb1 = Listbox(top)
Lb1.insert(1, "Python")
Lb1.insert(2, "Perl")
Lb1.insert(3, "C")
Lb1.insert(4, "PHP")
Lb1.insert(5, "JSP")
Lb1.insert(6, "Ruby")
Lb1.insert(1, "Python")
Lb1.insert(2, "Perl")
Lb1.insert(3, "C")
Lb1.insert(4, "PHP")
Lb1.insert(5, "JSP")
Lb1.insert(6, "Ruby")
Lb1.place(x=40 ,y=140 )

Lb2 = Listbox(top)
Lb2.insert(1, "find")
Lb2.insert(2, "find_all")
Lb2.insert(3, "find_next")
Lb2.insert(4, "find_next_sibling")
Lb2.insert(5, "JSP")
Lb2.insert(6, "Ruby")
Lb2.insert(1, "Python")
Lb2.insert(2, "Perl")
Lb2.insert(3, "C")
Lb2.insert(4, "PHP")
Lb2.insert(5, "JSP")
Lb2.insert(6, "Ruby")
Lb2.place(x=180 ,y=140 )


def clicked():
    messagebox.showinfo('Message','Welcome to our youtube channel')

button = Button(top,text="Generate", bg="green", fg="white", command=clicked).place(x=220, y=320)

out = Label(top,text="Output").place(x=40,y=380)
Output = Text(top, height = 10,
              width = 60,
              bg = "white").place(x=40,y=400)

download = Button(top,text="Convert into CSV", bg="green", fg="white").place(x=420, y=570)

top.geometry("900x600")
top.mainloop()