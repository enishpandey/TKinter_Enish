import time
import tkinter
from tkinter import *
import math
from tkinter import messagebox
from playsound import playsound


top=tkinter.Tk()
top.title("Timer App")
top['bg']="#F8DD33"


hour = StringVar()
minute = StringVar()
second=StringVar()

hour.set("00")
minute.set("00")
second.set("00")

# Command performed here
def submit():
    try:
        temp = int(hour.get())*3600+int(minute.get())*60+int(second.get())

    except:
        print("please input correct time")

    while temp>-1:
        mins, secs = divmod(temp, 60)

        hours=0
        if mins>60:
            hours, mins = divmod(mins, 60)

        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))

        top.update()
        time.sleep(1)

        if temp==0:

            messagebox.showinfo("Time Countdown", "Time's Up")
            # playsound('Sound/inspire.mp3')

        temp = temp-1


hour_entry = Entry(top, width=4,bg="white",fg="#900C3F",font=("Arial",15,""), textvariable=hour)
hour_entry.place(x=80,y=20)

minute_entry = Entry(top, width=4,bg="white",fg="#900C3F",font=("Arial",15,""),textvariable=minute)
minute_entry.place(x=140,y=20)

second_entry = Entry(top, width=4,bg="white",fg="#900C3F",font=("Arial",15,""),textvariable=second)
second_entry.place(x=200,y=20)

button = Button(top, text="Set Time Countdown", command=submit)
button.place(x=100, y=90)

top.geometry("300x250")
top.mainloop()