import tkinter as tk
import maths
from DATA import *


class MyGui:

    def __init__(self):

        self.average_speed = AVERAGE_SPEED
        self.fastest_speed = FASTEST_SPEED
        self.current_speed = CURRENT_SPEED

        self.root = tk.Tk()
        self.root.attributes("-fullscreen",True)
        
        self.maxspeed = tk.Label(self.root, text="Max: "+ str(self.average_speed), fg="red")
        self.maxspeed.grid(row=0, column=0,)

        self.currspeed = tk.Label(self.root, text="Curr: "+str(self.fastest_speed), fg="red")
        self.currspeed.grid(row=1, column=0, sticky=tk.W+tk.E)

        self.avgspeed = tk.Label(self.root, text="Avg: "+str(self.current_speed), fg="red")
        self.avgspeed.grid(row=2, column=0, sticky=tk.W+tk.E)

        self.resetbutton = tk.Button(self.root, text="reset", command=self.reset)
        self.resetbutton.grid(row=3, column=0)

        self.root.mainloop()

    def reset(self):
        self.average_speed = 0
        self.fastest_speed = 0
        self.current_speed = 0
        self.maxspeed.config(text="Max: "+str(self.fastest_speed))
        self.currspeed.config(text="Curr: "+str(self.current_speed))
        self.avgspeed.config(text="Avg: "+str(self.average_speed))
        
        

MyGui()

