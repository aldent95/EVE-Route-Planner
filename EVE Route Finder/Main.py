import sys
import os
from System import System
from GUI import UI
from Routes import RouteFinder




class Main:
     def handleError(self, errorCode):
          print("Handle error received error code: " + str(errorCode) + " Handle error does not currently do anything")
          #Error codes
          #0: Missing directory on load
          #1: Missing file on load
          #2: Missing data on load
          #3: Corrupt data on load
     def addSys(self, line):

               tempSys = System() #Create a sys object
               try:
                    tempSys = tempSys.build(line[0], line[1], line[2], line[3], line[4], line[5], line[6],line[7])
               except IndexError:
                    self.handleError(2)
                    return "Error, System file missing data, error passed to GUI"
               except ValueError:
                    self.handleError(3)
                    return "Error, System file data corrupt, error passed to GUI"
               self.systems[line[3]] = tempSys; #Add the sys object to the systems dict, with the sys id as key
               self.nameList.append(line[0]); #Append the sys name to the name list
               self.sysNames[line[0]] = line[3]; #Add the sys name to the sysNames array, putting it in the entry corosponding to its id               
               return tempSys
          
     
     def trimSystems(self, lines):
          sysToLoad = []
          for i in xrange(0,len(lines)):
               line = lines[i].split('\t')
               try:
                    if line[2] == "A821-A" or line[2] == "J7HZ-F" or line[2] == "UUA-F4" or line[3].startswith("31"):
                         continue
                    else :
                         sysToLoad.append(line)
               except IndexError:
                    self.handleError(2)
                    return "Error, System file missing data, error passed to GUI"
          return sysToLoad
     
     def loadSystems(self, specificPath="", specificFile="Systems.txt"):
          try:
               if(specificPath == ""):
                    os.chdir(os.path.dirname(__file__)+ "\data") #Set the current directory to the correct one
               else:
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
          try:
               tempSys = self.systems[line[4]]; #Retrive the origin system
               tempSys.addadjSys(self.systems[line[5]]); #Add the adjacent system
               pos = [line[1], line[2], line[3]]; #Add the gate pos to an object
               tempSys.addGatePos(line[5], pos); #Add the gate pos to the system
          except IndexError:
               self.handleError(2)
               return "Error, Gate file missing data, error passed to GUI"
          except KeyError:
               self.handleError(3)
               return "Error, Gate file data corrupt, error passed to GUI"

     def loadGates(self, specificPath="", specificFile="Stargates.txt"):
          if(specificPath == ""):
               try:
                    os.chdir(os.path.dirname(__file__)+ "\data"); #Set the current directory to the correct one
               except WindowsError:
                    self.handleError(0)
                    return "Error, missing path, error passed to GUI"
          else:
               try:
                    os.chdir(specificPath)
               except WindowsError:
                    self.handleError(0)
                    return "Error, missing path, error passed to GUI"
          lines = []
          try:
               with open(specificFile, 'r') as gatesFile: #Open the gates file
                   [lines.append(line.strip('\n')) for line in gatesFile] #For each line in gates file append to the lines array after stripping the new line char
               gatesLoaded = len(lines)
               [self.addGate(lines[i].split('\t')) for i in xrange(0,gatesLoaded) ]
          except IOError:
               self.handleError(1)
               return "Error, missing file, error passed to GUI"

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
          try:
               oriSys = self.systems[self.sysNames[origin]] #Get the origin system
               destSys = self.systems[self.sysNames[destination]] #Get the destination system
          except KeyError:
               self.handleError(4)
               return "Error, incorrect/non-existant system, error passed to GUI"
          self.routeFinder = RouteFinder(oriSys, destSys, self.systems) #Set up the route finder **TEMP**
          #setupRouteFinder()
          try:
               route = self.routeFinder.getRoute('j') #Get the route
          except Exception:
               self.handleError(999)
               return "Error, unknown route finder error, error passed to GUI"
          return route

     def setup(self, mode):
          self.systems = {}; #Initilise the systems dict
          self.gui = ""; #Initilise the gui object
          self.nameList = [];#Initilise the name list
          self.sysNames={}#Initilise the sysNames dict
          self.routeFinder = "" #Initilise the routefinder object
          if(mode != "Unit Tests"):
               self.loadSystems(); #Load the files
               self.loadGates()
               self.setupUI(); #Setup the gui
     def cleanUp(self):
          self.systems =""
          self.gui.stop()
          self.nameList =""
          self.sysNames = ""
     def __init__(self, mode=""):
          if(mode == "Random Tester"):
               self.setup(mode)
               self.runRandomTester()
          else:
               self.setup(mode)


if __name__ == "__main__":
    main = Main("");
