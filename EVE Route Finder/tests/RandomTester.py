import os
import sys
lib_path = os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), '..'))
sys.path.append(lib_path)
from Main import Main
from System import System
from Routes import RouteFinder
import random
import time

def runRandomTester(main):
        os.chdir(os.path.dirname(__file__))
        runs = 10
        incons = 0
        better = 0
        file = ""
        file = open("AutoTestLog.txt", 'w')
        print("File open, running")
        for i in xrange(0,runs):
             start = main.systems[random.choice(list(main.systems.keys()))]
             end = main.systems[random.choice(list(main.systems.keys()))]
             while(start == end):
                 end = main.systems[random.choice(list(main.systems.keys()))]
             print(i)
             routeFinder = RouteFinder(start, end, main.systems)
             jumps = [0,0]
             ctime, dtime = 0,0
             try:
                  ctime = int(round(time.time()*1000))
                  route = routeFinder.getRoute('j')
                  ctime = int(round(time.time()*1000))-ctime
                  jumps[0] = len(route)-1
                  file.write(start.getName() + "\t" + end.getName() + "\t" + str(len(route)-1) + "\t" + str(ctime) + "\n")
             except TypeError as e:
                  file.write(start.getName() + "\t" + end.getName() + "\t" + "Caught type error running A*\n")
             try:
                  dtime = int(round(time.time()*1000))
                  route = routeFinder.getRoute('j')
                  dtime = int(round(time.time()*1000))-dtime
                  jumps[1] = len(route)-1
                  file.write(start.getName() + "\t" + end.getName() + "\t" + str(len(route)-1) + "\t" + str(dtime) + "\n\n")
             except TypeError as e:
                  file.write(start.getName() + "\t" + end.getName() + "\t" + "Caught type error running breadth\n\n")
             if(dtime < ctime or (ctime == 0 and dtime > 0)):
                  better += 1
             if(jumps[0] != jumps[1]):
                  file.write("INCONSISTENCY!!!!!!!!!!!!!!!\n\n\n\n")
                  incons+=1
        file.write("Runs: " + str(runs) + " Inconsistencys : " + str(incons) + " Breadth first better time: " + str(better) + "/" + str(runs))
        file.close()
        print("Done")


if __name__ == "__main__":
    main = Main()
    print("Starting")
    runRandomTester(main)
