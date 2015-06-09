import os
import sys
lib_path = os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), '..'))
sys.path.append(lib_path)
from Main import Main
from System import System
from Routes import RouteFinder
import random
import time
from GeneralError import GeneralError




def runRandomTester(main):
        runs = 10
        incons = 0
        type2Better, type1Better = 0,0
        os.chdir(os.path.dirname(__file__))
        file = open("AutoTestLog.txt", 'w')
        print("File open, running")
        for i in xrange(0,runs):
             start = main.systems[random.choice(list(main.systems.keys()))]
             end = main.systems[random.choice(list(main.systems.keys()))]
             avoidence = []
             for j in xrange(0, 100):
                     avoidence.append(main.systems[random.choice(list(main.systems.keys()))])
             while(start == end):
                 end = main.systems[random.choice(list(main.systems.keys()))]
             print(i)
             routeFinder = RouteFinder(start, end, main.systems, avoidence)
             jumps = [0,0]
             ctime = 0
             dtime = 0
             if i%2==0:
                     result1 = test1(routeFinder, file, ctime,start ,end)
                     result2 = test2(routeFinder, file, dtime,start ,end)
             else:
                    result2 = test2(routeFinder, file, dtime,start ,end)
                    result1 = test1(routeFinder,file, ctime,start ,end)
             ctime = result1[1]
             dtime = result2[1]
             jumps[0] = result1[0]
             jumps[1] = result2[0]
             file.write("\n")   
             if(dtime < ctime):
                  type2Better += 1   
             if(ctime < dtime):
                  type1Better += 1
             if(jumps[0] != jumps[1]):
                  file.write("INCONSISTENCY!!!!!!!!!!!!!!!\n\n\n\n")
                  incons+=1
        file.write("Runs: " + str(runs) + " Inconsistencys : " + str(incons) + " Type 1 Better: " + str(type1Better) + "\t Type 2 Better: " + str(type2Better) + "/" + str(runs))
        file.close()
        print("Done")

def test1(routeFinder, file, ctime,start, end):
        try:
                dtime = int(round(time.time()*1000))
                route = routeFinder.getRoute('j')
                dtime = int(round(time.time()*1000))-dtime
                file.write("Avoidence Type 1: " + start.getName() + "\t" + end.getName() + "\t" + str(len(route)-1) + "\t" + str(dtime) + "\n")
                return [route, dtime]
        except GeneralError as e:
                file.write(start.getName() + "\t" + end.getName() + "\t" + "Caught General Error / out of systems running Avoidence Type 1\n")
        except Exception as e:
                file.write(start.getName() + "\t" + end.getName() + "\t" + "Caught unknown error running Avoidence type 1\t" + str(e) + "\n")
def test2(routeFinder, file, dtime,start,end):
             try:
                  ctime = int(round(time.time()*1000))
                  route = routeFinder.getRoute('jtest')
                  ctime = int(round(time.time()*1000))-ctime
                  file.write("Avoidence Type 2: " +start.getName() + "\t" + end.getName() + "\t" + str(len(route)-1) + "\t" + str(ctime) + "\n")
                  return [route,ctime]
             except GeneralError as e:
                  file.write(start.getName() + "\t" + end.getName() + "\t" + "Caught General Error / out of systems running Avoidence Type 2\n")
             except Exception as e:
                  file.write(start.getName() + "\t" + end.getName() + "\t" + "Caught unknown error running Avoidence type 2\t" + str(e) + "\n")
        

if __name__ == "__main__":
    main = Main()
    print("Starting")
    runRandomTester(main)
    main.cleanUp()
    main = ""
