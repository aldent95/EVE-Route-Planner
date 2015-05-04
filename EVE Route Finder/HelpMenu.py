#!/usr/bin/python
try:
    from Tkinter import *
except ImportError:
    from tkinter import *

class HelpMenu(Toplevel):
    def hide(self):  # Hides the window
        self.withdraw()
    def __init__(self, parent):
        Toplevel.__init__(self, parent)
        self.setup() 
        self.protocol("WM_DELETE_WINDOW", self.hide)  # Changes the close button to just hide the window
        self.withdraw()
    def setup(self):
        self.columnconfigure(0, weight=1)
        lines = []
        with open("Help.txt", 'r') as helpFile:
            for line in helpFile:
                lines.append(line.strip('\n'))
        for i in range(0,len(lines)):
            self.rowconfigure(i, weight=1)
            Label(self, padx=10, text=lines[i], wraplength=480).grid(row=i, column=0, sticky='E'+'W')
        helpFile.close()
        w = 500  # Sets up the window position on the screen
        h = 200
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.update()
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.resizable(width=0, height=0)
        self.grid()
        self.title("Help Menu")
        


