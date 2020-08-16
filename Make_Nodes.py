import pygame
import math
import time
import sys
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
LIGHT_BLUE = (64, 224, 208)

class Node:
    def __init__(self,row,col,width,total_rows):
        self.row=row
        self.col=col
        self.x=row*width
        self.y= col*width
        self.color=WHITE
        self.neighbors = []
        self.width=width
        self.total_rows=total_rows

    def get_pos(self):
        return self.row,self.col

    def is_way(self):
        return self.color==WHITE
    
    def is_start(self):
        return self.color==ORANGE

    def is_end(self):
        return self.color == LIGHT_BLUE

    def is_barrier(self):
        return self.color==BLACK

    def is_checked(self):
        return self.color== RED
    
    def is_active(self):
        return self.color==GREEN

    def reset(self):
        self.color = WHITE

    def make_start(self):
        self.color = ORANGE

    def make_checked(self):
        self.color = RED

    def make_active(self):
        self.color = GREEN

    def make_barrier(self):
        self.color = BLACK

    def make_end(self):
        self.color = LIGHT_BLUE

    def make_path(self):
        self.color = PURPLE

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        self.neighbors = []
        
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier(): # DOWN
            self.neighbors.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier(): # UP
            self.neighbors.append(grid[self.row - 1][self.col])

        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier(): # RIGHT
            self.neighbors.append(grid[self.row][self.col + 1])

        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier(): # LEFT
            self.neighbors.append(grid[self.row][self.col - 1])
    

def draw_grid_lines(win, rows,window_side):
    width= window_side// rows
	
    for i in range(rows+1):
        pygame.draw.line(win,GREY, (0, i * width), (rows*width, i * width))
        pygame.draw.line(win,GREY, (i * width, 0), (i * width,rows*width))

def make_grid(rows,window_side):
    grid = []
    width= window_side// rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, width, rows)
            grid[i].append(node)

    return grid


def reconstruct_path(came_from,current,start, draw):
    
    while current in came_from:
        current = came_from[current]
        if(current==start):
            return 1
        current.make_path()
        draw()


def draw(win, grid, rows,window_side):
    width=window_side//rows
    pygame.draw.rect(win,WHITE,(0,0,rows*width,rows*width))
    for row in grid:
        #print(DFS.dfs.running)
        for node in row:
            node.draw(win)

    draw_grid_lines(win, rows,window_side)
    update_Canvas=pygame.Rect(0,0,600,600)
    pygame.display.update(update_Canvas)


def get_clicked_pos(pos, rows,window_side):
    width= window_side// rows
    y, x = pos

    row = y // width
    col = x // width

    return row, col

