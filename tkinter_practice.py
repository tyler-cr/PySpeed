import tkinter as tk

def main():
    root = tk.Tk()
    root.title("My First GUI")
    '''root.attributes("-fullscreen",True)'''
    
    root.geometry("1920x1080")
    label = tk.Label(root, text="This is a label!", font=('Impact', 18))
    label.pack(padx = 20, pady = 20)

    textbox = tk.Text(root, font=('Impact', 14))
    textbox.pack(padx = 100, pady = 100)

    buttonframe=tk.Frame(root)
    buttonframe.columnconfigure(0, weight=1)
    buttonframe.columnconfigure(1, weight=1)
    buttonframe.columnconfigure(2, weight=1)

    btn1 = tk.Button(buttonframe, text = 'Button Frame 1', font = ('Impact', 8))
    btn1.grid(row=0,column=0, sticky=tk.W+tk.E)
    btn2 = tk.Button(buttonframe, text = 'Button Frame 2', font = ('Impact', 8))
    btn2.grid(row=1,column=1, sticky=tk.W+tk.E)
    btn3 = tk.Button(buttonframe, text = 'Button Frame 3', font = ('Impact', 8))
    btn3.grid(row=2,column=2, sticky=tk.W+tk.E)
    buttonframe.pack(fill='x')

    myentry=tk.Entry(root)
    myentry.pack()

    button = tk.Button(root, text="This is a button", font = ('Impact', 14))
    button.pack(pady = 20)

    anotherbtn = tk.Button(root, text="This is a place button", font = ('Impact', 14))
    anotherbtn.place(x=200,y=200)

    root.mainloop()





if __name__ == "__main__":
    main()


