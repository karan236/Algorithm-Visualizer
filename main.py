import pygame
import random
import time
from tkinter import *
from threading import *
import StartProcess


Process=StartProcess.START()

Process.start()



'''
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)

screen = pygame.display.set_mode((800, 400))

pygame.display.set_caption("Sorting Visualizer")

running = True
array = []

j = 2.5
while(j < 400):
    array.append(j)
    j += 2.5

random.shuffle(array)

while(running):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    for i in range(len(array)):
        pygame.draw.line(screen, white, ((i+1)*5, 0), ((i+1)*5, array[i]), 3)
    pygame.display.update()

    for j in range(len(array)):
        for i in range(len(array)-1):
            if array[i]>array[i+1]:
                pygame.draw.line(screen, green, ((i + 1) * 5, 0), ((i + 1) * 5, array[i]), 3)
                pygame.draw.line(screen, red, ((i + 2) * 5, 0), ((i + 2) * 5, array[i + 1]), 3)
                pygame.display.update()
                time.sleep(0.01)
                array[i],array[i+1]=array[i+1],array[i]
                pygame.draw.line(screen, green, ((i + 2) * 5, 0), ((i + 2) * 5, array[i + 1]), 3)
                pygame.draw.line(screen, black, ((i + 1) * 5, 0), ((i + 1) * 5, array[i + 1]), 3)
                pygame.draw.line(screen, red, ((i + 1) * 5, 0), ((i + 1) * 5, array[i]), 3)
                pygame.display.update()
                time.sleep(0.01)
                pygame.draw.line(screen, white, ((i + 1) * 5, 0), ((i + 1) * 5, array[i]), 3)
                pygame.draw.line(screen, white, ((i + 2) * 5, 0), ((i + 2) * 5, array[i+1]), 3)
                pygame.display.update()
            else:
                pygame.draw.line(screen, green, ((i + 1) * 5, 0), ((i + 1) * 5, array[i]), 3)
                pygame.draw.line(screen, green, ((i + 2) * 5, 0), ((i + 2) * 5, array[i + 1]), 3)
                pygame.display.update()
                time.sleep(0.01)
                pygame.draw.line(screen, white, ((i + 1) * 5, 0), ((i + 1) * 5, array[i]), 3)
                pygame.draw.line(screen, white, ((i + 2) * 5, 0), ((i + 2) * 5, array[i+1]), 3)
                pygame.display.update()
            pygame.event.get()
    pygame.display.update()
'''