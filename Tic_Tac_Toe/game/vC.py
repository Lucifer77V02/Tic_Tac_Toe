from frontend.frontend import board
import random
from tkinter import *

class Player:
    def __init__(self,pat):
        self.chances = []
        self.pat = pat
    def push(self,co):
        self.chances.append(co)
        self.chances.sort()

class bot(Player):
    def __init__(self,pat):
        super().__init__(pat)
        self.validchance = []

    def valid(self,btns):
        self.validchance = []
        for btn in btns:
            if btn['state'] != DISABLED:
                self.validchance.append(btn)

class Game:
    guide_b = [[1,2,3],[4,5,6],[7,8,9]]
    def __init__(self,base):
        self.board = board(base)
        self.player1 = Player(1)
        self.player2 = bot(-1)
        self.board.on_move_callback = self.Loop
        self.board.play = 1
    
    def cord_ch(self,num):
        match(num):
            # 8 1 6
            # 3 5 7
            # 4 9 2
            case 1: return 8
            case 2: return 3
            case 3: return 4
            case 4: return 1
            case 5: return 5
            case 6: return 9
            case 7: return 6
            case 8: return 7
            case 9: return 2

    def win_check(self,i):
        if i==1:
            if sum(self.player1.chances)>=15:
                p1 = 0
                while p1<len(self.player1.chances)-1 :
                    p2 = len(self.player1.chances)-1
                    while(p1<p2):
                        k = (15 - (self.player1.chances[p1]+self.player1.chances[p2]))
                        if k in self.player1.chances:
                            if k != self.player1.chances[p1] and k!=self.player1.chances[p2]:
                                return True
                        p2-=1
                    p1+=1
                return False

            else:
                return False

        else:
            if sum(self.player2.chances)>=15:
                p1 = 0
                while p1<len(self.player2.chances)-1 :
                    p2 = len(self.player2.chances)-1
                    while(p1<p2):
                        k = (15 - (self.player2.chances[p1]+self.player2.chances[p2]))
                        if k in self.player2.chances:
                            if k != self.player2.chances[p1] and k!=self.player2.chances[p2]:
                                return True
                        
                        p2-=1
                    p1+=1
                return False
            else:
                return False

    def Loop(self):
        c = self.win_check(self.board.turn%2)
        if c:
            self.board.chance_txt.set(f"Player {2} Winnss!")
            for b in self.board.btns:
                b.config(state=DISABLED)
            self.board.root.update()

        checking = [str(x) for x in range(1,10)]    
        numm = int(self.board.cord[-1])
        corr = self.cord_ch(numm)
        
        self.player1.push(corr)
        c1 = self.win_check(self.board.turn%2)
        if self.board.turn ==1 or c1:  
            temp = self.board.cord.copy()
            temp.sort()
            if c1:
                self.board.chance_txt.set(f"Player {1} Winnss!")
                for b in self.board.btns:
                    b.config(state=DISABLED)
                self.board.root.update()
            elif temp == checking and c1 is False:
                self.board.chance_txt.set("Its a Tie")
                self.board.root.update()
                
        if self.board.turn != 1 and c1 is False:
            self.player2.valid(self.board.btns)
            p2t = random.choice(self.player2.validchance)
            p2t.invoke()
            numm = int(self.board.cord[-1])
            corr = self.cord_ch(numm)
            self.player2.push(corr)
            c = self.win_check(self.board.turn%2)
            if self.board.turn == 1 or c: 
                temp = self.board.cord.copy()
                temp.sort() 
                if c:
                    self.board.chance_txt.set(f"Computer Winnss!")
                    for b in self.board.btns:
                        b.config(state=DISABLED)
                    self.board.root.update()
                elif temp == checking and c is False:
                    self.board.chance_txt.set("Its a Tie")
                    self.board.root.update()
if __name__ =='__main__':
    game = Game()