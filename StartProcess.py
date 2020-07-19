import random
import time
from tkinter import *
from MainMenu import front
from threading import *

class START(Thread):
    def run(self):
        root=Tk()
        front(root)
        root.mainloop()