#!/usr/bin/python
import os
from System import System
from GUI import UI
from Routes import RouteFinder
import random
    
#finder;

class Main:
     def load(self):
         os.chdir(os.path.dirname(sys.argv[0])); #Set the current directory to the correct one
         lines = []; #Set up the lines array
         with open("Systems.txt", 'r') as sysFile: #Open the systems file
              for line in sysFile: #For each line in the file
                   lines.append(line.strip('\n'));#Append the line to the array after stripping the new line char
         for i in range(0,len(lines)): #For each entry in the array
              line = lines[i].split('\t'); #Split by tabs
              tempSys = System(line[0], line[1], line[2], line[3], line[4], line[5], line[6],line[7]) #Create a sys object
              self.systems[line[3]] = tempSys; #Add the sys object to the systems dict, with the sys id as key
              self.nameList.append(line[0]); #Append the sys name to the name list
              self.sysNames[line[0]] = line[3]; #Add the sys name to the sysNames array, putting it in the entry corosponding to its id
         sysFile.close(); #Close the file
         self.nameList= sorted(self.nameList); #Sort the name list
         lines = []; #Clear the lines array
         with open("Stargates.txt", 'r') as gatesFile: #Open the gates file
              for line in gatesFile: #For each line in gates file
                   lines.append(line.strip('\n')) #Append to the lines array after stripping the new line char
         for i in range(0,len(lines)): #For each entry in the array
              line = lines[i].split('\t'); #Split by tabs
              tempSys = self.systems[line[4]]; #Retrive the origin system
              tempSys.addadjSys(line[5]); #Add the adjacent system
              pos = [line[1], line[2], line[3]]; #Add the gate pos to an object
              tempSys.addGatePos(line[5], pos); #Add the gate pos to the system
         return
     def setupUI(self):
         self.gui = UI(None, self.nameList, self); #Set up the GUI, pass it the names list and the main object
         return
     def setupRouteFinder(self):
         #Get route type setting from UI
          #Get ship settings
          #Get Security filter setting
          #Get avoidance list
          #Get specific security status filtering
          #Get Sov setting
          #Generate route finder based on settings
          self.routeFinder = RouteFinder() #Setup the route finder
     def findRoute(self, origin, destination):
          oriSys = self.systems[self.sysNames[origin]] #Get the origin system
          destSys = self.systems[self.sysNames[destination]] #Get the destination system
          self.routeFinder = RouteFinder(oriSys, destSys, self.systems) #Set up the route finder **TEMP**
          #setupRouteFinder()
          route = self.routeFinder.getRoute('dl') #Get the route
          return route
     def runRandomTester(self):
          runs = 10
          for i in range(0,10):
               start = self.systems[random.choice(list(self.systems.keys()))]
               end = self.systems[random.choice(list(self.systems.keys()))]
               while(start == end):
                   end = random.choice(list(self.systems.keys()))
               print(start.getName() + "\t" + end.getName())
     def __init__(self):
          self.systems = {}; #Initilise the systems dict
          self.gui = ""; #Initilise the gui object
          self.nameList = [];#Initilise the name list
          self.sysNames={}#Initilise the sysNames dict
          self.routeFinder = "" #Initilise the routefinder object
          self.load(); #Load the files
          self.setupUI(); #Setup the gui
          self.runRandomTester()

if __name__ == "__main__":
    import sys
    main = Main();
