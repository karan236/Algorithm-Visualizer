from heapq import heappush, heappop # for priority queue
import random
import pygame
import time
import math
from ExtraElements import *
from test import *
from threading import *
from tkinter import *
import StartProcess
class N_queen():
    def __init__(self,v,speed):
        pygame.init()
        pygame.display.set_caption("N-queens")
        self.diagonal1={};self.diagonal2={};self.col={}
        self.a=[];self.boo=False;self.n=v
        self.SIDE=650;self.block=self.SIDE//self.n
        self.win=pygame.display.set_mode((self.SIDE,self.SIDE))
        self.dtime=speed
        self.Q_SIDE=(3*self.block)//4;
        self.queen = pygame.image.load('Backtrack\Images\queen.png') 
        self.queen=pygame.transform.scale(self.queen,(self.Q_SIDE,self.Q_SIDE))
        self.WHITE=(255,255,255);self.BLACK=(0,0,0);self.RED=(255,0,0)
        

        self.x=(self.block-self.Q_SIDE)//2;self.y=(self.block-self.Q_SIDE)//2
        run=True
        while(run):
            self.win.fill((0,0,0))
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

            self.solve(0)
            pygame.time.delay(5000)
    def grid(self):
        for i in range(self.n):
            for j in range(self.n):
                if((i+j)%2==0):
                    color=self.WHITE
                else:
                    color=self.BLACK
                pygame.draw.rect(self.win,color,(i*self.block,j*self.block,self.block,self.block))
    def show(self):
        self.grid()
        for i in range(len(self.a)):
            self.win.blit(self.queen,(self.x+(self.a[i]-1)*self.block,self.y+i*self.block))
        pygame.display.update()
        pygame.time.delay(self.dtime)
    def attack_col(self,co):
        
        pygame.draw.rect(self.win,(255,0,0),(self.block//2+(co-1)*self.block,self.block//2,5,self.SIDE-self.block))
        #pygame.display.update()
        
    def attack_diagonal1(self,aa):
        yy1=aa-1;xx1=1
        if(aa>self.n):
            yy1=self.n;xx1=aa-self.n
        #print(r,c,xx1,yy1)
        xx1=self.block//2+self.block*(xx1-1);yy1=self.block//2+self.block*(yy1-1)
        pygame.draw.line(self.win, (255,0,0), (xx1,yy1), (yy1,xx1),7)
    def attack_diagonal2(self,aa):
        yy1=aa;xx1=0
        if(aa<0):
            yy1,xx1=xx1,-yy1
        #print(aa,xx1,yy1)
        #xx1=40+80*(xx1-1);yy1=40+80*(yy1-1)
        pygame.draw.line(self.win, (255,0,0), (self.block//2+xx1*self.block,self.block//2+yy1*self.block), (self.block//2+(self.n-yy1-1)*self.block,self.block//2+(self.n-xx1-1)*self.block),7)
    def solve(self,i):
        if(i==self.n):
            print("::SOLVED::")
            boo=True
            return 1
        r=i+1
        for c in range(1,self.n+1):
            self.a.append(c)
            self.show()
            if((c in self.col) or (r+c in self.diagonal1) or (r-c in self.diagonal2)):
                
                if(c in self.col):
                    self.attack_col(c)
                if(r+c in self.diagonal1):
                    self.attack_diagonal1(r+c)
                if(r-c in self.diagonal2):
                    self.attack_diagonal2(r-c)
                pygame.display.update()
                pygame.time.delay(self.dtime)
                self.a.pop()
                continue
            #print(r,c,self.col,self.diagonal1,self.diagonal2)
            self.col[c]=r;
            self.diagonal1[r+c]=r;
            self.diagonal2[r-c]=r
            if(self.solve(i+1)):
                return 1
            self.a.pop()
            del self.diagonal1[r+c];del self.col[c]
            del self.diagonal2[r-c]
        return 0
            
