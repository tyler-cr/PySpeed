import tkinter as tk
from PIL import ImageTK, Image


class MyGui:

    def __init__(self):
        self.root = tk.Tk()
        self.gauge = PIL.ImageTK.PhotoImage(Image.open("./Images./gauge.png"))
        self.my_label = tk.Label(image=self.gauge)
        self.my_label.pack()

MyGui()

