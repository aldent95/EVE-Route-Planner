import unittest
import os,sys
lib_path = os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), '..'))
sys.path.append(lib_path)
from Main import Main
from Routes import RouteFinder
from GeneralError import GeneralError
import math

class TestRouteMethods(unittest.TestCase):
    def setUp(self):
        main = Main("Unit Tests")
        main.loadSystems()
        main.loadGates()
        self.systems = main.systems
        self.sysNames = main.sysNames
        lines = []        
        path = os.path.dirname(__file__)
        os.chdir(path)
        fileName= "TestData.txt"
        with open(fileName, 'r') as testFile:
            for line in testFile:
                lines.append(line.strip("\n"))
        testFile.close()
        self.testRoutes = []
        for i in xrange(0, len(lines)):
            if 13 <= i <= 22:
                self.testRoutes.append(lines[i].split("\t"))
        for i in xrange(0, len(self.testRoutes)):
            self.testRoutes[i][0] = self.systems[self.sysNames[self.testRoutes[i][0]]]
            self.testRoutes[i][1] = self.systems[self.sysNames[self.testRoutes[i][1]]]
    def test_PositiveInitiliseRoute(self):
        self.testRoute = RouteFinder(self.systems[self.sysNames["Amarr"]], self.systems[self.sysNames["Jita"]], self.systems)
        self.assertEqual(self.testRoute.mainStart, self.systems[self.sysNames["Amarr"]], "Fail: Start system not loaded/stored correctly")
        self.assertEqual(self.testRoute.mainEnd, self.systems[self.sysNames["Jita"]], "Fail: End system not loaded/stored correctly")
        self.assertEqual(self.testRoute.systems, self.systems, "Fail: Systems not loaded/stored correctly")
        self.assertEqual(self.testRoute.currentCalcs, 0, "Fail: Current Calcs not setup correctly")
    def test_NegativeInitiliseRoute(self):
        line= self.testRoutes
        fails4= {}
        with self.assertRaises(TypeError):
            self.testRoute = RouteFinder("Fails1", self.systems[self.sysNames["Jita"]], self.systems)
        with self.assertRaises(TypeError):
            self.testRoute = RouteFinder(self.systems[self.sysNames["Amarr"]], "Fails2", self.systems)
        with self.assertRaises(TypeError):
            self.testRoute = RouteFinder(self.systems[self.sysNames["Amarr"]], self.systems[self.sysNames["Jita"]], "Fails3")
        with self.assertRaises(IndexError):
            self.testRoute = RouteFinder(self.systems[self.sysNames["Amarr"]], self.systems[self.sysNames["Jita"]], fails4)
    def test_Positive_get_Sys(self):
        self.testRoute = RouteFinder(self.systems[self.sysNames["Amarr"]], self.systems[self.sysNames["Jita"]], self.systems)
        expectedResult = self.systems[self.sysNames["Tanoo"]]
        actualResult = self.testRoute.getSys("30000001")
        self.assertEqual(expectedResult, actualResult, "Fail: Did not return correct System")
    def test_Negative_get_Sys(self):
        self.testRoute = RouteFinder(self.systems[self.sysNames["Amarr"]], self.systems[self.sysNames["Jita"]], self.systems)
        with self.assertRaises(KeyError):
            self.testRoute.getSys("301")
    def test_Positive_get_Adj(self):
        self.testRoute = RouteFinder(self.systems[self.sysNames["Amarr"]], self.systems[self.sysNames["Jita"]], self.systems)
        sys = self.systems[self.sysNames["Tanoo"]]
        expectedResult = sys.getadjSyss()
        actualResult = self.testRoute.getAdj(sys)
        self.assertEqual(expectedResult, actualResult, "Fail: getAdj not fetching the correct adj sys list")
    def test_Negative_get_Adj(self):
        self.testRoute = RouteFinder(self.systems[self.sysNames["Amarr"]], self.systems[self.sysNames["Jita"]], self.systems)
        with self.assertRaises(TypeError):
            self.testRoute.getAdj("Fails")
    def test_Positive_get_Route_Jumps(self):
        for i in xrange(0,len(self.testRoutes)):
            self.testRoute = RouteFinder(self.testRoutes[i][0], self.testRoutes[i][1], self.systems)
            expectedResult = int(self.testRoutes[i][2])
            actualResult = len(self.testRoute.getRoute('j'))-1
            self.assertEqual(expectedResult, actualResult, "Fail: Route length not correct, must be a fault somewhere in route generation")

    def test_Negative_get_Route(self):
        self.testRoute = RouteFinder(self.testRoutes[0][0], self.testRoutes[0][1], self.systems)
        with self.assertRaises(GeneralError):
            self.testRoute.getRoute("Fails")
    
    
    
