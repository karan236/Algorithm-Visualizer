import pygame
from heapq import *
import random
import time
import ExtraWidgits
import ExtraWidgits_for_Pathfinders
from threading import *
import StartProcess
import Knight_Tour

RunClock=True

class Knight():
    def __init__(self, v, speed):
        self.n = v
        self.cb = [[0 for x in range(v)] for y in range(v)]
        self.ans = []
        self.speed = speed
        self.WaitForEndProcess=True
        self.operations=0
        self.running=True

        pygame.init()
        self.SIDE = 600
        self.block = self.SIDE // self.n
        self.win = pygame.display.set_mode((self.SIDE+450, self.SIDE))
        self.K_SIDE = (self.block * 3) // 4
        self.knight_img = pygame.image.load('Images/knight2.png')
        self.knight_img = pygame.transform.scale(self.knight_img, (self.K_SIDE, self.K_SIDE))
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        pygame.display.set_caption("KNIGHT'S TOUR")
        self.x = self.block // 2
        self.y = self.block // 2
        self.x1 = (self.block - self.K_SIDE) // 2
        self.line_w = -int(-70 // self.n)

        self.StartVisualization()



    def StartVisualization(self):
        self.grid()
        AddClock = ExtraWidgits.Clock(self.win, 850, 100, 25)
        AddClock.start()
        
        AddExitText = ExtraWidgits.ExitText(self.win,725,250)
        AddExitText.start()
        AddMainMenuButton = ExtraWidgits_for_Pathfinders.MainMenuButton(self.win,700,300)
        AddMainMenuButton.start()
        
        StartSolving=Thread(target=self.solve)
        StartSolving.start()
        self.CheckActions()



    def CheckActions(self):
        self.X = 700
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
                            Knight_Tour.RunClock=True
                        except:
                            pass


    def grid(self):
        for i in range(self.n):
            for j in range(self.n):
                if not self.running:
                    break
                if ((i + j) % 2 == 0):
                    color = self.WHITE
                else:
                    color = self.BLACK
                pygame.draw.rect(self.win, color, (i * self.block, j * self.block, self.block, self.block))
                if ([i, j] in self.ans):
                    color = (0, 180, 0)
                    pygame.draw.rect(self.win, (120, 255, 0),
                                     (self.x1 + i * self.block, self.x1 + j * self.block, self.K_SIDE, self.K_SIDE))


    def show(self):
        self.grid()
        xx, yy = self.ans[0]
        for i in range(1, len(self.ans)):
            if not self.running:
                break
            tx, ty = self.ans[i]
            pygame.draw.line(self.win, (255, 0, 0), (self.x + xx * self.block, self.x + yy * self.block),
                             (self.x + tx * self.block, self.x + ty * self.block), self.line_w)
            xx, yy = self.ans[i]
        self.win.blit(self.knight_img, (self.x1 + xx * self.block, self.x1 + yy * self.block))

        update_display=pygame.Rect(0,0,self.SIDE,self.SIDE)
        pygame.display.update(update_display)



    def solve(self):
        kx = random.randint(0, self.n - 1)
        ky = random.randint(0, self.n - 1)
        dx = [-2, -1, 1, 2, -2, -1, 1, 2]
        dy = [1, 2, 2, 1, -1, -2, -2, -1]
        for k in range(self.n ** 2):
            if not self.running:
                break
            self.operations+=1
            self.cb[ky][kx] = k + 1
            self.ans.append([kx, ky])
            self.show()
            if not self.running:
                break
            time.sleep(1/self.speed)
            pq = []
            for i in range(8):
                self.operations+=1
                if not self.running:
                    break
                nx = kx + dx[i]
                ny = ky + dy[i]
                if 0 <= nx < self.n and 0 <= ny < self.n:
                    if self.cb[ny][nx] == 0:
                        ctr = 0
                        for j in range(8):
                            self.operations+=1
                            if not self.running:
                                break
                            ex = nx + dx[j]
                            ey = ny + dy[j]
                            if 0 <= ex < self.n and 0 <= ey < self.n:
                                if self.cb[ey][ex] == 0: ctr += 1
                        heappush(pq, (ctr, i))
            if len(pq) > 0:
                (p, m) = heappop(pq)
                kx += dx[m]
                ky += dy[m]
            else:
                break
        if self.running:
            ExtraWidgits.OperationsDoneKnight(self.operations, self.win, 700, 400, "Knight's Tour Completed.")
        Knight_Tour.RunClock=False
        self.WaitForEndProcess=False
        return True
