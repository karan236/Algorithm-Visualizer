import pygame
import time
from threading import *
import DFS
import Astar

class Clock(Thread):
    def __init__(self,screen,CordinateX,CordinateY,font,*args):
        Thread.__init__(self)
        self.screen = screen
        self.CordinateX=CordinateX
        self.CordinateY=CordinateY
        pygame.draw.rect(screen,(0,0,0),(self.CordinateX-50,self.CordinateY,80,50))
        self.ClockComplete=False
        self.font=font
        self.running=True
        self.Clock=[0,0]
        self.printTime= "00:00"

    def run(self):
        try:
            while(DFS.RunClock and Astar.RunClock):
                pygame.font.init()

                myfont = pygame.font.SysFont('Comic Sans MS', self.font)
                self.textsurface = myfont.render(self.printTime, False, (255, 255, 255))
                self.screen.blit(self.textsurface, (self.CordinateX-50, self.CordinateY))

                myfont = pygame.font.SysFont('Comic Sans MS', self.font)
                self.textsurface = myfont.render(" Time Escaped:", False, (255, 255, 255))
                self.screen.blit(self.textsurface, (self.CordinateX-120, self.CordinateY-30))

                time.sleep(1)
                if not DFS.RunClock or not Astar.RunClock:
                    break
                
                textsurface = myfont.render(self.printTime, False, (0, 0, 0))
                self.screen.blit(textsurface, (self.CordinateX-50, self.CordinateY))


                if not self.ClockComplete:

                    if self.Clock[1]==59:

                        self.Clock[0]+=1
                        self.Clock[1]=0
                        if len(str(self.Clock[0])) == 1:
                            self.printTime = '0' + str(self.Clock[0])
                        else:
                            self.printTime = str(self.Clock[0])
                        self.printTime=str(self.Clock[0])+':'+ '0' + str(self.Clock[1])

                    else:

                        self.Clock[1]+=1
                        if len(str(self.Clock[0])) == 1 and len(str(self.Clock[1]))==1:
                            self.printTime='0'+str(self.Clock[0])+':' +'0' + str(self.Clock[1])
                        elif len(str(self.Clock[1]))==1:
                            self.printTime=str(self.Clock[0])+':'+ '0' + str(self.Clock[1])
                        elif len(str(self.Clock[0])) == 1:
                            self.printTime = '0'+str(self.Clock[0]) + ':' + str(self.Clock[1])
                        else:
                            self.printTime = str(self.Clock[0])+ ':' + str(self.Clock[1])

            myfont = pygame.font.SysFont('Comic Sans MS', self.font)
            textsurface = myfont.render(self.printTime, False, (255, 255, 255))
            self.screen.blit(textsurface, (self.CordinateX-50, self.CordinateY))
            
        except:
            pass




class MainMenuButton(Thread):
    def __init__(self,screen,CordinateX,CordinateY,*args):
        Thread.__init__(self)
        self.X=CordinateX
        self.Y=CordinateY
        self.screen = screen
        self.CordinateX=CordinateX
        self.CordinateY=CordinateY
        self.ClockComplete=False

    def run(self):
        try:
            while(True):
                if(not self.screen):
                    break
                self.pos=pygame.mouse.get_pos()

                self.OnMainMenuButton=False
                if self.pos[0] > self.X and self.pos[0] < self.X + 240 and self.pos[1] > self.Y and self.pos[1] < self.Y + 35:
                    self.OnMainMenuButton=True

                pygame.font.init()

                if self.OnMainMenuButton == False:
                    pygame.draw.rect(self.screen,(255,255,255),(self.X,self.Y,240,35))
                    myfont = pygame.font.SysFont('Comic Sans MS', 20)
                    textsurface = myfont.render("Go Back to Main Menu", False, (0, 0, 0))
                    self.screen.blit(textsurface, (self.X+17, self.Y))
                else:
                    pygame.draw.rect(self.screen,(0,0,0),(self.X,self.Y,240,35))
                    pygame.draw.rect(self.screen,(255,255,255),(self.X,self.Y,240,35),3)
                    myfont = pygame.font.SysFont('Comic Sans MS', 20)
                    textsurface = myfont.render("Go Back to Main Menu", False, (255, 255, 255))
                    self.screen.blit(textsurface, (self.X+17, self.Y))
                    
                update_Widgits=pygame.Rect(600,0,450,600)
                pygame.display.update(update_Widgits)
                
        except:
            pass


class Instructions(Thread):
    def __init__(self,screen,*args):
        Thread.__init__(self)
        self.win = screen
        self.ClockComplete=False
        pygame.font.init()
        self.font = pygame.font.SysFont('Comic Sans MS', 20)

    def run(self):
        try:
            while(True):
                self.win.blit(self.font.render("Select  Starting and Ending nodes.", False, (255, 255, 255)),(660,50))
                self.win.blit(self.font.render("Click on cells to create wall.", False, (255, 255, 255)), (690,75))
                self.win.blit(self.font.render("Press Space to START", False, (255, 255, 255)),(710,100))
                self.win.blit(self.font.render("Press 'C' to Clear Screen", False, (255, 255, 255)),(700,150))
        
        except:
            pass
        
class ExitText(Thread):
    def __init__(self,screen,CordinateX,CordinateY,*args):
        Thread.__init__(self)
        self.X=CordinateX
        self.Y=CordinateY
        self.screen = screen
        self.CordinateX=CordinateX
        self.CordinateY=CordinateY
        self.ClockComplete=False

    def run(self):
        try:
            while(True):
                pygame.font.init()
                myfont = pygame.font.SysFont('Comic Sans MS', 20)
                textsurface = myfont.render("Press Esc to Exit.", False, (255, 255, 255))
                self.screen.blit(textsurface, (self.X+17, self.Y))
        except:
            pass



class OperationsDone:
    def __init__(self,NoOfOperations,screen,X,Y):
        try:
            self.NoOfOperations=NoOfOperations
            self.screen=screen
            self.X=X
            self.Y=Y
            pygame.font.init()
            pygame.draw.rect(self.screen,(0,0,0),(self.X,self.Y,280,30))
            myfont = pygame.font.SysFont('Comic Sans MS', 20)
            textsurface = myfont.render("Operations Performed: "+str(self.NoOfOperations), False, (255, 255, 255))
            self.screen.blit(textsurface, (self.X, self.Y))
        except:
            pass

class Final_Message:
    def __init__(self,screen,X,Y,message):
        self.screen=screen
        self.X=X
        self.Y=Y
        pygame.font.init()
        pygame.draw.rect(self.screen,(0,0,0),(self.X-100,self.Y,380,30))
        myfont = pygame.font.SysFont('Comic Sans MS', 20)
        textsurface = myfont.render(message, False, (255, 255, 255))
        self.screen.blit(textsurface, (self.X, self.Y))
