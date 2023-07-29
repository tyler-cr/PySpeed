import tkinter as tk
from tkinter import messagebox

class MyGui:

    def __init__(self):

        #inits the root window for gui
        self.root=tk.Tk()

        #sets menu stuff
        self.menubar = tk.Menu(self.root)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Close", command=self.on_closing)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Close Without Question", command=exit)
        self.actionmenu = tk.Menu(self.menubar, tearoff=0)
        self.actionmenu.add_command(label = "show message", command=self.show_message)
        self.menubar.add_cascade(menu=self.filemenu, label="File")
        self.menubar.add_cascade(menu=self.actionmenu, label="Actions")
        self.root.config(menu=self.menubar)

        #Basically title text
        self.label = tk.Label(self.root, text="Your Message")
        self.label.pack(padx=10, pady=10)

        #What ever user puts in
        self.textbox = tk.Text(self.root)
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack(padx=10, pady=10)

        #a checkbox
        self.check_state = tk.IntVar()
        self.check = tk.Checkbutton(self.root, text = "This is a check!", variable=self.check_state)
        self.check.pack(padx = 10, pady = 10)

        #a button that shows a message
        self.button = tk.Button(self.root, text = "This is a button!", command=self.show_message)
        self.button.pack()

        #a button that clears things
        self.clearbutton = tk.Button(self.root, text = "This button clears!", command = self.clear)
        self.clearbutton.pack(padx=10,pady=10)

        #gives window when closing
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    #function that either prints user input to  
    def show_message(self):
        if self.check_state.get() == 0:
            print(self.textbox.get('1.0', tk.END))
        else:
            messagebox.showinfo(title= "This is a messagebox", message=self.textbox.get('1.0', tk.END))

    #Prints to terminal key presses
    def shortcut(self, event):
        print(event)

    #how closing window is handled
    def on_closing(self):
        if messagebox.askyesno(title = "Quit", message="Would you like to quit?"):
            print("Goodbye World")
            self.root.destroy()

    #for clear button
    def clear(self):
        self.textbox.delete('1.0', tk.END)

MyGui()