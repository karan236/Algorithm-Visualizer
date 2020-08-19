from Make_Nodes import *
import pygame
import time
from threading import *
import ExtraWidgits_for_Pathfinders
import StartProcess
import DFS
import sys

sys.setrecursionlimit(15000)
RunClock=True
class dfs:
    def __init__(self,n,speed):
        pygame.init()
        pygame.font.init()
        self.font = pygame.font.SysFont('Comic Sans MS', 18)
        pygame.display.set_caption("DFS PathFinding Visualisation")
        self.operations=0
        self.WaitForEndProcess=False
        self.running=True
        
        self.No_Of_Rows = n
        self.WINDOW_SIDE = 600
        self.block =self.WINDOW_SIDE // self.No_Of_Rows
        self.win = pygame.display.set_mode((self.WINDOW_SIDE+450,self.WINDOW_SIDE))
        self.speed=speed

        self.grid=make_grid(self.No_Of_Rows,self.WINDOW_SIDE)
        self.start_node=None
        self.stop_node=None

        self.visited={node:0 for row in self.grid for node in row}
        self.came_from={node:None for row in self.grid for node in row}
        self.RIGHT_LEFT=[1,0,-1,0]
        self.UP_DOWN=[0,-1,0,1]

        self.solving=False
        self.StartVisualization()
        #self.Canvas()
        
        
    def StartVisualization(self):

        AddInstructions=ExtraWidgits_for_Pathfinders.Instructions(self.win)
        AddInstructions.start()

        AddExitText = ExtraWidgits_for_Pathfinders.ExitText(self.win,715,275)
        AddExitText.start()
        
        AddMainMenuButton = ExtraWidgits_for_Pathfinders.MainMenuButton(self.win,700,325)
        AddMainMenuButton.start()
        
        self.Canvas()

    def Canvas(self):
        pygame.init()
        cur=[None,None]
        X=700
        Y=325
        while(self.running):
            if(not self.running):
                break
            try:
                pos = pygame.mouse.get_pos()
            except:
                pass
            if(not self.solving):
                draw(self.win,self.grid,self.No_Of_Rows,self.WINDOW_SIDE)

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.running=False
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONUP:
                        cur=[None,None]

                if X <pos[0] < X + 240 and Y <pos[1] < Y + 35:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        try:
                            self.running=False
                            while(self.WaitForEndProcess):
                                pass
                            pygame.quit()
                            Process = StartProcess.START()
                            Process.start()
                            DFS.RunClock=True
                            
                        except:
                            pass
                        
                if(self.solving):
                    continue
                
                elif(event.type == pygame.KEYDOWN):
                    if(event.key ==pygame.K_SPACE and self.start_node and self.stop_node and not self.solving):
                        
                        #print("::START::")
                        self.opreations=0
                        self.solving=True
                        self.WaitForEndProcess=True
                        DFS.RunClock=True
                        AddClock =ExtraWidgits_for_Pathfinders.Clock(self.win, 840, 215, 25)
                        AddClock.start()
                        Solve=Thread(target=self.solve,args=(lambda:draw(self.win,self.grid,self.No_Of_Rows,self.WINDOW_SIDE),))
                        Solve.start()
                        
                    elif(event.key == pygame.K_c):
                        self.start_node=None
                        self.stop_node=None
                        self.solving=False
                        DFS.RunClock=True
                        self.operation=0
                        self.grid=make_grid(self.No_Of_Rows,self.WINDOW_SIDE)
                        self.visited={node:0 for row in self.grid for node in row}
                        self.came_from={node:None for row in self.grid for node in row}

                if(pos[0]>=self.WINDOW_SIDE or pos[1]>=self.WINDOW_SIDE):
                        continue
                    
                if(pygame.mouse.get_pressed()[0]):
                    row,col=get_clicked_pos(pos,self.No_Of_Rows,self.WINDOW_SIDE)
                    
                    if(cur==[row,col]):
                        continue
                    cur=[row,col]
                    
                    if event.type == pygame.MOUSEBUTTONUP:
                        cur=[None,None]

                    node=self.grid[row][col]
                    if(node== self.start_node):
                        self.start_node=None
                        node.reset()
                        
                    elif(node== self.stop_node):
                        self.stop_node=None
                        node.reset()
                        
                    elif not self.start_node and node!=self.stop_node and not node.is_barrier():
                        self.start_node=node
                        self.start_node.make_start()
                        
                    elif not self.stop_node and node!=self.start_node and not node.is_barrier():
                        self.stop_node=node
                        self.stop_node.make_end()

                    elif node!= self.start_node and node!=self.stop_node and node.is_barrier():
                        node.reset()
                        
                    elif node!= self.start_node and node!=self.stop_node and not node.is_barrier():
                        node.make_barrier()

     

    def DFS_function(self,draw,current_node):
        draw()
        time.sleep(1/(self.speed*2))
        self.operations+=1
        if(not self.running):
            return 0
        for event in pygame.event.get():
            if(not self.running):
                return 0

            
            if event.type == pygame.QUIT:
                pygame.quit()
        if(current_node==self.stop_node):
            return 1

        row,col=current_node.get_pos()
        for i in range(4):
            if(not self.running):
                return 0
            
            neighbours_row,neighbours_col=row+self.UP_DOWN[i],col+self.RIGHT_LEFT[i]
            
            if(0<=neighbours_row<self.No_Of_Rows and 0<=neighbours_col<self.No_Of_Rows):
                neighbours_node=self.grid[neighbours_row][neighbours_col]
                
                if(not self.visited[neighbours_node] and  not neighbours_node.is_barrier()):
                    self.visited[neighbours_node]=1
                    
                    if neighbours_node!= self.stop_node:
                        neighbours_node.make_active()
                    self.came_from[neighbours_node]=current_node
                    
                    if(self.DFS_function(draw,neighbours_node)):
                        return 1

                    
        if(not self.running):
            return 0
        
        if current_node != self.start_node:
            current_node.make_checked()
        draw()
        time.sleep(1/(self.speed*2))
        return False
                    
    
    def solve(self,draw):
        self.visited[self.start_node]=1
        
        if(self.DFS_function(draw,self.start_node)):
            DFS.RunClock=False
            ExtraWidgits_for_Pathfinders.Final_Message(self.win,730,410,"Destination Reached.")
            ExtraWidgits_for_Pathfinders.OperationsDone(self.operations-1,self.win,700,450)
            reconstruct_path(self.came_from,self.stop_node,self.start_node,draw)
            
        elif(not self.running):
            pass

        else:
            ExtraWidgits_for_Pathfinders.Final_Message(self.win,680,410,"Destination cannot be Reached.")
            ExtraWidgits_for_Pathfinders.OperationsDone(self.operations-1,self.win,700,450)

        DFS.RunClock=False    
        self.WaitForEndProcess=False
        self.solving=False
        self.operations=0
        self.visited={node:0 for row in self.grid for node in row}
        self.came_from={node:None for row in self.grid for node in row}
