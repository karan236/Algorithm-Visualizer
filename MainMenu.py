from  tkinter import *
from tkinter import messagebox
from SortingAlgorithm import *
import StartProcess
import N_Queen
from Knight_Tour import *
from SUDOKU import *
from Rat_In_The_Maze import *
from DFS import *
from Astar import *

class Window:
    def __init__(self,root):
        self.root = root
        self.root.geometry("300x150")
        self.root.resizable(False, False)
        self.root.title("Algorithm Visualizer")
        try:
            self.root.iconbitmap("Images/hnet.com-image.ico")
        except:
            img = PhotoImage("Images/hnet.com-image.ico")
            self.root.tk.call('wm', 'iconphoto', self.root._w, img)


        self.AlgoTypeLabel = Label(self.root, text='Select Algorithm Type:-', font=("Courier", 10))
        self.AlgoTypeLabel.pack(pady=2)

        self.AlgoTypeVar = StringVar()
        self.AlgoTypeVar.set("Select Algorithm Type")
        self.AlgoTypeList = ["Select Algorithm Type","Pathfinding Algorithm", "Backtracking Algorithm","Sorting Algorithm"]
        self.AlgoTypeDrop = OptionMenu(self.root, self.AlgoTypeVar, *self.AlgoTypeList)
        self.AlgoTypeDrop.pack(pady=10)

        self.NextButton = Button(self.root, text="Next>", command=self.SecondWindow)
        self.NextButton.pack()


    def Exit(self):
        self.root.destroy()

    def Back(self):
        self.root.destroy()
        Process = StartProcess.START()

        Process.start()

    def run(self):
        if self.AlgoNameVar.get() == "Select Algorithm Name" or self.AlgoTypeVar.get() == "Select Algorithm Type":
            messagebox.showerror("Incomplete Data!", "Please fill all the Fields to Start Visualization.")
        else:
            if self.AlgoTypeVar.get() == "Sorting Algorithm":
                self.temp1=self.NoOfElementsSlider.get()
                self.temp2=self.SpeedSlider.get()
                self.root.destroy()
                Sorting(self.temp1, self.temp2,self.AlgoNameVar.get())

            elif self.AlgoTypeVar.get() == "Backtracking Algorithm":
                self.temp1 = self.DimensionOfBoard.get()
                self.temp2 = self.SpeedSlider.get()
                self.root.destroy()
                if self.AlgoNameVar.get() == "N-Queen":
                    N_Queen.N_queen(self.temp1, self.temp2)

                if self.AlgoNameVar.get() == "Knight Tour":
                    Knight(self.temp1, self.temp2)
                
                if self.AlgoNameVar.get() == "SUDOKU":
                    Sudoku(9, self.temp2)

                if self.AlgoNameVar.get() == "Rat in the Maze":
                    Rat_in_Maze(self.temp1, self.temp2)

            elif self.AlgoTypeVar.get() == "Pathfinding Algorithm":
                self.temp1 = self.DimensionOfBoard.get()
                self.temp2 = self.SpeedSlider.get()
                self.root.destroy()
                if self.AlgoNameVar.get() == "Breadth First Search":
                    print("To Be Made")
                    pass
                    

                if self.AlgoNameVar.get() == "Depth First Search":
                    dfs(self.temp1, self.temp2)
                
                if self.AlgoNameVar.get() == "Dijkstra":
                    print("To Be Made")
                    pass

                if self.AlgoNameVar.get() == "A*(Astar)":
                    astar(self.temp1, self.temp2)
                    pass

    def SecondWindow(self):
        if self.AlgoTypeVar.get()=="Select Algorithm Type":
            messagebox.showerror("Incomplete Data!", "Please select Algorithm Type.")
        elif self.AlgoTypeVar.get() == "Sorting Algorithm":
            self.root.destroy()
            self.root=Tk()
            self.root.geometry("725x300")
            self.root.resizable(False, False)
            self.root.title(self.AlgoTypeVar.get())
            try:
                self.root.iconbitmap("Images/hnet.com-image.ico")
            except:
                img = PhotoImage("Images/hnet.com-image.ico")
                self.root.tk.call('wm', 'iconphoto', self.root._w, img)
                
            self.AlgoNameLabel = Label(self.root, text=' Select Algorithm Name:-', pady=5, font=("Courier", 10))
            self.AlgoNameLabel.grid(row=0, column=1)

            self.AlgoNameVar = StringVar()
            self.AlgoNameVar.set("Select Algorithm Name")

            self.AlgoNameList = ["Select Algorithm Name", "Bubble Sort", "Heap Sort", "Insertion Sort", "Selection Sort","Quick Sort","Shell Sort","Iterative Merge Sort","Recursive Merge Sort"]
            self.AlgoNameDrop = OptionMenu(self.root, self.AlgoNameVar, *self.AlgoNameList)
            self.AlgoNameDrop.grid(row=1, column=1)

            self.fill6 = Label(self.root, text="")
            self.fill6.grid(row=2, column=0)

            self.NoOfElementsLabel1 = Label(self.root, text="   Select Number of Elements:-", font=("Courier", 10))
            self.NoOfElementsLabel1.grid(row=3, column=0)
            self.NoOfElementsLabel2 = Label(self.root, text="(from 5 to 160)")
            self.NoOfElementsLabel2.grid(row=4, column=0)

            self.NoOfElementsSlider = Scale(self.root, from_=5, to=160, orient=HORIZONTAL, sliderlength=20, width=10)
            self.NoOfElementsSlider.grid(row=5, column=0)

            self.SpeedLabel1 = Label(self.root, text="Select Speed of Visualization:-", font=("Courier", 10))
            self.SpeedLabel1.grid(row=3, column=2)
            self.SpeedLabel2 = Label(self.root, text="(in Operations per sec.)")
            self.SpeedLabel2.grid(row=4, column=2)

            self.SpeedSlider = Scale(self.root, from_=1, to=400, orient=HORIZONTAL, sliderlength=20, width=10)
            self.SpeedSlider.grid(row=5, column=2)

            self.fill1 = Label(self.root, text="")
            self.fill1.grid(row=6, column=0)
            self.StartButton = Button(self.root, text="Start Visualization>", padx=5, command=self.run)
            self.StartButton.grid(row=7, column=1)
            self.fill2 = Label(self.root, text="")
            self.fill2.grid(row=8, column=0)


            self.BackButton = Button(self.root, text="<Back", padx=5, command=self.Back)
            self.BackButton.grid(row=9, column=1)
        #############################
            self.AlgoNameList = ["Select Algorithm Name", "Breadth First Search","Depth First Search","Dijkstra", "A*(Astar)"]
        elif self.AlgoTypeVar.get() == "Pathfinding Algorithm":
            self.root.destroy()
            self.root = Tk()
            self.root.geometry("750x300")
            self.root.resizable(False, False)
            self.root.title(self.AlgoTypeVar.get())
            try:
                self.root.iconbitmap("Images/hnet.com-image.ico")
            except:
                img = PhotoImage("Images/hnet.com-image.ico")
                self.root.tk.call('wm', 'iconphoto', self.root._w, img)


            self.AlgoNameLabel = Label(self.root, text=' Select Algorithm Name:-', pady=5, font=("Courier", 10))
            self.AlgoNameLabel.grid(row=0, column=1)

            self.AlgoNameVar = StringVar()
            self.AlgoNameVar.set("Select Algorithm Name")
            self.AlgoNameList = ["Select Algorithm Name", "Breadth First Search","Depth First Search","Dijkstra", "A*(Astar)"]
    
            self.AlgoNameDrop = OptionMenu(self.root, self.AlgoNameVar, *self.AlgoNameList)
            self.AlgoNameDrop.grid(row=1, column=1)

            self.fill6 = Label(self.root, text="")
            self.fill6.grid(row=2, column=0)

            self.NoOfElementsLabel1 = Label(self.root, text="   Select the Dimension of Board:-", font=("Courier", 10))
            self.NoOfElementsLabel1.grid(row=3, column=0)
            self.NoOfElementsLabel2 = Label(self.root, text="(from 4x4 to 50x50)")
            self.NoOfElementsLabel2.grid(row=4, column=0)

            self.DimensionOfBoard = Scale(self.root, from_=4, to=50, orient=HORIZONTAL, sliderlength=20, width=10)
            self.DimensionOfBoard.grid(row=5, column=0)
            

            self.SpeedLabel1 = Label(self.root, text="Select Speed of Visualization:-", font=("Courier", 10))
            self.SpeedLabel1.grid(row=3, column=2)
            self.SpeedLabel2 = Label(self.root, text="(in Operations per sec.)")
            self.SpeedLabel2.grid(row=4, column=2)

            self.SpeedSlider = Scale(self.root, from_=1, to=400, orient=HORIZONTAL, sliderlength=20, width=10)
            self.SpeedSlider.grid(row=5, column=2)

            self.fill1 = Label(self.root, text="")
            self.fill1.grid(row=7, column=0)
            self.StartButton = Button(self.root, text="Start Visualization>", padx=5, command=self.run)
            self.StartButton.grid(row=8, column=1)
            self.fill2 = Label(self.root, text="")
            self.fill2.grid(row=9, column=0)

            self.BackButton = Button(self.root, text="<Back", padx=5, command=self.Back)
            self.BackButton.grid(row=10, column=1)
            
        ###################
        elif self.AlgoTypeVar.get() == "Backtracking Algorithm":
            self.root.destroy()
            self.root = Tk()
            self.root.geometry("750x300")
            self.root.resizable(False, False)
            self.root.title(self.AlgoTypeVar.get())
            try:
                self.root.iconbitmap("Images/hnet.com-image.ico")
            except:
                img = PhotoImage("Images/hnet.com-image.ico")
                self.root.tk.call('wm', 'iconphoto', self.root._w, img)

    
            self.AlgoNameLabel = Label(self.root, text=' Select Algorithm Name:-', pady=5, font=("Courier", 10))
            self.AlgoNameLabel.grid(row=0, column=1)

            self.AlgoNameVar = StringVar()
            self.AlgoNameVar.set("Select Algorithm Name")
            self.AlgoNameList = ["Select Algorithm Name","Knight Tour", "N-Queen","SUDOKU","Rat in the Maze"]
            self.AlgoNameDrop = OptionMenu(self.root, self.AlgoNameVar, *self.AlgoNameList)
            self.AlgoNameDrop.grid(row=1, column=1)

            self.fill6 = Label(self.root, text="")
            self.fill6.grid(row=2, column=0)

            self.NoOfElementsLabel1 = Label(self.root, text="   Select the Dimension of Board:-", font=("Courier", 10))
            self.NoOfElementsLabel1.grid(row=3, column=0)
            self.NoOfElementsLabel2 = Label(self.root, text="(from 4x4 to 50x50)")
            self.NoOfElementsLabel2.grid(row=4, column=0)

            self.DimensionOfBoard = Scale(self.root, from_=4, to=50, orient=HORIZONTAL, sliderlength=20, width=10)
            self.DimensionOfBoard.grid(row=5, column=0)
            #######
            self.NoOfElementsLabel2 = Label(self.root, text="(Not For SUDOKU)")
            self.NoOfElementsLabel2.grid(row=6, column=0)

            self.SpeedLabel1 = Label(self.root, text="Select Speed of Visualization:-", font=("Courier", 10))
            self.SpeedLabel1.grid(row=3, column=2)
            self.SpeedLabel2 = Label(self.root, text="(in Operations per sec.)")
            self.SpeedLabel2.grid(row=4, column=2)

            self.SpeedSlider = Scale(self.root, from_=1, to=100, orient=HORIZONTAL, sliderlength=20, width=10)
            self.SpeedSlider.grid(row=5, column=2)

            self.fill1 = Label(self.root, text="")
            self.fill1.grid(row=7, column=0)
            self.StartButton = Button(self.root, text="Start Visualization>", padx=5, command=self.run)
            self.StartButton.grid(row=8, column=1)
            self.fill2 = Label(self.root, text="")
            self.fill2.grid(row=9, column=0)

            self.BackButton = Button(self.root, text="<Back", padx=5, command=self.Back)
            self.BackButton.grid(row=10, column=1)
