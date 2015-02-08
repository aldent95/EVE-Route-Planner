#!/usr/bin/python
import os
from System import System
from GUI import UI
from JumpsRoute import JumpsRoute
    
#finder;

class Main:
     def load(self):
         os.chdir(os.path.dirname(sys.argv[0]));
         lines = [];
         with open("Systems.txt", 'r') as sysFile:
              for line in sysFile:
                   lines.append(line.strip('\n'));
         for i in range(0,len(lines)-1):
              line = lines[i].split('\t');
              tempSys = System(line[0], line[1], line[2], line[3], line[4], line[5], line[6],line[7])
              self.systems[line[3]] = tempSys;
              self.nameList.append(line[0]);
              self.sysNames[line[0]] = line[3];
         sysFile.close();
         self.nameList= sorted(self.nameList);
         lines = [];
         with open("Stargates.txt", 'r') as gatesFile:
              for line in gatesFile:
                   lines.append(line.strip('\n'))
         for i in range(0,len(lines)):
              line = lines[i].split('\t');
              tempSys = self.systems[line[4]];
              tempSys.addadjSys(line[5]);
              pos = [line[1], line[2], line[3]];
              tempSys.addGatePos(line[5], pos);
         return
     def setupUI(self):
         self.gui = UI(None, self.nameList, self); 
         return
     def setupRouteFinder(self):
         #Get route type setting from UI
          #Get ship settings
          #Get Security filter setting
          #Get avoidance list
          #Get specific security status filtering
          #Get Sov setting
          #Generate route finder based on settings
          self.routeFinder = JumpsRoute()
     def findRoute(self, origin, destination):
          oriSys = self.systems[self.sysNames[origin]]
          destSys = self.systems[self.sysNames[destination]]
          self.routeFinder = JumpsRoute(oriSys, destSys, self.systems)
          jumpsRoute = self.routeFinder.getRoute()
          #setupRouteFinder()
          return jumpsRoute
     def __init__(self):
          self.systems = {};
          self.gui = "";
          self.nameList = [];
          self.sysNames={}
          self.routeFinder = ""
          self.load();
          self.setupUI();
          

if __name__ == "__main__":
    import sys
    main = Main();
