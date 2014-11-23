#!/usr/bin/python
try:
    from Tkinter import *
except ImportError:
    from tkinter import *
from AutoCompleteEntry import AutoCompleteEntry

class UI(Tk):
    def initialize(self, namesList):
        w = 500;
        h = 500;
        sw = self.winfo_screenwidth();
        sh = self.winfo_screenheight();
        x=(sw-w)/2;
        y =(sh-h)/2;
        self.update();
        self.geometry('%dx%d+%d+%d' % (w,h,x,y));
        self.minsize(int(w),int(h/2));
        
        self.columnconfigure(0,weight=1);
        self.columnconfigure(1,weight=1);
        self.columnconfigure(2,weight=1);
        self.columnconfigure(3,weight=1);
        self.rowconfigure(1,weight=1);
        
        self.title("EVE Route Finder");
        self.grid();
        self.configureMenu();
        
        Label(self,padx=2,text="Origin").grid(row=0,column=0,sticky='E'+'W');
        self.origin = AutoCompleteEntry(self, namesList);
        self.origin.grid(column=1,row=0,sticky='E'+'W');
        
        Label(self,padx=2,text="Destination").grid(row=0,column=2,sticky='E'+'W');
        self.des = AutoCompleteEntry(self,namesList);
        self.des.grid(column=3,row=0,sticky='E'+'W');
        
        self.output = Text(self);
        self.output.grid(column=0,row=1,sticky='E'+'W'+'N'+'S',columnspan=4);
        self.output.insert('end',"Output test");
        self.output.configure(state='disabled');
        
    def configureMenu(self):
        menu = Menu(self);
        filemenu = Menu(menu,tearoff=0);
        menu.add_cascade(label="File",menu=filemenu);
        self.config(menu=menu);
        
    def setupButtons(self):
        quitButton= Button(self, text="Quit", command=self.quit)
        quitButton.place(x=0,y=0);
    def quit(self):
       return; 
    def __init__(self, parent, namesList):
       Tk.__init__(self,parent);
       self.parent = parent;
       self.initialize(namesList);
       self.mainloop();
