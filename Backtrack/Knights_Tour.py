import pygame
from heapq import heappush, heappop # for priority queue
import random

#from ALGO.N_queen import *
class Knight():
    def __init__(self,v,speed):
        self.n=v
        self.cb=[[0 for x in range(v)] for y in range(v)]
        self.ans=[]
        self.dtime=speed
        pygame.init()
        self.SIDE=650
        self.block=self.SIDE//self.n
        self.win=pygame.display.set_mode((self.SIDE,self.SIDE))
        self.K_SIDE=(self.block*3)//4
        self.knight_img= pygame.image.load('Backtrack\Images\knight2.png') 
        self.knight_img=pygame.transform.scale(self.knight_img,(self.K_SIDE,self.K_SIDE))
        self.WHITE=(255,255,255);self.BLACK=(0,0,0);self.RED=(255,0,0)
        pygame.display.set_caption("KNIGHT'S TOUR")
        self.x=self.block//2;self.y=self.block//2
        self.x1=(self.block-self.K_SIDE)//2
        self.line_w=-int(-70//self.n)
        self.grid()
        run=True
        while(run):
            execute=False
            pygame.time.delay(10)
            for event in pygame.event.get():
                if(event.type==pygame.QUIT):
                    run=False
            k=pygame.key.get_pressed()
            if(k[pygame.K_SPACE]):
                execute=True
    
            if(not execute):
                self.grid()
                pygame.display.update() 
                continue

            self.solve()
            pygame.time.delay(50000)    
            #break
            run=False

    def grid(self):
        for i in range(self.n):
            for j in range(self.n):
                if((i+j)%2==0):
                    color=self.WHITE
                else:
                    color=self.BLACK
                pygame.draw.rect(self.win,color,(i*self.block,j*self.block,self.block,self.block))
                if([i,j] in self.ans):
                    color=(0,180,0)
                    pygame.draw.rect(self.win,(120,255,0),(self.x1+i*self.block,self.x1+j*self.block,self.K_SIDE,self.K_SIDE))
    def show(self):
        self.grid()
        xx,yy=self.ans[0]
        for i in range(1,len(self.ans)):
            tx,ty=self.ans[i]
            pygame.draw.line(self.win, (255,0,0), (self.x+xx*self.block,self.x+yy*self.block), (self.x+tx*self.block,self.x+ty*self.block),self.line_w)
            xx,yy=self.ans[i]
        self.win.blit(self.knight_img,(self.x1+xx*self.block,self.x1+yy*self.block))
        pygame.display.update()
        pygame.time.delay(self.dtime)
        
    def solve(self):
        print("start")
        kx = random.randint(0, self.n - 1)
        ky = random.randint(0, self.n - 1)
        dx = [-2, -1, 1, 2, -2, -1, 1, 2]
        dy = [1, 2, 2, 1, -1, -2, -2, -1]
        for k in range(self.n**2):
            self.cb[ky][kx] = k + 1
            self.ans.append([kx,ky])
            self.show()
            #print(self.ans)
            pq = [] # priority queue of available neighbors
            for i in range(8):
                nx = kx + dx[i]; ny = ky + dy[i]
                if 0<=nx<self.n and 0<=ny<self.n:
                    if self.cb[ny][nx] == 0:
                        # count the available neighbors of the neighbor
                        ctr = 0
                        for j in range(8):
                            ex = nx + dx[j]; ey = ny + dy[j]
                            if 0<=ex<self.n and 0<=ey<self.n:
                                if self.cb[ey][ex] == 0: ctr += 1
                        heappush(pq, (ctr, i))
            # move to the neighbor that has min number of available neighbors
            if len(pq) > 0:
                (p, m) = heappop(pq)
                kx += dx[m]; ky += dy[m]
            else:
                break
        #print(self.ans)
        return True
    
