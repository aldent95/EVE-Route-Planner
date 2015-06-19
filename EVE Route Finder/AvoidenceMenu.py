#!/usr/bin/python
try:
    from Tkinter import *
except ImportError:
    from tkinter import *
import os
from AutoCompleteEntry import AutoCompleteEntry

class AvoidenceMenu(Toplevel):
    def addAvoidence(self):
        system = self.systemEntry.get()
        if system not in self.avoidList and system in self.nameList:
            avoidList.append(system)
            self.output.configure(state='normal')
            self.output.insert('end',""+system+"\n")
            self.output.configure(state='disabled')
            self.save()
        ##TODO error display
    def removeAvoidence(self):
        system = self.systemEntry.get()
        if system in self.avoidList:
            avoidList.remove(system)
            self.output.configure(state='normal')
            self.output.delete(1.0,'end')
            for sys in avoidList:
                self.output.insert('end', ""+sys+"\n")
            self.output.configure(state='disabled')
            self.save()
        #TODO error display    
    def load(self):
        lines = []
        os.chdir(os.path.dirname(__file__)+"\data")
        try:
            with open("Avoidence.txt",'r') as avoidenceFile:
                [lines.append(line.strip('\t')) for line in avoidenceFile]
        except IOError:
            return []
        self.output.configure(state='normal')
        for line in lines:
            self.output.insert('end',""+line+"\n")
            self.avoidList.append(line)
        self.output.configure(state='disabled')
    def save(self):
        file=open("Avoidence.txt",'w')
        for entry in avoidList:
            file.write(entry+"\t")
        file.close()
    def getList(self):
        return self.avoidList
    def hide(self):  # Hides the window
        self.withdraw()
    def configureOutput(self):
        self.output = Text(self)
        self.output.grid(column=0, row=2, sticky='E'+'W'+'N'+'S',columnspan=2)
        self.output.configure(state='disabled')
    def __init__(self, parent, nameList):
        Toplevel.__init__(self, parent)
        self.avoidList = []
        self.setup(nameList) 
        self.protocol("WM_DELETE_WINDOW", self.hide)  # Changes the close button to just hide the window
        self.withdraw()
    def setup(self, nameList):
        self.grid()
        self.nameList = nameList
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        w = 200  # Sets up the window position on the screen
        h = 500
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.update()
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.resizable(width=0, height=0)
        self.title("Avoidence List")
        self.configureOutput()
        Label(self,text="System:").grid(row=0,column=0,sticky='W')
        self.systemEntry = AutoCompleteEntry(self,self.nameList)
        self.systemEntry.grid(column=1,row=0,sticky='E'+'W')
        addButton = Button(self,text="Add System",command=self.addAvoidence).grid(column=0,row=1,sticky='E'+'W')
        removeButton = Button(self, text="Remove System",command=self.removeAvoidence).grid(column=1,row=1,sticky='E'+'W')        
        self.avoidList = self.load()
        self.update()


    
        


