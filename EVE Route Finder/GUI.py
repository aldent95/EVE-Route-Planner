#!/usr/bin/python
#Allows compatibility with any version of Python by checking for both versions of Tkinter
try:
    from Tkinter import *
except ImportError:
    from tkinter import *
#Imports the AutoCompleteEntry
from AutoCompleteEntry import AutoCompleteEntry
from HelpMenu import HelpMenu
from SettingsMenu import SettingsMenu

class UI(Tk):
    def initialize(self, namesList):
        #Handles setting up most of the GUI
        w = 500;#Window width
        h = 500;#Window height
        sw = self.winfo_screenwidth();#Gets screen width
        sh = self.winfo_screenheight();#Gets screen height
        x=(sw-w)/2;#Calculates the x position for the left side of the window that allows it to be placed in the center of the screen
        y =(sh-h)/2;#Calculates the y position for the top of the window that allows it to be placed in the center of the screen
        self.update();#Forces and update on the window
        self.geometry('%dx%d+%d+%d' % (w,h,x,y));#Sets the windows width, height and position
        self.minsize(int(w),int(h/2));#Sets the minimum size of the window
        
        self.columnconfigure(0,weight=1);#Configure all used columns to automaticly resize
        self.columnconfigure(1,weight=1);
        self.columnconfigure(2,weight=1);
        self.columnconfigure(3,weight=1);
        self.rowconfigure(1,weight=1);#Configures the row uesd for the text area to automaticly resize
        
        self.title("EVE Route Finder");#Sets the title
        self.grid();#Sets the layout to use grid
        self.configureMenu();#Calls the function that configures the menus
        
        Label(self,padx=2,text="Origin").grid(row=0,column=0,sticky='E'+'W');#Setup and place the origin label
        self.origin = AutoCompleteEntry(self, namesList);#Setup the origin autocomplete entry box
        self.origin.grid(column=1,row=0,sticky='E'+'W');#Place the origin entry box
        
        Label(self,padx=2,text="Destination").grid(row=0,column=2,sticky='E'+'W');#Setup and place the Destination label
        self.des = AutoCompleteEntry(self,namesList);#Setup the destination autocomplete entry box
        self.des.grid(column=3,row=0,sticky='E'+'W');#Place the destination entry box
        
        self.output = Text(self);#Setup the text area
        self.output.grid(column=0,row=1,sticky='E'+'W'+'N'+'S',columnspan=4);#Place the text area, spanning 4 columns
        self.output.insert('end',"Output test");#Add some testing text to the text area
        self.output.configure(state='disabled');#Disable the text area
        
    def configureMenu(self):
        #Handles configuring and setting up the menus
        menu = Menu(self);#Setup the menu bar
        menu.add_command(label="Settings",command=self.displaySettings);
        menu.add_command(label="Help",command=self.displayHelp);
        self.config(menu=menu);
    def displaySettings(self):
        self.helpMenu.deiconify();
    def updateHelp(self, helpMenu):
        self.helpMenu=helpMenu;
    def displayHelp(self):
        self.helpMenu.deiconify();
    def setupButtons(self):
        #Handles creating and setting up all the buttons (Not really in use yet)
        quitButton= Button(self, text="Quit", command=self.quit)
        quitButton.place(x=0,y=0);
    def quit(self):
    #Handles quitting the program, not working yet
       return; 
    def __init__(self, parent, namesList):
    #Handles the initial call to create a GUI
       Tk.__init__(self,parent);#Parent constructor
       self.parent = parent;#Store the parent
       self.initialize(namesList);#Initilize the GUI
       self.helpMenu = HelpMenu(self, self);
       self.settingsMenu = SettingsMenu(self, self);
       self.mainloop();#Start the main loop

