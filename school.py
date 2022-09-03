import tkinter
from tkinter import *
import random

top = tkinter.Tk()
top.title("Quiz App")
top['background']="white"

questions=[
    "If you could live anywhere, where would it be?",
    "What did you want to be when you were small?",
    "What was the last movie you went to? What did you think?",
    "What motivates you to work hard?",
    "What makes you laugh the most?",
    "What is your favorite book to read?",
    "What is your child's proudest accomplishment?",
    "What is your biggest complaint about your job?",
    "What is your favorite thing about your career?",
    "What really makes you angry?",
]


indexes=[]
def gen():
    global indexes
    while (len(indexes)<5):
        x=random.randint(0, 9)
        if x in indexes:
            continue
        else:
            indexes.append(x)
    print(indexes)





def quiz_questions():
    global question,a1,a2,a3,a4
    question = Label(top,
                      text=questions[indexes[0]],
                      font=("normal", 10, "bold"),bg="white",
                      wraplength=400,fg="red"
                      )
    question.pack(anchor=W)
    question1 = Label(top,
                      text=questions[indexes[1]],
                      font=("normal", 10, "bold"),bg="white",
                      wraplength=400,fg="red"
                      )
    question1.pack(anchor=W)
    question2 = Label(top,
                      text=questions[indexes[2]],
                      font=("normal", 10, "bold"),bg="white",
                      wraplength=400,fg="red"
                      )
    question2.pack(anchor=W)
    question3 = Label(top,
                      text=questions[indexes[3]],
                      font=("normal", 10, "bold"),bg="white",
                      wraplength=400,fg="red"
                      )
    question3.pack(anchor=W)
    question4 = Label(top,
                      text=questions[indexes[4]],
                      font=("normal", 10, "bold"),bg="white",
                      wraplength=400,fg="red"
                      )
    question4.pack(anchor=W)

    


    # global radiovar
    # radiovar = IntVar()
    # radiovar.set(0)
    # print(radiovar)
    #
    # a1=Radiobutton(top, text=answers[indexes[0]][0],value=1,variable=radiovar,bg="white",wraplength=400)
    # a1.pack(anchor=W)
    # a2=Radiobutton(top, text=answers[indexes[0]][1],value=2,variable=radiovar,bg="white",wraplength=400)
    # a2.pack(anchor=W)
    # a3=Radiobutton(top, text=answers[indexes[0]][2],value=3,variable=radiovar,bg="white",wraplength=400)
    # a3.pack(anchor=W)
    # a4=Radiobutton(top, text=answers[indexes[0]][3],value=4,variable=radiovar,bg="white",wraplength=400,)
    # a4.pack(anchor=W)





def start_clicked():
    start.destroy()
    gen()
    quiz_questions()

# PhotoImage(file="image/quiz.jpg")
start = Button(top,text="Generate Question", font=("sans",10,"bold"), bg="pink", command=start_clicked)
start.pack(pady=50)




top.geometry("400x300")
top.mainloop()