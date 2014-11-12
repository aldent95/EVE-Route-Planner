#!/usr/bin/python
import os
from System import System

    
#finder;
systems = [];
def __int__():
     load();
def load():
    os.chdir(os.path.dirname(sys.argv[0]));
    sysFile = open("Systems.txt", 'r');
    lines = [];
    for line in sysFile:
         lines.append(line.strip('\n'));
    print (len(lines));
    for i in range(0,len(lines)-1):
         line = lines[i].split('\t');
         tempSys = System(line[0], line[1], line[2], line[3], line[4], line[5], line[6],line[7])
         systems.append(tempSys);
    sysFile.close();
    for system in systems:
         print(system.toString());
    return
def setupGUI():
    return
def setupRouteFinder():
    return
def findRoute():
    return


if __name__ == "__main__":
    import sys
    __int__();
