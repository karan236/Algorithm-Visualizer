import pygame
import time
import ExtraWidgits_for_Pathfinders
import StartProcess
import Astar
import sys
from threading import *
from Make_Nodes import *
from queue import PriorityQueue
from heapq import heappop,heappush,heapify

sys.setrecursionlimit(15000)
RunClock=True
class astar:
    def __init__(self,n,speed):
        pygame.init()
        pygame.font.init()
        self.font = pygame.font.SysFont('Comic Sans MS', 18)
        pygame.display.set_caption("A* PathFinding Visualisation")
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
        #draw(self.win,self.grid,self.No_Of_Rows,self.WINDOW_SIDE)
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
                            Astar.RunClock=True
                            
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
                        Astar.RunClock=True
                        AddClock =ExtraWidgits_for_Pathfinders.Clock(self.win, 840, 215, 25)
                        AddClock.start()
                        for row in self.grid:
                            for spot in row:
                                spot.update_neighbors(self.grid)

                        Solve=Thread(target=self.solve,args=(lambda:draw(self.win,self.grid,self.No_Of_Rows,self.WINDOW_SIDE),))
                        Solve.start()
                        
                    elif(event.key == pygame.K_c):
                        self.start_node=None
                        self.stop_node=None
                        self.solving=False
                        Astar.RunClock=True
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

    
    
    def  heuristic_function(self,p1, p2):
	    x1, y1 = p1
	    x2, y2 = p2
	    return abs(x1 - x2) + abs(y1 - y2)
    
    def astar_function(self,draw):
        count=0
        heap=[]
        heappush(heap,[0,count,self.start_node])
        g_score={node:float("inf") for row in self.grid for node in row}            #Shortest distance from the start_node to the given node
        g_score[self.start_node]=0
        f_score={node:float("inf") for row in self.grid for node in row}            #Sum of g_score and h_score(heuristic_function) 
        f_score[self.start_node]=self.heuristic_function(self.start_node.get_pos(),self.stop_node.get_pos())
        self.visited[self.start_node]=1

        while heap:
            if(not self.running):
                return 0

            current_node=heappop(heap)[2]
            if(current_node==self.stop_node):
                current_node.make_end()
                return True

            current_row,current_col=current_node.get_pos()
            for neighbor in current_node.neighbors :
                if(not self.running):
                    return 0
                
                if(self.visited[neighbor]):
                    continue

                temp_g_score=g_score[current_node]+1

                if(temp_g_score<g_score[neighbor]):
                    self.came_from[neighbor]=current_node
                    g_score[neighbor]=temp_g_score
                    f_score[neighbor]=temp_g_score+self.heuristic_function(neighbor.get_pos(),self.stop_node.get_pos())
                    
                    if(not self.visited[neighbor]):
                        self.operations+=1    
                        count+=1
                        heappush(heap,[f_score[neighbor],count,neighbor])
                        self.visited[neighbor]=1
                        neighbor.make_active()

            if(not self.running):
                return 0    
                
            draw()
            time.sleep(1/self.speed)

            if(current_node!=self.start_node):
                current_node.make_checked()

        return False
                
    
    def solve(self,draw):
        self.visited[self.start_node]=1
        
        if(self.astar_function(draw)):
            Astar.RunClock=False
            ExtraWidgits_for_Pathfinders.Final_Message(self.win,730,410,"Destination Reached.")
            ExtraWidgits_for_Pathfinders.OperationsDone(self.operations-1,self.win,700,450)
            reconstruct_path(self.came_from,self.stop_node,self.start_node,draw)
            
        elif(not self.running):
            pass

        else:
            ExtraWidgits_for_Pathfinders.Final_Message(self.win,680,410,"Destination cannot be Reached.")
            ExtraWidgits_for_Pathfinders.OperationsDone(self.operations-1,self.win,700,450)

        Astar.RunClock=False    
        self.WaitForEndProcess=False
        self.solving=False
        self.operations=0
        self.visited={node:0 for row in self.grid for node in row}
        self.came_from={node:None for row in self.grid for node in row}
