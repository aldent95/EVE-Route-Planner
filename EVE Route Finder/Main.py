import sys
import os
from System import System
from GUI import UI
from Routes import RouteFinder
import random
import time



class Main:
     def handleError(self, errorCode):
          print("Handle error received error code: " + str(errorCode) + " Handle error does not currently do anything")
     def addSys(self, line):
          tempSys = System(line[0], line[1], line[2], line[3], line[4], line[5], line[6],line[7]) #Create a sys object

          self.systems[line[3]] = tempSys; #Add the sys object to the systems dict, with the sys id as key

          self.nameList.append(line[0]); #Append the sys name to the name list

          self.sysNames[line[0]] = line[3]; #Add the sys name to the sysNames array, putting it in the entry corosponding to its id

          return tempSys
     
     def trimSystems(self, lines):
          sysToLoad = []
          for i in xrange(0,len(lines)):
               line = lines[i].split('\t')
               if line[2] == "A821-A" or line[2] == "J7HZ-F" or line[2] == "UUA-F4" or line[3].startswith("31"):
                    continue
               else :
                    sysToLoad.append(line)
          return sysToLoad
     
     def loadSystems(self, specificPath="", specificFile="Systems.txt"):
          if(specificPath == ""):
               os.chdir(os.path.dirname(__file__)+ "\data"); #Set the current directory to the correct one
          else:
               try:
                    os.chdir(specificPath)
               except WindowsError:
                    self.handleError(0)
                    return "Error, missing path, error passed to GUI"
          lines = []; #Set up the lines array
          try:
               with open(specificFile, 'r') as sysFile: #Open the systems file
                    [lines.append(line.strip('\n')) for line in sysFile] #For each line in the file Append the line to the array after stripping the new line char
          except IOError:
               self.handleError(1)
               return "Error, missing file, error passed to GUI"
          sysFile.close(); #Close the file

          sysLoaded = len(lines)

          sysToLoad = self.trimSystems(lines)
          [self.addSys(sysToLoad[i]) for i in xrange(0,len(sysToLoad))]

          self.nameList= sorted(self.nameList); #Sort the name list

          return sysLoaded

     def addGate(self, line):

          tempSys = self.systems[line[4]]; #Retrive the origin system
          tempSys.addadjSys(line[5]); #Add the adjacent system
          pos = [line[1], line[2], line[3]]; #Add the gate pos to an object
          tempSys.addGatePos(line[5], pos); #Add the gate pos to the system

     def loadGates(self):
          lines = []
          with open("Stargates.txt", 'r') as gatesFile: #Open the gates file
              [lines.append(line.strip('\n')) for line in gatesFile] #For each line in gates file append to the lines array after stripping the new line char
          gatesLoaded = len(lines)
          [self.addGate(lines[i].split('\t')) for i in xrange(0,gatesLoaded) ]

          return gatesLoaded


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
          route = self.routeFinder.getRoute('j') #Get the route
          return route
     
     def runRandomTester(self):
          runs = 10
          incons = 0
          better = 0
          file = ""
          file = open("AutoTestLog.txt", 'w')
          for i in xrange(0,runs):
               start = self.systems[random.choice(list(self.systems.keys()))]
               end = self.systems[random.choice(list(self.systems.keys()))]
               while(start == end):
                   end = self.systems[random.choice(list(self.systems.keys()))]
               print(i)
               routeFinder = RouteFinder(start, end, self.systems)
               jumps = [0,0]
               ctime, dtime = 0,0
               try:
                    ctime = int(round(time.time()*1000))
                    route = routeFinder.getRoute('dl')
                    ctime = int(round(time.time()*1000))-ctime
                    jumps[0] = len(route)-1
                    file.write(start.getName() + "\t" + end.getName() + "\t" + str(len(route)-1) + "\t" + str(ctime) + "\n")
               except TypeError as e:
                    file.write(start.getName() + "\t" + end.getName() + "\t" + "Caught type error running A*")
               try:
                    dtime = int(round(time.time()*1000))
                    route = routeFinder.getRoute('j')
                    dtime = int(round(time.time()*1000))-dtime
                    jumps[1] = len(route)-1
                    file.write(start.getName() + "\t" + end.getName() + "\t" + str(len(route)-1) + "\t" + str(dtime) + "\n\n")
               except TypeError as e:
                    file.write(start.getName() + "\t" + end.getName() + "\t" + "Caught type error running breadth")
               if(dtime < ctime or (ctime == 0 and dtime > 0)):
                    better += 1
               if(jumps[0] != jumps[1]):
                    file.write("INCONSISTENCY!!!!!!!!!!!!!!!\n\n\n\n")
                    incons+=1
          file.write("Runs: " + str(runs) + " Inconsistencys : " + str(incons) + " Breadth first better time: " + str(better) + "/" + str(runs))
          file.close()
          print("Done")
          
     def setup(self,mode):
          self.systems = {}; #Initilise the systems dict
          self.gui = ""; #Initilise the gui object
          self.nameList = [];#Initilise the name list
          self.sysNames={}#Initilise the sysNames dict
          self.routeFinder = "" #Initilise the routefinder object
          if(mode != "Unit Tests"):
               self.loadSystems(); #Load the files
               self.loadGates()
               self.setupUI(); #Setup the gui
          
     def __init__(self, mode):
          if(mode == "Random Tester"):
               self.setup()
               self.runRandomTester()
          else:
               self.setup(mode)


if __name__ == "__main__":
    main = Main("");
