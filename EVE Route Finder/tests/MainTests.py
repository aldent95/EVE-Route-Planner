import unittest
import os,sys
lib_path = os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), '..'))
sys.path.append(lib_path)
from Main import Main
from System import System

class TestMainMethods(unittest.TestCase):
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
        self.corruptMissingSysLine = lines[1].split("\t")
        self.corruptWrongDataSysLine = lines[2].split("\t")
            
    def tearDown(self):
        self.main = ""
        
    def test_PositiveLoadSysCorrectTotal(self):
        #TODO Try catch
        linecount = 0
        path = os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), '..'))
        path = path+'\data'
        os.chdir(path)
        with open("Systems.txt", 'r') as sysFile:
            for line in sysFile:
                linecount+=1
        sysFile.close()
        self.assertEqual(linecount, self.main.loadSystems(), 'Incorrect amount of systems loaded')

    def test_NegativeLoadSysMissingPath(self):
        try:
            returnedValue = self.main.loadSystems("C:\\test\\noexistant\\")
        except WindowsError:
            returnedValue = "FAILED"
        expectedValue = "Error, missing path, error passed to GUI"
        self.assertEqual(returnedValue, expectedValue, "Fail: Missing Path Error not handleded correctly")
        
    def test_NegativeLoadSysMissingFile(self):
        try:
            returnedValue = self.main.loadSystems(specificFile = "Fail.txt")
        except WindowsError:
            returnedValue = "FAILED"
        expectedValue = "Error, missing file, error passed to GUI"
        self.assertEqual(returnedValue, expectedValue, "Fail: Missing File Error not handleded correctly")

    def test_PositiveaddSysCorrectSysObject(self):
        line = self.correctSysLine
        testSys=System(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7])
        self.assertEquals(testSys, self.main.addSys(line), "Fail: Systems not equal")
        try:
            self.assertEquals(testSys, self.main.systems[line[3]], "Fail: System not added correctly to system list:Systems not equal")
        except KeyError:
            self.fail("Fail: System not added correctly to system list: KeyError")
        self.assertTrue(line[0] in self.main.nameList, "Fail: Name list does not contain system name")
        try:
            self.assertEquals(line[3], self.main.sysNames[line[0]], "Fail: sys Name list does not contain correct sys ID")
        except KeyError:
            self.fail("Fail: sys Name list does not contain system name")
        
##    def test_NegativeaddSysCorruptData(self):
##        path = os.path.dirname(__file__)
##        fileName= "CorruptDataTest.txt"
##        try:
##            returnedValue = self.main.loadSystems(path, fileName)
##        except:
##            returnedValue = "FAILED"
##        expectedValue = "Error, System file data corruption detected, error passed to GUI"
##        if(returnedValue == "Error, missing file, error passed to GUI"):
##            self.assertEqual(returnedValue, expectedValue, "Fail: Corrupt Data test file missing")
##        else:
##            self.assertEqual(returnedValue, expectedValue, "Fail: Corrupt Data not handleded correctly")

    
    

















