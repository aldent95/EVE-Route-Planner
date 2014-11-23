#!/usr/bin/python
import os
from System import System
from GUI import UI

    
#finder;

class Main:
     def load(self):
         os.chdir(os.path.dirname(sys.argv[0]));
         lines = [];
         with open("Systems.txt", 'r') as sysFile:
              for line in sysFile:
                   lines.append(line.strip('\n'));
         print (len(lines));
         for i in range(0,len(lines)-1):
              line = lines[i].split('\t');
              tempSys = System(line[0], line[1], line[2], line[3], line[4], line[5], line[6],line[7])
              self.systems[line[3]] = tempSys;
              self.nameList.append(line[0]);
         sysFile.close();
         self.nameList= sorted(self.nameList);
         lines = [];
         with open("Stargates.txt", 'r') as gatesFile:
              for line in gatesFile:
                   lines.append(line.strip('\n'))
         for i in range(0,len(lines)-1):
              line = lines[i].split('\t');
              tempSys = self.systems[line[4]];
              tempSys.addExit(line[5]);
              pos = [line[1], line[2], line[3]];
              tempSys.addGatePos(line[5], pos);
         return
     def setupGUI(self):
         self.gui = UI(None, self.nameList); 
         return
     def setupRouteFinder(self):
         return
     def findRoute(self):
         return
     def __init__(self):
          self.systems = {};
          self.gui = "";
          self.nameList = [];
          
          self.load();
          self.setupGUI();
          

if __name__ == "__main__":
    import sys
    main = Main();
