import pygame
import time
from threading import *
import ExtraWidgits
import ExtraWidgits_for_Pathfinders
import StartProcess
import Rat_In_The_Maze
RunClock=True

class Rat_in_Maze:
    def __init__(self, v, speed):
        pygame.init()
        pygame.display.set_caption("Rat In The Maze")
        self.operations=0
        self.WaitForEndProcess=False
        self.n = v
        self.SIDE = 600
        self.block = self.SIDE // self.n
        self.win = pygame.display.set_mode((self.SIDE+450, self.SIDE))
        self.speed=speed
        self.R_SIDE = (3 * self.block) // 4
        self.RAT = pygame.transform.scale(pygame.image.load('Images/Rat.jpg'), (self.R_SIDE, self.R_SIDE))
        self.HOME = pygame.transform.scale(pygame.image.load('Images/Home.png'), (self.block,self.block))
        self.WHITE = (255, 255, 255);self.BLACK = (0, 0, 0)
        self.rat_pos=[[0,0]]
        self.IMG_Pading = (self.block - self.R_SIDE) // 2
        self.maze=[[0]*self.n for i in range(self.n)]
        self.visited=[[0]*self.n for i in range(self.n)]
        self.RIGHT_MOVE=[1,0,-1,0];self.DOWN_MOVE=[0,1,0,-1]
        self.make_maze=True
        self.solving=False
        self.running = True
        self.StartVisualization()
        
    def StartVisualization(self):
        self.print_maze()
        pygame.font.init()
        font = pygame.font.SysFont('Comic Sans MS', 23)
        self.win.blit(font.render("Click on cells to create wall.", False, (255, 255, 255)), (670,50))
        self.win.blit(font.render("Press Space to START", False, (255, 255, 255)),(700,80))
        
        AddMainMenuButton = ExtraWidgits_for_Pathfinders.MainMenuButton(self.win,700,300)
        AddMainMenuButton.start()

        AddExitText = ExtraWidgits.ExitText(self.win,725,250)
        AddExitText.start()
        self.CheckActions()
    
    def CheckActions(self):
        self.X = 700
        self.Y = 300
        SOLVE=Thread(target=self.solve)
        while (self.running):
            try:
                self.pos = pygame.mouse.get_pos()
            except:
                pass
            if(not self.running):
                break
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.running=False
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                        pygame.quit()
                    if event.key==pygame.K_RETURN and not Rat_In_The_Maze.RunClock:
                        self.operations=0
                        self.win.fill((0,0,0))
                        self.solving=False
                        self.make_maze=True
                        self.WaitForEndProcess=True
                        Rat_In_The_Maze.RunClock=True
                        self.operation=0
                        self.rat_pos=[[0,0]]
                        self.visited=[[0]*self.n for i in range(self.n)]
                        self.StartVisualization()
                if(not self.solving):
                    if(not self.running):
                        break
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if(0<=self.pos[0]<=600 and 0<=self.pos[1]<=600) and self.make_maze:
                            self.make_Wall(self.pos[0],self.pos[1])
                    
                    if event.type == pygame.KEYDOWN:
                        if(not self.running):
                            break
                        if event.key == pygame.K_SPACE and not self.solving:
                            self.solving=True
                            self.WaitForEndProcess=True
                            self.make_maze=False
                            AddClock =ExtraWidgits.Clock(self.win, 850, 180, 25)
                            AddClock.start()
                            SOLVE=Thread(target=self.solve)
                            SOLVE.start()
                            pass
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
                            Rat_In_The_Maze.RunClock=True
                            
                        except:
                            pass
    def make_Wall(self,x,y):
            row=x//self.block;col=y//self.block
            if(row==0 and col==0) or (row==self.n-1 and col==self.n-1):
                return
            self.maze[row][col]^=1
            self.print_maze()

    def print_maze(self):
        for y in range(self.n):
            if(not self.running):
                break
            for x in range(self.n):
                if(not self.running):
                    break
                color=self.WHITE
                if(self.maze[x][y]==1):
                    color=self.BLACK
                pygame.draw.rect(self.win, color, (x* self.block, y * self.block, self.block, self.block))
        try:        
            self.win.blit(self.HOME, ((self.n-1) * self.block,(self.n-1) * self.block))
        except:
            pass

        for i in range(self.n):
            if(not self.running):
                break
        
            pygame.draw.line(self.win,(150,150,150),(0,i*self.block),(self.n*self.block,i*self.block),2)
            pygame.draw.line(self.win,(150,150,150),(i*self.block,0),(i*self.block,self.n*self.block),2)
        cur=[0,0]

        for i in self.rat_pos[1:]:
            if(not self.running):
                break
            pygame.draw.line(self.win, (255, 0, 0), (self.block//2 + cur[0] * self.block, self.block//2 + cur[1] * self.block),
                             (self.block//2+ i[0] * self.block,self.block//2+ i[1] * self.block), 5)
            cur=i

        pygame.draw.line(self.win,(150,150,150),(self.n*self.block,0),(self.n*self.block,self.SIDE),5)
        self.win.blit(self.RAT, (self.IMG_Pading + (self.rat_pos[-1][0]) * self.block, self.IMG_Pading + (self.rat_pos[-1][1]) * self.block))

        update_canvas=pygame.Rect(0,0,600,600)
        pygame.display.update(update_canvas)

    def find_way(self,x,y):
        self.operations+=1
        if(not self.running):
            return 0
        if(x==self.n-1 and y==self.n-1):
            return 1
        for i in range(4):
            if(not self.running):
                break
            row=x+self.RIGHT_MOVE[i]
            col=y+self.DOWN_MOVE[i]
            if(0<=row<self.n and 0<=col<self.n and self.maze[row][col]==0 and not self.visited[row][col]):
                if(not self.running):
                    break
                self.visited[row][col]=1
                self.rat_pos.append([row,col])
                self.print_maze()
                time.sleep(1/self.speed)
                if(self.find_way(row,col)):
                    return 1
                else:
                    if(not self.running):
                        return 0
                    self.operations+=1
                    self.rat_pos.pop()
                    self.print_maze()
                    time.sleep(1/self.speed)
                
        return 0
                
    def solve(self):
        self.visited[0][0]=1
        if(self.find_way(0,0)):
            ExtraWidgits.OperationsDone(self.operations-1,self.win,700,400,"MAZE is Solved")
        elif(not self.running):
            self.WaitForEndProcess=False
            Rat_In_The_Maze.RunClock=False
            return 0
        else:
            ExtraWidgits.OperationsDone(self.operations-1,self.win,700,400,"MAZE cannot be Solved")
        font = pygame.font.SysFont('Comic Sans MS', 28)
        self.win.blit(font.render("Press Enter to Restart.", False, (255, 255, 255)), (680,500))
        self.WaitForEndProcess=False
        Rat_In_The_Maze.RunClock=False
