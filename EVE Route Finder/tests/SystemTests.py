import unittest
import os,sys
lib_path = os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), '..'))
sys.path.append(lib_path)
from Main import Main
from System import System
from GeneralError import GeneralError
import math

class TestSystemMethods(unittest.TestCase):
    def setUp(self):
        self.main = Main("Unit Tests")
        lines = []        
        path = os.path.dirname(__file__)
        os.chdir(path)
        fileName= "TestData.txt"
        with open(fileName, 'r') as testFile:
            for line in testFile:
                lines.append(line.strip("\n"))
        testFile.close()
        self.correctSysLine = lines[0].split("\t")
        self.corruptMissingDataSysLine = lines[1].split("\t")
        self.corruptWrongDataSysLine = lines[2].split("\t")
        self.correctGateData = [lines[23].split("\t"), lines[24].split("\t"), lines[25].split("\t")]
        self.corruptMissingGateData = lines[26].split("\t")
        self.corruptWrongGateData = lines[27].split("\t")
        self.secondSys = lines[28].split("\t")
        self.distances = lines[29].split("\t")
                  
    def tearDown(self):
        self.main = ""
        
    def test_PositiveBuildSys(self):
        line = self.correctSysLine
        testSys = System()
        testSys.build(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7])
        self.assertTrue(isinstance(testSys, System), "Fail: test system is not an instance of system")
        self.assertEqual(line[0], testSys.getName(), "Fail: test system name not correct")
        self.assertEqual(line[1], testSys.getConstellation(), "Fail: test system constellation not correct")
        self.assertEqual(line[2], testSys.getRegion(), "Fail: test system region not correct")
        self.assertEqual(line[3], testSys.getID(), "Fail: test system ID not correct")
        self.assertEqual(convert(line[4], 1), testSys.getPOS()[0], "Fail: test system PosX not correct")
        self.assertEqual(convert(line[5], 1), testSys.getPOS()[1], "Fail: test system PosY not correct")
        self.assertEqual(convert(line[6], 1), testSys.getPOS()[2], "Fail: test system PosZ not correct")
        self.assertEqual(line[7], testSys.getSecurity(), "Fail: test system Security not correct")

    def test_NegativeBuildSys(self):
        line = self.corruptMissingDataSysLine
        testSys = System()
        with self.assertRaises(TypeError):
            testSys.build(line[0], line[1], line[2], line[3], line[4], line[5], line[6])
        line = self.corruptWrongDataSysLine
        with self.assertRaises(ValueError):
            testSys.build(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7])
        with self.assertRaises(ValueError):
            testSys.build(line[0], line[1], line[2], line[3], "Ten", line[5], line[6], line[7])
    
    def test_PositiveaddAdjSysandgetAdjSys(self):
        self.main.loadSystems()
        line = self.correctSysLine
        testSys = System()
        testSys.build(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7])
        testID = self.correctGateData[0][5]
        testSys.addadjSys(self.main.systems[testID])
        self.assertEqual(self.main.systems[testID],testSys.getadjSys(testID),"Fail: adjacent system not added correctly")

    def test_NegativeaddAdjSysandgetAdjSys(self):
        self.main.loadSystems()
        line = self.correctSysLine
        testSys = System()
        testSys.build(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7])
        with self.assertRaises(IndexError):
            testSys.getadjSys(self.correctGateData[0][5])
        testSys.addadjSys(self.main.systems[self.correctGateData[0][5]])
        with self.assertRaises(ValueError):
            testSys.getadjSys("80059")
        with self.assertRaises(TypeError):
            testSys.addadjSys("Fails")
    def test_PositivesetgetParent(self):
        self.main.loadSystems()
        line = self.correctSysLine
        testSys = System()
        testSys.build(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7])
        parent = self.main.systems[self.correctGateData[0][5]]
        testSys.setParent(0, parent)
        self.assertEqual(testSys.getParent(0), parent, "Fail: Parent stored incorrectly or at incorrect num")
        parent = self.main.systems[self.correctGateData[1][5]]
        testSys.setParent(10, parent)
        self.assertEqual(testSys.getParent(10), parent, "Fail: Parent stored incorrectly or at incorrect num")
    def test_NegativesetgetParent(self):
        self.main.loadSystems()
        line = self.correctSysLine
        testSys = System()
        testSys.build(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7])
        parent = self.main.systems[self.correctGateData[0][5]]
        with self.assertRaises(TypeError):
            testSys.setParent("Fail", parent)
        with self.assertRaises(TypeError):
            testSys.setParent(1, "Fail")
        with self.assertRaises(IndexError):
            testSys.getParent(9)
    def test_PositiveaddgetGatePos(self):
        self.main.loadSystems()
        line = self.correctSysLine
        testSys = System()
        testSys.build(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7])
        line = self.correctGateData[0]
        testSys.addGatePos(line[5], [line[1], line[2], line[3]])
        pos = testSys.getGatePos(line[5])
        self.assertEqual(convert(line[1], 2), pos[0], "Fail: PosX not added correctly")
        self.assertEqual(convert(line[2], 2), pos[1], "Fail: PosY not added correctly")
        self.assertEqual(convert(line[3], 2), pos[2], "Fail: PosZ not added correctly")
    def test_NegativeaddgetGatePos(self):
        line = self.correctSysLine
        testSys = System()
        testSys.build(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7])
        line = self.corruptMissingGateData
        with self.assertRaises(IndexError):
            testSys.addGatePos(line[4], [line[1], line[2]])
        line = self.corruptWrongGateData
        with self.assertRaises(ValueError):
            testSys.addGatePos(line[5], [line[1], line[2], line[3]])
        with self.assertRaises(KeyError):
            testSys.getGatePos("fail")
    def test_PositivegetSysDistance(self):
        line = self.correctSysLine
        testSys = System()
        testSys.build(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7])
        line = self.secondSys
        secondSys = System().build(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7])
        self.assertEqual(convert(self.distances[0], 1)/1000, int(testSys.getSysDistance(secondSys)), "Fail: System distances are not getting calculated correctly")
    def test_NegativegetSysDistance(self):
        line = self.correctSysLine
        testSys = System()
        testSys.build(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7])
        secondSys = ""
        with self.assertRaises(TypeError):
            testSys.getSysDistance(secondSys)
    def test_PositiveGetGateDistance(self):
        line = self.correctSysLine
        testSys = System()
        testSys.build(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7])
        line = self.correctGateData
        testSys.addGatePos(line[0][5], [line[0][1], line[0][2], line[0][3]])
        testSys.addGatePos(line[1][5], [line[1][1], line[1][2], line[1][3]])
        expectedResult = round((convert(self.distances[1], 1)/1000)/149597871, 1)
        actualResult = int(testSys.getGateDistance(line[0][5], line[1][5]))
        self.assertEqual(expectedResult, actualResult, "Fail: Gate distances not calculated correctly")
    def test_NegativeGetGateDistance(self):
        line = self.correctSysLine
        testSys = System()
        testSys.build(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7])
        line = self.correctGateData
        testSys.addGatePos(line[0][5], [line[0][1], line[0][2], line[0][3]])
        testSys.addGatePos(line[1][5], [line[1][1], line[1][2], line[1][3]])
        with self.assertRaises(KeyError):
            testSys.getGateDistance(line[0][5], "Test")
        with self.assertRaises(KeyError):
            testSys.getGateDistance("Test", line[1][5])
        with self.assertRaises(GeneralError):
            testSys.getGateDistance(line[1][5], line[1][5])
def convert(num,conType):
    if(conType == 1):
        num = num.split('e+');
    else:
        num = num.split('E');
    num[0] = float(num[0]);
    if len(num) >1:
        num[1] = float(num[1]);
        num = num[0]*pow(10,num[1]);
    else:
        num = num[0];
    return num
