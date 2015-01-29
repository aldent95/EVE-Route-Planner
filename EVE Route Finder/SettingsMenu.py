#!/usr/bin/python
try:
    from Tkinter import *
except ImportError:
    from tkinter import *

class SettingsMenu(Toplevel):
   def __init__(self, parent, observer):
        Toplevel.__init__(self);
        self.observer = observer;
        self.setup();
        self.withdraw();
        self.protocol('WM_DELETE_WINDOW', self.quit());
    
   def setup(self):
       self.columnconfigure(0,weight=1);
       w = 250;
       h = 150;
       sw = self.winfo_screenwidth();
       sh = self.winfo_screenheight();
       x=(sw-w)/2;
       y =(sh-h)/2;
       self.update();
       self.geometry('%dx%d+%d+%d' % (w,h,x,y));
       self.resizable(width=0, height=0);
       lines = self.load();
       self.grid();
       self.title("Help for EVE Route Finder V1.0");
       for i in range(0, 10):
           Label(self,pady=5,text=lines[i]).grid(row=i,column=0,sticky='E'+'W');
        
   def quit(self):
       self.withdraw();
   def load(self):
       lines = [];
       with open("Systems.txt", 'r') as sysFile:
            for line in sysFile:
                 lines.append(line.strip('\n'));
       return lines;
