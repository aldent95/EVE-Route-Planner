#!/usr/bin/python
import os

    
#finder;
systems = [];
def __int__():
     load();
def load():
    os.chdir(os.path.dirname(sys.argv[0]));
    os.chdir(os.path.join(os.getcwd(), "..", "File Converter", "src", "files"));
    temp = os.getcwd();
    print (temp);
    sysFile = open("Systems.txt", 'r', 1);
    temp = [x.strip('\n') for x in sysFile.readlines()];
    sysFile.close();
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
