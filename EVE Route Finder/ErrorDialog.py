#!/usr/bin/python
try:
    from Tkinter import *
except ImportError:
    from tkinter import *
import sys

class ErrorDialog(Toplevel):
    def showEasterEgg(self):
        easterEgg = EasterEgg(self)
    def __init__(self, parent, errorMsg, errorCode=999, toExit=False):
        Toplevel.__init__(self, parent)
        if toExit:
            self.protocol("WM_DELETE_WINDOW", sys.exit)  # Changes the close button to just hide the window
        else:
            self.protocol("WM_DELETE_WINDOW", self.destroy)
        self.grid()
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        
        Button(self,text="An interesting problem has occured!",command=self.showEasterEgg,borderwidth=0,relief='flat').grid(column=0,row=0)
        
        Label(self,text=str(errorCode),padx=10,pady=10).grid(row=1,column=0)
        lines = errorMsg.split('\n')
        print(lines)
        for i in xrange(0,len(lines)):
            self.rowconfigure(i+2, weight=1)
            Label(self,text=lines[i],padx=5,pady=5, wraplength=290).grid(row=i+2,column=0)
        self.rowconfigure(len(lines)+1,weight=1)
        if toExit:
            exitButton = Button(self,text="Exit",command=sys.exit).grid(column=0,row=len(lines)+3)
        else:
            exitButton = Button(self,text="Close",command=self.destroy).grid(column=0,row=len(lines)+3)
        w = 300  # Sets up the window position on the screen
        #print(len(lines))
        h = 100+(30*len(lines))
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.update()
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.resizable(width=0, height=0)
        
        self.update()

class EasterEgg(Toplevel):
    def __init__(self,parent):
        Toplevel.__init__(self,parent)
        self.protocol("WM_DELETE_WINDOW", self.destroy)
        self.grid()
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)
        self.rowconfigure(1,weight=1)
        w = 200  # Sets up the window position on the screen
        h = 50
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.update()
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.resizable(width=0, height=0)
        Label(self,text="Definition of interesting:").grid()
        Label(self,text="oh God, oh God, we're all going to die").grid(row=1)

    
        


