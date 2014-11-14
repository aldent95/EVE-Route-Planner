#!/usr/bin/python
try:
    from Tkinter import *
except ImportError:
    from tkinter import *
class UI(Frame):
    def setupRoot(self):
        root = Tk();
        w = 500;
        h = 500;
        sw = root.winfo_screenwidth();
        sh = root.winfo_screenheight();
        x=(sw-w)/2;
        y =(sh-h)/2;
        root.geometry('%dx%d+%d+%d' % (w,h,x,y));
        root.title("EVE Route Finder");
        return root;
    def setupButtons(self):
        quitButton= Button(self, text="Quit", command=self.quit)
        quitButton.place(x=0,y=0);
    def quit(self):
       return; 
    def __init__(self):
       self.root = self.setupRoot();
       Frame.__init__(self, self.root);
       for r in range(3):
           for c in range(4):
               Label(self.root, text='R%s/C%s'%(r,c),
               borderwidth=1 ).grid(row=r,column=c)
       self.pack(fill=BOTH, expand=1);
       self.setupButtons();
       self.root.mainloop();  
