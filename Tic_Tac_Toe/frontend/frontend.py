from tkinter import *

class Mybut(Button):
    def __init__(self,tag,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tag = tag
    def print_tag(self):
        return str(self.tag) 
    

class board:

    def __init__(self,base=None):
        self.turn =10
        self.cord = []
        self.on_move_callback = None
        self.play = -1
        
        if base:
            self.root = Toplevel(base)
        else:
            self.root = Tk()
        self.root.geometry("512x512")
        self.root.config(background="lightblue")
        self.root.grid_anchor('center')

        r =1
        c = 1

        self.frame1 = Frame(self.root,height=32,width=512,background='lightblue')
        self.frame2 = Frame(self.root,height=21,width=42)

        self.frame1.pack(pady= 3,padx=5)
        self.frame2.pack(pady=7)

        self.chance_txt = StringVar()
        self.chance_txt.set(f"Player {self.turn%2 + 1} chance : ")

        self.label = Label(self.frame1,text="Welcome",width = 14 , height= 2,fg='black',background='lightblue')
        self.label2 = Label(self.frame1,text="Play",width = 14 , height= 2,fg='black',background='lightblue')
        self.label3 = Label(self.frame1,textvariable=self.chance_txt,width = 14 , height= 2,fg='black',background='lightblue')
        self.label.grid(row=0,column=0)
        self.label2.grid(row=1,column=0)
        self.label3.grid(row=2,column=0)
        #label.grid(row=0,column=2)


        self.b1 = Mybut(tag = "1",master=self.frame2,text="1",width=14,height=7)
        self.b2 = Mybut(tag = "2",master=self.frame2,text="2",width=14,height=7)
        self.b3 = Mybut(tag = "3",master=self.frame2,text="3",width=14,height=7)
        self.b4 = Mybut(tag = "4",master=self.frame2,text="4",width=14,height=7)
        self.b5 = Mybut(tag = "5",master=self.frame2,text="5",width=14,height=7)
        self.b6 = Mybut(tag = "6",master=self.frame2,text="6",width=14,height=7)
        self.b7 = Mybut(tag = "7",master=self.frame2,text="7",width=14,height=7)
        self.b8 = Mybut(tag = "8",master=self.frame2,text="8",width=14,height=7)
        self.b9 = Mybut(tag = "9",master=self.frame2,text="9",width=14,height=7)
        # 
        self.b1.grid(row=r+0,column=c+0)
        self.b2.grid(row=r+0,column=c+1)
        self.b3.grid(row=r+0,column=c+2)
        self.b4.grid(row=r+1,column=c+0)
        self.b5.grid(row=r+1,column=c+1)
        self.b6.grid(row=r+1,column=c+2)
        self.b7.grid(row=r+2,column=c+0)
        self.b8.grid(row=r+2,column=c+1)
        self.b9.grid(row=r+2,column=c+2)
        #
        self.b1.config(background="yellow",command= lambda btn = self.b1: self.clicke(btn))
        self.b2.config(background="yellow",command= lambda btn = self.b2: self.clicke(btn))
        self.b3.config(background="yellow",command= lambda btn = self.b3: self.clicke(btn))
        self.b4.config(background="yellow",command= lambda btn = self.b4: self.clicke(btn))
        self.b5.config(background="yellow",command= lambda btn = self.b5: self.clicke(btn))
        self.b6.config(background="yellow",command= lambda btn = self.b6: self.clicke(btn))
        self.b7.config(background="yellow",command= lambda btn = self.b7: self.clicke(btn))
        self.b8.config(background="yellow",command= lambda btn = self.b8: self.clicke(btn))
        self.b9.config(background="yellow",command= lambda btn = self.b9: self.clicke(btn))

        self.btns = [self.b1,self.b2,self.b3,self.b4,self.b5,self.b6,self.b7,self.b8,self.b9]
        #
    
    def clicke(self,a):
        if self.turn%2==0:
            current='O'
        else:
            current='X'
        self.turn-=1
        if self.play ==-1:
            self.chance_txt.set(f"Player {self.turn%2 +1} chance : ")
        self.cord.append(a.print_tag())
        a.config(text=current,state=DISABLED,font = ("Arial" , 9 ,'bold'),width=14,height=7)
        if self.on_move_callback:
            if self.play!=-1:
                if self.turn%2 == self.play:
                    self.on_move_callback()
            else:
                self.on_move_callback()

        