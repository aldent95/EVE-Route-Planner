#!/usr/bin/python
try:
    from Tkinter import *
except ImportError:
    from tkinter import *
import os
from AutoCompleteEntry import AutoCompleteEntry

class WaypointsMenu(Toplevel):
    def addWaypoint(self):
        system = self.systemEntry.get()
        index = self.indexEntry.get()
        if system in self.nameList:
            if index == "":
                self.waypointList.append(system)
            else:
                self.waypointList.insert(int(index), system)
        self.systemEntry.delete(0,'end')
        self.indexEntry.delete(0,'end')
        self.rewriteList()
        ##TODO error display
    def removeWaypoint(self):
        system = self.systemEntry.get()
        index = self.indexEntry.get()
        if system in self.nameList and system in self.waypointList:
            if index == "":
                self.waypointList.remove(system)
            elif self.waypointList[int(index)] == system:
                self.waypointList.pop(int(index))
        self.systemEntry.delete(0,'end')
        self.indexEntry.delete(0,'end')
        self.rewriteList()
        #TODO error display    
    def rewriteList(self):
        self.output.configure(state='normal')
        self.output.delete(1.0,'end')
        for i in xrange(0,len(self.waypointList)):
            string = ""
            if i == 0 and i != len(self.waypointList)-1:
                string = "Start: " + self.waypointList[i]
            elif i == len(self.waypointList)-1 and i != 0:
                string = "End: " + self.waypointList[i]
            elif i == 0 and i == len(self.waypointList)-1:
                string = "Start/End: " + self.waypointList[i]
            else:
                string = str(i) + ": " + self.waypointList[i]
            self.output.insert('end',""+string+"\n")
        self.output.configure(state='disabled')
        self.parent.checkboxChanged()
    def hide(self):  # Hides the window
        self.withdraw()
    def getStart(self):
        if(len(self.waypointList) >=1):
            return self.waypointList[0]
        else:
            return ""
    def getEnd(self):
        if(len(self.waypointList) >=1):
            return self.waypointList[len(self.waypointList)-1]
        else:
            return ""
    def getList(self):
        return self.waypointList
    def configureOutput(self):
        self.output = Text(self)
        self.output.grid(column=0, row=3, sticky='E'+'W'+'N'+'S',columnspan=2)
        self.output.configure(state='disabled')
    def __init__(self, parent, nameList, ui):
        Toplevel.__init__(self, parent)
        self.parent = ui
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
        self.rowconfigure(3, weight=1)
        w = 200  # Sets up the window position on the screen
        h = 500
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.update()
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.resizable(width=0, height=0)
        self.title("Waypoint List")
        self.configureOutput()
        Label(self,text="System:").grid(row=0,column=0,sticky='W')
        self.systemEntry = AutoCompleteEntry(self,self.nameList)
        self.systemEntry.grid(column=1,row=0,sticky='E'+'W')
        Label(self,text="Index:").grid(row=1,column=0,sticky='E'+'W')
        self.indexEntry = Entry(self)
        self.indexEntry.grid(column=1,row=1,sticky='E'+'W')
        addButton = Button(self,text="Add System",command=self.addWaypoint).grid(column=0,row=2,sticky='E'+'W')
        removeButton = Button(self, text="Remove System",command=self.removeWaypoint).grid(column=1,row=2,sticky='E'+'W')        
        self.waypointList = []
        self.update()


    
        


