import pygame
import time
from threading import *
import ExtraWidgits
from random import randint
import StartProcess
import SUDOKU

RunClock=True

class Sudoku():
    def __init__(self,N,speed):
       self.n=N
       self.speed=speed
       pygame.init()
       self.SIDE=554;self.block=60
       self.win=pygame.display.set_mode((self.SIDE+450,self.SIDE))
       pygame.display.set_caption("SUDOKU")
       self.WHITE=(250,250,250);self.BLACK=(135,206,250)
       self.font=pygame.font.Font('freesansbold.ttf',45)
       #Solved SUDOKU
       self.solve_set=[
           [[9,5,1,7,6,8,3,2,4],[6,4,8,9,2,3,5,7,1],[3,2,7,1,4,5,8,9,6],[2,6,4,5,8,7,9,1,3],
            [7,9,5,3,1,4,2,6,8],[1,8,3,6,9,2,7,4,5],[8,1,6,2,5,9,4,3,7],[4,7,2,8,3,1,6,5,9],[5,3,9,4,7,6,1,8,2]],
           [[1,2,3,4,5,6,7,8,9],[4,5,6,7,8,9,1,2,3],[7,8,9,1,2,3,4,5,6],[2,1,4,3,6,5,8,9,7],
            [3,6,5,8,9,7,2,1,4],[8,9,7,2,1,4,3,6,5],[5,3,1,6,4,2,9,7,8],[6,4,2,9,7,8,5,3,1],[9,7,8,5,3,1,6,4,2]],
           [[1,2,3,7,8,9,6,5,4],[9,6,5,4,1,3,8,7,2],[4,8,7,2,6,5,9,3,1],[2,3,8,6,7,4,1,9,5],
            [7,9,4,1,5,2,3,6,8],[6,5,1,9,3,8,4,2,7],[3,7,9,5,4,1,2,8,6],[5,1,2,8,9,6,7,4,3],[8,4,6,3,2,7,5,1,9]],
           [[1,9,4,2,7,6,3,5,8],[2,6,8,3,9,5,7,1,4],[3,5,7,8,4,1,9,2,6],[7,4,2,6,1,9,5,8,3],
            [8,1,6,7,5,3,4,9,2],[9,3,5,4,2,8,1,6,7],[6,8,9,1,3,4,2,7,5],[5,7,3,9,6,2,8,4,1],[4,2,1,5,8,7,6,3,9]]]
       
       self.solved=self.solve_set[randint(0,len(self.solve_set)-1)]
       self.shift=7
       self.initial=[[0]*self.n for i in range(self.n)]
       self.to_solve=[[0]*self.n for i in range(self.n)]
       self.text_Pading_x=18;self.text_Pading_y=12
       self.running = True
       self.operations=0
       self.WaitForEndProcess=True
       self.StartVisualization()
       
    def StartVisualization(self):
        
        self.board()
        self.initial_state(randint(40,60))

        AddClock =ExtraWidgits.Clock(self.win, 800, 100, 25)
        AddClock.start()
        AddMainMenuButton =ExtraWidgits.MainMenuButton(self.win,650,300)
        AddMainMenuButton.start()
        AddExitText = ExtraWidgits.ExitText(self.win,675,250)
        AddExitText.start()
        StartSolving=Thread(target=self.solve)
        StartSolving.start()
        #self.solve()
        self.CheckActions()


    def CheckActions(self):
        self.X = 650
        self.Y = 300
        while (self.running):
            try:
                self.pos = pygame.mouse.get_pos()
            except:
                pass
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.running=False
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                        pygame.quit()

                if self.pos[0] > self.X and self.pos[0] < self.X + 240 and self.pos[1] > self.Y and self.pos[
                    1] < self.Y + 35:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        try:
                            self.running=False
                            pygame.quit()
                            while(self.WaitForEndProcess):
                                pass
                            Process = StartProcess.START()
                            Process.start()
                            SUDOKU.RunClock=True
                        except:
                            pass

    def print_Board(self):
        for i in range(self.n):
            if not self.running:
                break
            for j in range(self.n):
                if not self.running:
                    break
                if(self.to_solve[i][j]!=0):
                    self.print_Number(j,i,str(self.to_solve[i][j]),(0,0,0))
        
    def print_Number(self,x,y,number,color,bgcolor=()):
        x_shift=(x//3)*self.shift
        y_shift=(y//3)*self.shift
        if(len(bgcolor)==0):
            if((x//3+y//3)%2==0):
                bgcolor=self.BLACK
            else:
                bgcolor=self.WHITE
        try:
            pygame.draw.rect(self.win,bgcolor,(4+x_shift+x*self.block,4+y_shift+y*self.block,self.block-6,self.block-6))
            self.win.blit(self.font.render(number, True,color),(self.text_Pading_x+x_shift+x*self.block,self.text_Pading_y+y_shift+y*self.block))
        except:
            pass
    def initial_state(self,NoOfElements):
        AlreadyPresent={}
        while(len(AlreadyPresent)<NoOfElements):
            if not self.running:
                break
            row=randint(0,8)
            col=randint(0,8)
            if((row,col) not in AlreadyPresent):
                AlreadyPresent[(row,col)]=1
                self.to_solve[row][col]=self.solved[row][col]
                self.initial[row][col]=self.solved[row][col]
        self.print_Board()
        
    def board(self):
        x_shift=0;y_shift=0
        for i in range(self.n):
            if not self.running:
                break
            y_shift=0
            if(i%3==0 and i!=0):
                x_shift+=self.shift
            for j in range(self.n):
                if not self.running:
                    break
                if(j%3==0 and j!=0):
                    y_shift+=self.shift
                if((i//3+j//3)%2==1):
                    color=self.WHITE
                else:
                    color=self.BLACK
                pygame.draw.rect(self.win,color,(x_shift+i*self.block,y_shift+j*self.block,self.block,self.block))
        x_shift=0;y_shift=0
        for i in range(self.n):
            if not self.running:
                break
            if(i%3==0 and i!=0):
                x_shift+=self.shift
                y_shift+=self.shift
                continue
            pygame.draw.line(self.win,(0,0,0),(0,x_shift+i*self.block),(self.SIDE,x_shift+i*self.block),2)
            pygame.draw.line(self.win,(0,0,0),(y_shift+i*self.block,0),(y_shift+i*self.block,self.SIDE),2)
            

    def chk(self,x,y,val):
        boo=True
        for i in range(9):
            if not self.running:
                    break
            if(self.to_solve[i][y]==val):
                boo=False
                self.print_Number(y,i,str(self.to_solve[i][y]),(0,0,0),(255,100,100))
            if(self.to_solve[x][i]==val):
                boo=False
                self.print_Number(i,x,str(self.to_solve[x][i]),(0,0,0),(255,100,100))
        x1=3*(x//3);y1=3*(y//3)
        for i in range(3):
            if not self.running:
                break
            for j in range(3):
                if not self.running:
                    break
                if(self.to_solve[x1+i][y1+j]==val):
                    boo=False
                    self.print_Number(y1+j,x1+i,str(self.to_solve[x1+i][y1+j]),(0,0,0),(255,100,100))
                    break
        time.sleep(1/self.speed)
        for i in range(9):
            if not self.running:
                break
            if(self.to_solve[i][y]==val):
                if(self.initial[i][y]==val):
                    self.print_Number(y,i,str(self.to_solve[i][y]),(0,0,0))
                else:
                    self.print_Number(y,i,str(self.to_solve[i][y]),(255,0,0))
            if(self.to_solve[x][i]==val):
                if(self.initial[x][i]==val):
                    self.print_Number(i,x,str(self.to_solve[x][i]),(0,0,0))
                else:
                    self.print_Number(i,x,str(self.to_solve[x][i]),(255,0,0))
        x1=3*(x//3);y1=3*(y//3)
        for i in range(3):
            if not self.running:
                break
            for j in range(3):
                if not self.running:
                    break
                if(self.to_solve[x1+i][y1+j]==val):
                    if(self.initial[x1+i][y1+j]==val):
                        self.print_Number(y1+j,x1+i,str(self.to_solve[x1+i][y1+j]),(0,0,0))
                    else:
                        self.print_Number(y1+j,x1+i,str(self.to_solve[x1+i][y1+j]),(255,0,0))
                    break
        return boo
    def solve(self):
        chk=1
        if(not self.running):
            return 0
        for i in range(9):
            if not self.running:
                chk=0
                break
            for j in range(9):
                self.operations+=1
                if not self.running:
                    chk=0
                    break
                if(self.to_solve[i][j]==0):
                    for k in range(1,10):
                        if not self.running:
                            chk=0
                            break
                        self.print_Number(j,i,str(k),(255,0,0),(0,255,0))
                        if(self.chk(i,j,k)):
                            self.to_solve[i][j]=k
                            self.print_Number(j,i,str(k),(255,0,0))
                            if not self.running:
                                chk=0
                                break
                            if(not self.solve()):
                                if not self.running:
                                    chk=0
                                    break
                                self.print_Number(j,i,str("  "),(255,0,0))
                                self.to_solve[i][j]=0
                            else:
                                if self.running:
                                    ExtraWidgits.OperationsDone(self.operations,self.win,650,400,"SUDOKU Solved.")
                                SUDOKU.RunClock=False
                                self.WaitForEndProcess=False
                                return 1
                        else:
                            if(not self.running):
                                chk=0
                                break
                            self.print_Number(j,i,str("  "),(255,0,0))
                if(not self.running):
                    break           
                if(self.to_solve[i][j]==0):
                    return False
            if(not self.running):
                break
        self.WaitForEndProcess=False
        return True
