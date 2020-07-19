import pygame
import random
import time
import math
from ExtraElements import *
from test import *
from threading import *
from tkinter import *
import StartProcess

RunClock=True

class Sorting:
    def __init__(self, NoOfElements, Speed, AlgorithmName):
        self.NoOfElements = NoOfElements
        self.Speed = Speed
        self.AlgorithmName = AlgorithmName
        self.white = (255, 255, 255)
        self.green = (0, 255, 0)
        self.red = (255, 0, 0)
        self.black = (0, 0, 0)
        self.blue = (0,0,255)
        self.running = True
        self.Sorting = True
        self.array = []
        self.colours=[]
        self.Operations=0
        for i in range(self.NoOfElements):
            self.colours.append(self.white)
        self.WaitForEndProcess = True

        self.HeightDiff = 400/self.NoOfElements

        self.gap = 2

        for i in range(1, self.NoOfElements + 1):
            self.array.append(self.HeightDiff * i)

        self.thickness = math.ceil((800 - self.gap * (self.NoOfElements + 1)) / self.NoOfElements)
        self.initial = (self.gap + self.thickness) / 2
        self.difference = self.thickness + self.gap

        self.resize_x = int(self.initial + (self.NoOfElements-1)*self.difference)

        self.screen = pygame.display.set_mode((self.resize_x+(math.ceil(self.thickness/2)+self.gap), 600))

        pygame.display.set_caption(self.AlgorithmName)

        random.shuffle(self.array)

        self.StartVisualisation()

    def StartVisualisation(self):
        try:
            AddClock = Clock(self.screen, self.resize_x + (math.ceil(self.thickness / 2) + self.gap) - 75,
                             550, 25)
            AddClock.start()
            AddMainMenuButton=MainMenuButton(self.screen,(self.resize_x + (math.ceil(self.thickness / 2) + self.gap)) / 3,550)
            AddMainMenuButton.start()
            AddExitText= ExitText(self.screen,((self.resize_x + (math.ceil(self.thickness / 2) + self.gap)) / 3) +25 ,500)
            AddExitText.start()

        except:
            pass

        if self.AlgorithmName == 'Bubble Sort':
            DrawElements = Thread(target=self.DrawBubleSort)
            DrawElements.start()

        elif self.AlgorithmName == "Selection Sort":
            DrawElements = Thread(target=self.DrawSelectionSort)
            DrawElements.start()



        self.CheckActions()


    def CheckActions(self):
        self.X = (self.resize_x+(math.ceil(self.thickness/2)+self.gap))/3
        self.Y = 550
        while (self.running):
            try:
                self.pos = pygame.mouse.get_pos()
            except:
                pass
            for event in pygame.event.get():
                if event.type == pygame.QUIT:

                    pygame.quit()
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                        pygame.quit()

                if self.pos[0] > self.X and self.pos[0] < self.X + 240 and self.pos[1] > self.Y and self.pos[
                    1] < self.Y + 35:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        try:
                            self.running=False
                            self.Sorting=False
                            Process = StartProcess.START()
                            Process.start()

                            while(self.WaitForEndProcess):
                                pass

                            pygame.quit()
                            SortingAlgorithm.RunClock=True
                        except:
                            pass


    def draw(self):
        self.last = self.initial
        for i in range(len(self.array)):
            pygame.draw.line(self.screen, self.colours[i], (self.last, 0), (self.last, self.array[i]),self.thickness)
            self.last += self.difference

        if self.array==sorted(self.array):
            self.Sorting=False
            self.last = self.initial
            for i in range(len(self.array)):
                pygame.draw.line(self.screen, self.green, (self.last, 0), (self.last, self.array[i]),self.thickness)
                self.last += self.difference

            OperationsDone(self.Operations, self.screen,
                           (self.resize_x + (math.ceil(self.thickness / 2) + self.gap)) / 6 - 125, 450)
            SortingAlgorithm.RunClock=False


    def DrawBubleSort(self):
        self.CurrentPosition=0
        while(self.Sorting):
            try:
                if self.CurrentPosition == self.NoOfElements -1:
                    self.CurrentPosition=0
                self.Operations+=1
                if self.array[self.CurrentPosition] > self.array[self.CurrentPosition+1]:
                    self.Operations+=1
                    self.colours[self.CurrentPosition]=self.green
                    self.colours[self.CurrentPosition+1]=self.red
                    self.draw()

                    time.sleep(1/self.Speed)
                    if not self.running:
                        self.WaitForEndProcess=False
                        break

                    self.colours[self.CurrentPosition] = self.black
                    self.draw()
                    self.array[self.CurrentPosition],self.array[self.CurrentPosition+1]=self.array[self.CurrentPosition+1],self.array[self.CurrentPosition]
                    self.colours[self.CurrentPosition]=self.red
                    self.colours[self.CurrentPosition+1] = self.green
                    self.draw()

                    time.sleep(1/self.Speed)

                    self.colours[self.CurrentPosition] = self.white
                    self.colours[self.CurrentPosition + 1] = self.white

                else:
                    self.colours[self.CurrentPosition]=self.green
                    self.colours[self.CurrentPosition+1]=self.green
                    self.draw()

                    time.sleep(1/self.Speed)

                    self.colours[self.CurrentPosition] = self.white
                    self.colours[self.CurrentPosition+1] = self.white
                self.CurrentPosition+=1
                self.WaitForEndProcess=False
            except:
                pass


    def DrawSelectionSort(self):
        self.CurrentPosition=0
        while(self.Sorting):
            self.WaitForEndProcess=True
            self.min=min(self.array[self.CurrentPosition:])
            self.minPosition=0
            for i in range(self.CurrentPosition,self.NoOfElements):
                self.Operations+=1
                if self.array[i]==self.min:
                    self.minPosition=i
                self.colours[i] = self.blue
                self.draw()
                time.sleep(1/self.Speed)
                self.colours[i] = self.white
                if not self.running:
                    break
            self.Operations+=1
            if not self.running:
                self.WaitForEndProcess=False
                break
            if self.CurrentPosition==self.minPosition:
                self.colours[self.minPosition]=self.green
                self.draw()
                time.sleep(1/self.Speed)
                self.colours[self.minPosition]=self.white
            else:
                self.colours[self.CurrentPosition]=self.red
                self.colours[self.minPosition]=self.green
                self.draw()
                time.sleep(1/self.Speed)
                self.colours[self.CurrentPosition] = self.black
                self.colours[self.minPosition] = self.white
                self.draw()
                self.array[self.CurrentPosition],self.array[self.minPosition]=self.array[self.minPosition],self.array[self.CurrentPosition]

                self.colours[self.CurrentPosition] = self.green
                self.colours[self.minPosition] = self.red
                self.draw()
                time.sleep(1/self.Speed)
                self.colours[self.CurrentPosition] = self.white
                self.colours[self.minPosition] = self.white

            self.CurrentPosition+=1
            self.WaitForEndProcess=False