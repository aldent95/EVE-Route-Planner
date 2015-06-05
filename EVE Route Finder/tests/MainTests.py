import unittest
import os,sys
lib_path = os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), '..'))
sys.path.append(lib_path)
from Main import Main
from System import System
import math

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
        self.corruptMissingDataSysLine = lines[1].split("\t")
        self.corruptWrongDataSysLine = lines[2].split("\t")
        self.trimTestData = [lines[3], lines[4], lines[5], lines[6], lines[7], lines[8]]
        self.trimBadData = [lines[9]]
        self.addGateGoodData = lines[10].split("\t")
        self.addGateMissingData = lines[11].split("\t")
        self.addGateCorruptData = lines[12].split("\t")
        self.systemsRouteTestData =[lines[13].split("\t"), lines[14].split("\t"),lines[15].split("\t"), lines[16].split("\t"), lines[17].split("\t"), lines[18].split("\t"), lines[19].split("\t"), lines[20].split("\t"), lines[21].split("\t"), lines[22].split("\t")]
        self.RouteTestsExpectedResults = [33,42,55
            
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
        testSys = System() #Create a sys object
        testSys = testSys.build(line[0], line[1], line[2], line[3], line[4], line[5], line[6],line[7])
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
        
    def test_NegativeaddSysCorruptData(self):
        line= self.corruptMissingDataSysLine
        returnedValue = self.main.addSys(line)
        expectedValue = "Error, System file missing data, error passed to GUI"
        if(returnedValue == "Error, missing file, error passed to GUI"):
            self.assertEqual(returnedValue, expectedValue, "Fail: Corrupt Data test file missing")
        else:
            self.assertEqual(returnedValue, expectedValue, "Fail: Missing Data not handleded correctly")
        line = self.corruptWrongDataSysLine
        returnedValue = self.main.addSys(line)
        expectedValue = "Error, System file data corrupt, error passed to GUI"
        if(returnedValue == "Error, missing file, error passed to GUI"):
            self.assertEqual(returnedValue, expectedValue, "Fail: Corrupt Data test file missing")
        else:
            self.assertEqual(returnedValue, expectedValue, "Fail: Corrupt Data not handleded correctly")

    def test_PositivetrimSystems(self):
        lines = self.trimTestData
        expectedLength = 2
        returnedLength = len(self.main.trimSystems(lines))
        self.assertEqual(returnedLength, expectedLength, "Fail: some systems were either trimmed or not trimmed when they shouldn't/should have been")
    
    def test_NegativetrimSystems(self):
        lines = self.trimBadData
        expectedValue = "Error, System file missing data, error passed to GUI"
        self.assertEqual(self.main.trimSystems(lines), expectedValue, "Fail: Missing Data not handleded correctly in trim systems")

    def test_PositiveLoadGate(self):
        self.main.loadSystems()
        #TODO Try catch
        linecount = 0
        path = os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), '..'))
        path = path+'\data'
        os.chdir(path)
        with open("Stargates.txt", 'r') as sysFile:
            for line in sysFile:
                linecount+=1
        sysFile.close()
        self.assertEqual(linecount, self.main.loadGates(), 'Incorrect amount of systems loaded')

    def test_NegativeLoadGate(self):
        self.main.loadSystems()
        try:
            returnedValue = self.main.loadGates("C:\\test\\noexistant\\")
        except WindowsError:
            returnedValue = "FAILED"
        expectedValue = "Error, missing path, error passed to GUI"
        self.assertEqual(returnedValue, expectedValue, "Fail: Missing Path Error not handleded correctly")
        try:
            returnedValue = self.main.loadGates(specificFile = "Fail.txt")
        except WindowsError:
            returnedValue = "FAILED"
        expectedValue = "Error, missing file, error passed to GUI"
        self.assertEqual(returnedValue, expectedValue, "Fail: Missing File Error not handleded correctly")

    def test_PositiveaddGate(self):
        line = self.addGateGoodData
        self.main.loadSystems()
        testSys = self.main.systems[line[4]]
        adjSys = self.main.systems[line[5]]
        self.main.addGate(line)
        self.assertEquals(adjSys, self.main.systems[line[4]].getadjSys(line[5]), "Fail: testSys does not have correct adj sys")
        pos = [convert(line[1], 2), convert(line[2], 2), convert(line[3], 2)]
        self.assertEquals(pos, self.main.systems[line[4]].getGatePos(line[5]), "Fail: Expected gate POS and given gate POS not equal")
        
        
    def test_NegativeaddGate(self):
        self.main.loadSystems()
        line= self.addGateMissingData
        returnedValue = self.main.addGate(line)
        expectedValue = "Error, Gate file missing data, error passed to GUI"
        if(returnedValue == "Error, missing file, error passed to GUI"):
            self.assertEqual(returnedValue, expectedValue, "Fail: Corrupt Data test file missing")
        else:
            self.assertEqual(returnedValue, expectedValue, "Fail: Missing Data not handleded correctly")
        line = self.addGateCorruptData
        returnedValue = self.main.addGate(line)
        expectedValue = "Error, Gate file data corrupt, error passed to GUI"
        if(returnedValue == "Error, missing file, error passed to GUI"):
            self.assertEqual(returnedValue, expectedValue, "Fail: Corrupt Data test file missing")
        else:
            self.assertEqual(returnedValue, expectedValue, "Fail: Corrupt Data not handleded correctly")

    def test_PositivefindRoute(self):
        
        

    def test_NegativefindRoute(self):

        

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
    return num;










