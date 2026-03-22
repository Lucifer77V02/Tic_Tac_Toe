from tkinter import *
from game.v1 import Game as gv1
from game.vC import Game as gvC

root =Tk()

root.geometry('720x512')
root.title('Menu')
root.config(padx =4,pady=4,background="#fffffe")


def start_1():
    games = gv1(root)
def start_C():
    game = gvC(root)

def qq():
    root.destroy()

frame = Frame(root,bg="#f2f7f5",height=400,width=480,highlightthickness=2,relief='raised',highlightbackground="#00214d")
frame.pack()
frame.place(relx=0.16,rely=0.12)
l = Label(frame,text= 'Main Menu',fg ='black',justify='center',font=('Arial',16),relief='solid')
b1 = Button(frame,text="1 V 1",fg="#00214d",bg="#00ebc7",justify='center',font=('Times',15))
b2 = Button(frame,text="1 V C",fg="#00214d",bg="#00ebc7",justify='center',font=('Times',15))
b3 = Button(frame,text="Quit",justify='center',bg="#ff6e6c",fg="#1f1235",command=qq,font=('Times',15))

#b1.grid(row = 2,column=2,padx= 5,pady=5),
l.place(relx=0.125,rely=0.1,height=52,width=355)
b1.place(relx=0.125,rely=0.35,height=49,width=355)
b2.place(relx=0.125,rely=0.525,height=49,width=355)
b3.place(relx=0.125,rely=0.7,height=49,width=355)


b1.config(command= start_1)

b2.config(command= start_C)


root.mainloop()
