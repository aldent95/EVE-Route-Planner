#!/usr/bin/python
#Allows compatibility with any version of Python by checking for both versions of Tkinter
try:
    from Tkinter import *
except ImportError:
    from tkinter import *
import re #Regex library

class AutoCompleteEntry(Entry):
    #Sets up the box and all the needed variables
    def __init__(self, parent, namesList):
        Entry.__init__(self);#Parent constructor
        self.namesList = namesList;#Store the list of word/names to search when typing into the box
        self.var = self["textvariable"];#Sets the local variable var to to textvariable of the Entry box
        if self.var == '': #If var is still empty then setup both var and self["textvariable"] to be a variable string
            self.var = self["textvariable"] = StringVar();

        self.var.trace('w', self.altered);#Setup a trace so that when var is modified it calls self.altered

        self.bind("<Up>", self.up);#Bind the up arrow to move up the list
        self.bind("<Down>", self.down);#Bind the down arrow to move down the list
        self.bind("<Return>", self.selection);#Bind the enter/return key to make a selection from the list

        self.listBox_Displayed = False;#Tracks the state of the listbox, if it is currently displayed or not

    def altered(self, name, index, mode):
    #Altered handles when there is text added or removed from the entry box
        if self.var.get() == '':#If the entry box is empty, destroy the list box
            self.listBox.destroy();
            self.listBox_Displayed = False;

        else:
            words = self.findWords(); #Finds all the words that contain the current entry box text
            if len(words) != 0:#If there are words found
                if not self.listBox_Displayed:#If the list box is not displayed
                    self.listBox = Listbox();#Create the list box
                    self.listBox.bind("<Double-Button-1>", self.selection);#Bind double left click to select from the list
                    self.listBox.bind("<Return>",self.selection);#Bind the return/enter key to make a selection from the list
                    self.listBox.place(x=self.winfo_x(), y=self.winfo_y()+self.winfo_height());#Set the list box to appear below the entry box
                    self.listBox_Displayed = True;

                self.listBox.delete(0,END);#Clear the entry box, even if it is already clear
                for w in words:#For all the found words
                    self.listBox.insert(END,w);#Add them to the list box
            else:#If there are no words found
                if self.listBox_Displayed:#And the listbox is displayed
                    self.listBox.destroy();#Destroy the listbox
                    self.listBox_Displayed = False;

    def selection(self, event):
    #Handles the transition from a selected item in the listbox to an entry in the entry box
        if self.listBox_Displayed:#If the list box is displayed
            self.var.set(self.listBox.get(ACTIVE));#Set the entry text to be what is currently selected in the listbox
            self.listBox.destroy();#Destroy the list box
            self.listBox_Displayed = False;
            self.icursor(END);#Move the cursor in the entry box to the end

    def up(self, event):
    #Handles movement up the listbox when using arrow keys
        if self.listBox_Displayed:#If the list box is displayed
            if self.listBox.curselection() == ():#If the current selection is empty
                index = '0';#Index is set to 0
            else:#Otherwise
                index = self.listBox.curselection()[0];#Index is set to the index of the current selection
            if index != '0':#If index is not already at the top
                self.listBox.selection_clear(first = index);#Clear the selection
                index = str(int(index)-1);#Move the index up one
                self.listBox.selection_set(first=index);#Set the new selection
                self.listBox.activate(index);#Activate the list box
        
    def down(self, event):
    #Handles movement down the listbox using arrow keys
        if self.listBox_Displayed:#If the list box is displayed
            if self.listBox.curselection() == ():#If the current selection is empty
                index = '0';#Index is set to 0
            else:#Otherwise
                index = self.listBox.curselection()[0];#Index is set to the index of the current selection
            if index != END:#If index is not already at the bottom
                self.listBox.selection_clear(first = index);#Clear the selection
                index = str(int(index)+1);#Move the index down one
                self.listBox.selection_set(first=index);#Set the new selection
                self.listBox.activate(index);#Activate the list box

    def findWords(self):#Handles finding the words
        pattern = re.compile('.*' + self.var.get() + '.*', re.IGNORECASE);#Setup the regex pattern for finding the word
        # .* means any amount of any character, so by having that infront and behind the text from the entry box it
        #means we can select any word that contains the entry text.
        return [w for w in self.namesList if re.match(pattern, w)];#Search through the words list to find matchs and return them
