#!/usr/bin/python
try:
    from Tkinter import *
except ImportError:
    from tkinter import *
import re #Regex library

class AutoCompleteEntry(Entry):
    def __init__(self, parent, namesList):
        Entry.__init__(self);
        self.namesList = namesList;
        self.var = self["textvariable"];
        if self.var == '':
            self.var = self["textvariable"] = StringVar();

        self.var.trace('w', self.altered);

        self.bind("<Up>", self.up);
        self.bind("<Down>", self.down);
        self.bind("<Return>", self.selection);

        self.listBox_Displayed = False;

    def altered(self, name, index, mode):

        if self.var.get() == '':
            self.listBox.destroy();
            self.listBox_Displayed = False;

        else:
            words = self.findWords();
            if len(words) != 0:
                if not self.listBox_Displayed:
                    self.listBox = Listbox();
                    self.listBox.bind("<Double-Button-1>", self.selection);
                    self.listBox.bind("<Return>",self.selection);
                    self.listBox.place(x=self.winfo_x(), y=self.winfo_y()+self.winfo_height());
                    self.listBox_Displayed = True;

                self.listBox.delete(0,END);
                for w in words:
                    self.listBox.insert(END,w);
            else:
                if self.listBox_Displayed:
                    self.listBox.destroy();
                    self.listBox_Displayed = False;

    def selection(self, event):

        if self.listBox_Displayed:
            self.var.set(self.listBox.get(ACTIVE));
            self.listBox.destroy();
            self.listBox_Displayed = False;
            self.icursor(END);

    def up(self, event):

        if self.listBox_Displayed:
            if self.listBox.curselection() == ():
                index = '0';
            else:
                index = self.listBox.curselection()[0];
            if index != '0':
                self.listBox.selection_clear(first = index);
                index = str(int(index)-1);
                self.listBox.selection_set(first=index);
                self.listBox.activate(index);
        
    def down(self, event):

        if self.listBox_Displayed:
            if self.listBox.curselection() == ():
                index = '0';
            else:
                index = self.listBox.curselection()[0];
            if index != END:
                self.listBox.selection_clear(first = index);
                index = str(int(index)+1);
                self.listBox.selection_set(first=index);
                self.listBox.activate(index);

    def findWords(self):
        pattern = re.compile('.*' + self.var.get() + '.*');
        return [w for w in self.namesList if re.match(pattern, w)];
