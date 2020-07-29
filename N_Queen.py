import pygame
import time
from threading import *
from ExtraWidgits import *
import StartProcess

RunClock=True


class N_queen:
    def __init__(self, v, speed):
        pygame.init()
        pygame.display.set_caption("N-Queens")
        self.diagonal1 = {}
        self.diagonal2 = {}
        self.col = {}
        self.operations=0
        self.a = []
        self.boo = False
        self.WaitForEndProcess=True
        self.n = v
        self.SIDE = 600
        self.block = self.SIDE // self.n
        self.win = pygame.display.set_mode((self.SIDE+450, self.SIDE))
        self.speed=speed
        self.Q_SIDE = (3 * self.block) // 4
        self.queen = pygame.image.load('Images/queen.png')
        self.queen = pygame.transform.scale(self.queen, (self.Q_SIDE, self.Q_SIDE))
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)

        self.x = (self.block - self.Q_SIDE) // 2
        self.y = (self.block - self.Q_SIDE) // 2

        self.running = True

        self.StartVisualization()

    def StartVisualization(self):
        self.grid()
        AddClock = Clock(self.win, 850, 100, 25)
        AddClock.start()
        AddMainMenuButton = MainMenuButton(self.win,700,300)
        AddMainMenuButton.start()
        AddExitText = ExitText(self.win,725,250)
        AddExitText.start()
        StartSolving=Thread(target=self.solve,args=(0,))
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
                            N_Queen.RunClock=True
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

    def show(self):
        self.grid()
        for i in range(len(self.a)):
            if not self.running:
                break
            self.win.blit(self.queen, (self.x + (self.a[i] - 1) * self.block, self.y + i * self.block))


    def attack_col(self, co):

        pygame.draw.rect(self.win, (255, 0, 0),
                         (self.block // 2 + (co - 1) * self.block, self.block // 2, 5, self.SIDE - self.block))

    def attack_diagonal1(self, aa):
        yy1 = aa - 1
        xx1 = 1
        if (aa > self.n):
            yy1 = self.n
            xx1 = aa - self.n
        xx1 = self.block // 2 + self.block * (xx1 - 1)
        yy1 = self.block // 2 + self.block * (yy1 - 1)
        pygame.draw.line(self.win, (255, 0, 0), (xx1, yy1), (yy1, xx1), 7)

    def attack_diagonal2(self, aa):
        yy1 = aa
        xx1 = 0
        if (aa < 0):
            yy1, xx1 = xx1, -yy1
        pygame.draw.line(self.win, (255, 0, 0),
                         (self.block // 2 + xx1 * self.block, self.block // 2 + yy1 * self.block), (
                         self.block // 2 + (self.n - yy1 - 1) * self.block,
                         self.block // 2 + (self.n - xx1 - 1) * self.block), 7)

    def solve(self, i):
        if (i == self.n):
            boo = True
            return 1
        r = i + 1
        for c in range(1, self.n + 1):
            if not self.running:
                break
            self.operations+=1
            self.a.append(c)
            self.show()
            if not self.running:
                break
            time.sleep(1/self.speed)
            if ((c in self.col) or (r + c in self.diagonal1) or (r - c in self.diagonal2)):

                if (c in self.col):
                    self.attack_col(c)
                    self.operations += 1
                if (r + c in self.diagonal1):
                    self.attack_diagonal1(r + c)
                    self.operations += 1
                if (r - c in self.diagonal2):
                    self.attack_diagonal2(r - c)
                    self.operations += 1
                if not self.running:
                    break
                time.sleep(1/self.speed)
                self.a.pop()
                self.operations += 1
                continue
            if not self.running:
                break
            self.col[c] = r
            self.diagonal1[r + c] = r
            self.diagonal2[r - c] = r
            self.operations += 1
            if (self.solve(i + 1)):
                OperationsDone(self.operations, self.win,700,400,"Queens Placed.")
                N_Queen.RunClock=False
                self.WaitForEndProcess=False
                return 1
            self.a.pop()
            self.operations += 1
            del self.diagonal1[r + c]
            del self.col[c]
            del self.diagonal2[r - c]
        self.WaitForEndProcess=False
        return 0
'''
run=True
while(run):
    
    k=N_queen(9,17)
    run=False
'''
