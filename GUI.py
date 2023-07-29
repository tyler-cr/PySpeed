import tkinter as tk
import maths
import DATA


class MyGui:

    def __init__(self):
        self.root = tk.Tk()
        self.root.attributes("-fullscreen",True)
        
        self.maxspeed = tk.Label(self.root, text="Max:", fg="red")
        self.maxspeed.grid(row=0, column=0,)

        self.currspeed = tk.Label(self.root, text="Curr:", fg="red")
        self.currspeed.grid(row=1, column=0, sticky=tk.W+tk.E)

        self.avgspeed = tk.Label(self.root, text="Avg:", fg="red")
        self.avgspeed.grid(row=2, column=0, sticky=tk.W+tk.E)

        self.root.mainloop()

MyGui()

