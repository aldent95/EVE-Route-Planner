import unittest
import os,sys
lib_path = os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), '..'))
sys.path.append(lib_path)
from Main import Main
from Routes import RouteFinder
from GeneralError import GeneralError
from System import System
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
        self.testSysLine = lines[0].split("\t")
        self.testRoutes = []
        for i in xrange(0, len(lines)):
            if 13 <= i <= 22:
                self.testRoutes.append(lines[i].split("\t"))
        for i in xrange(0, len(self.testRoutes)):
            self.testRoutes[i][0] = self.systems[self.sysNames[self.testRoutes[i][0]]]
            self.testRoutes[i][1] = self.systems[self.sysNames[self.testRoutes[i][1]]]
    def test_PositiveInitiliseRoute(self):
        avoidence = [self.testRoutes[0][0]]
        self.testRoute = RouteFinder(self.systems[self.sysNames["Amarr"]], self.systems[self.sysNames["Jita"]], self.systems,avoidence)
        self.assertEqual(self.testRoute.mainStart, self.systems[self.sysNames["Amarr"]], "Fail: Start system not loaded/stored correctly")
        self.assertEqual(self.testRoute.mainEnd, self.systems[self.sysNames["Jita"]], "Fail: End system not loaded/stored correctly")
        self.assertEqual(self.testRoute.systems, self.systems, "Fail: Systems not loaded/stored correctly")
        self.assertEqual(self.testRoute.currentCalcs, 0, "Fail: Current Calcs not setup correctly")
        self.assertEqual(self.testRoute.avoidence, avoidence, "Fail: Avoidence list not loaded/stored correctly")
        self.testRoute = RouteFinder(self.systems[self.sysNames["Amarr"]], self.systems[self.sysNames["Jita"]], self.systems)
        self.assertEqual(self.testRoute.avoidence, [], "Fail: Avoidence not loaded correctly when none passed")
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
        with self.assertRaises(TypeError):
            self.testRoute = RouteFinder(self.systems[self.sysNames["Amarr"]], self.systems[self.sysNames["Jita"]], self.systems, "Fails")
        with self.assertRaises(GeneralError):
            self.testRoute = RouteFinder(self.systems[self.sysNames["Amarr"]], self.systems[self.sysNames["Jita"]], self.systems, ["Fails"])
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
            actualResult = len(self.testRoute.getRoute('normal'))-1
            self.assertEqual(expectedResult, actualResult, "Fail: Route length not correct, must be a fault somewhere in route generation")

    def test_Negative_get_Route(self):
        self.testRoute = RouteFinder(self.testRoutes[0][0], self.testRoutes[0][1], self.systems)
        with self.assertRaises(GeneralError):
            self.testRoute.getRoute("Fails")

    def test_Negative_build_Route(self):
        self.testRoute = RouteFinder(self.testRoutes[0][0], self.testRoutes[0][1], self.systems)
        with self.assertRaises(TypeError):
            self.testRoute.buildRoute("TEST",0,self.testRoutes[0][0])
        with self.assertRaises(TypeError):
            self.testRoute.buildRoute(self.testRoutes[0][1], 0, "TEST")
        with self.assertRaises(TypeError):
            self.testRoute.buildRoute(self.testRoutes[0][1], "Fail", self.testRoutes[0][0])

    def test_Negative_jumps_Route(self):
        self.testRoute = RouteFinder(self.testRoutes[0][0], self.testRoutes[0][1], self.systems)
        self.testSys = System()
        line = self.testSysLine
        self.testSys.build(line[0], line[1], line[2], line[3], line[4], line[5], line[6],line[7])
        with self.assertRaises(GeneralError):
            self.testRoute.jumpsRoute('normal',start=self.testSys)
        with self.assertRaises(GeneralError):
            self.testRoute.jumpsRoute('normal',end=self.testSys)
    
    def test_Positive_get_Route_Jumps_Avoidence(self):
        self.testRoute = RouteFinder(self.systems[self.sysNames["Jita"]], self.systems[self.sysNames['Amarr']], self.systems, [self.systems[self.sysNames["Perimeter"]]])
        expectedResult = 10
        actualResult = len(self.testRoute.getRoute('normal'))-1
        self.assertEqual(expectedResult, actualResult, "Fail: Route length not correct, must be a fault somewhere in route generation")

    def test_Positive_get_Route_Jumps_Safe(self):
        self.testRoute = RouteFinder(self.systems[self.sysNames["Jita"]], self.systems[self.sysNames['Hek']], self.systems, [])
        expectedResult = 19
        actualResult = len(self.testRoute.getRoute('safe'))-1
        self.assertEqual(expectedResult, actualResult, "Fail: Route length not correct, must be a fault somewhere in route generation")
    def test_Positive_get_Route_Jumps_LessSafe(self):
        self.testRoute = RouteFinder(self.systems[self.sysNames["6-CZ49"]], self.systems[self.sysNames['Dodixie']], self.systems, [])
        expectedResult = 16
        actualResult = self.testRoute.getRoute('lessSafe')

        for sys in actualResult:
            print sys.getName()
        print len(actualResult)-1
        print self.systems[self.sysNames["Reblier"]].getSecurity()
        self.assertEqual(expectedResult, len(actualResult)-1, "Fail: Route length not correct, must be a fault somewhere in route generation")
                    
