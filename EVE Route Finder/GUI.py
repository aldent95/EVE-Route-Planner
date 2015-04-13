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
import webbrowser

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
        self.columnconfigure(4,weight=1);
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

        self.configureOutput()
        self.setupButtons();
    def configureOutput(self):
        self.output = Text(self);#Setup the text area
        self.output.grid(column=0,row=1,sticky='E'+'W'+'N'+'S',columnspan=5);#Place the text area, spanning 4 columns
        self.output.insert('end',"Output\n test\n");#Add some testing text to the text area
        self.output.configure(state='disabled');#Disable the text area

        self.output.tag_config("a", foreground="blue", underline=1)
        self.output.tag_bind("a", "<Button-1>", self.showLink)
    def showLink(self, event):
        webbrowser.open(self.dotlanURL)
    def configureMenu(self):
        #Handles configuring and setting up the menus
        menu = Menu(self);#Setup the menu bar
        menu.add_command(label="Settings",command=self.displaySettings);
        menu.add_command(label="Help",command=self.displayHelp);
        self.config(menu=menu);
    def displaySettings(self):
        self.settingsMenu.deiconify();
    def displayHelp(self):
        self.helpMenu.deiconify();
    def setupButtons(self):
        #Handles creating and setting up all the buttons
        calculateButton= Button(self, text="Calculate", command=self.getRoute)
        calculateButton.grid(column=4,row=0,sticky='E'+'W')
    def getRoute(self,debug=False):
        systems = ""
        if(debug):
            systems = self.observer.findRoute("1DH-SX","Santola")
        else:
            systems = self.observer.findRoute(self.origin.get(),self.des.get())
        self.dotlanURL = buildDotlan(systems)
        jumps = len(systems)-1
        distance = 0
        for i in range(0,len(systems)):
            if(i==0 or i==len(systems)-1):
               continue
            else:
               distance = distance + systems[i].getGateDistance(systems[i-1].getID(),systems[i+1].getID());
        distance = round(distance, 2)
        self.output.configure(state='normal')
        self.output.delete(1.0,'end');
        self.output.insert('end', "Route information\n Total Jumps: " + str(jumps) + " Total warp distance: " + str(distance))
        self.output.insert('end', "\n Dotlan link click ")
        self.output.insert('end', "here", "a")
        self.output.insert('end', "\n")
        count = 0
        routeString = ""
        for j in range(0,len(systems)):
            if(j != len(systems)-1):
                routeString += systems[j].getName() + " --> "
            else:
                routeString += systems[j].getName()
            count+=1
            if(count == 5):
                count = 0
                self.output.insert('end', routeString + "\n")
                routeString =""
        if(count > 0):
            self.output.insert('end', routeString + "\n")
        self.output.configure(state='disabled')
    def __init__(self, parent, namesList, observer):
    #Handles the initial call to create a GUI
       Tk.__init__(self,parent);#Parent constructor
       self.parent = parent;#Store the parent
       self.initialize(namesList);#Initilize the GUI
       self.helpMenu = HelpMenu(self);
       self.settingsMenu = SettingsMenu(self);
       #Set up the observe so that we can tell it when we want a route
       self.observer = observer
       self.dotlanURL = "evemaps.dotlan.net"
       #self.getRoute(True)
       #self.mainloop();#Start the main loop

def buildDotlan(systems):
    url = "evemaps.dotlan.net/route/"
    print(len(systems))
    for i in range(0,len(systems)):
        if(i != len(systems)):
            name = systems[i].getName()
            name = name.replace(" ", "_")
            url+=name + ":"
        else:
            name = systems[i].getName()
            name = name.replace(" ", "_")
            url+=name
    print(url)
    return url
