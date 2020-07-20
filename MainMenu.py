from  tkinter import *
from tkinter import messagebox
from SortingAlgorithm import *

class front:
    def __init__(self,root):
        self.root = root
        self.root.geometry("650x300")
        self.root.resizable(False, False)
        self.root.title("Algorithm Visualizer")
        self.root.iconbitmap("hnet.com-image.ico")

        self.AlgoTypeLabel = Label(self.root, text='  Select Algorithm Type:-', font=("Courier", 10))
        self.AlgoTypeLabel.grid(row=0, column=0 ,pady=15)

        self.AlgoTypeVar = StringVar()
        self.AlgoTypeVar.set("Select Algorithm Type")
        self.AlgoTypeList = ["Select Algorithm Type", "Sorting Algorithm"]
        self.AlgoTypeDrop = OptionMenu(self.root, self.AlgoTypeVar, *self.AlgoTypeList)
        self.AlgoTypeDrop.grid(row=1, column=0)

        self.AlgoNameLabel = Label(self.root, text=' Select Algorithm Name:-', font=("Courier", 10))
        self.AlgoNameLabel.grid(row=0, column=2)

        self.AlgoNameVar = StringVar()
        self.AlgoNameVar.set("Select Algorithm Name")
        self.AlgoNameList = ["Select Algorithm Name", "Bubble Sort","Heap Sort","Insertion Sort","Selection Sort"]
        self.AlgoNameDrop = OptionMenu(self.root,self.AlgoNameVar,*self.AlgoNameList)
        self.AlgoNameDrop.grid(row=1, column=2)

        self.fill6 = Label(self.root, text="")
        self.fill6.grid(row=2, column=0)

        self.NoOfElementsLabel1 = Label(self.root, text="   Select Number of Elements:-", font=("Courier", 10))
        self.NoOfElementsLabel1.grid(row=3, column=0)
        self.NoOfElementsLabel2 = Label(self.root, text="(from 5 to 160)")
        self.NoOfElementsLabel2.grid(row=4, column=0)

        self.NoOfElementsSlider = Scale(self.root, from_= 5, to = 160, orient=HORIZONTAL, sliderlength=20, width=10)
        self.NoOfElementsSlider.grid(row=5, column=0)

        self.SpeedLabel1 = Label(self.root, text="Select Speed of Visualization:-", font=("Courier", 10))
        self.SpeedLabel1.grid(row=3, column=2)
        self.SpeedLabel2 = Label(self.root, text="(in Operations per sec.)")
        self.SpeedLabel2.grid(row=4,column=2)

        self.SpeedSlider = Scale(self.root, from_ = 1, to = 400, orient=HORIZONTAL, sliderlength=20, width=10)
        self.SpeedSlider.grid(row=5, column=2)

        self.fill1 = Label(self.root, text="")
        self.fill1.grid(row=6,column=0)
        self.fill2 = Label(self.root, text="")
        self.fill2.grid(row=7,column=0)

        self.StartButton = Button(self.root, text="Start Visualization", padx=5,command=self.run)
        self.StartButton.grid(row=8,column=1)

    def run(self):
        if self.AlgoNameVar.get() == "Select Algorithm Name" or self.AlgoTypeVar.get() == "Select Algorithm Type":
            messagebox.showerror("Incomplete Data!", "Please fill all the Fields to Start Visualization.")
        else:
            if self.AlgoTypeVar.get() == "Sorting Algorithm":
                self.temp1=self.NoOfElementsSlider.get()
                self.temp2=self.SpeedSlider.get()
                self.root.destroy()
                Sorting(self.temp1, self.temp2,self.AlgoNameVar.get())