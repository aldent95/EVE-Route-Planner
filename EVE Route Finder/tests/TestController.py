import unittest
from MainTests import TestMainMethods

class TestController():
    def runTests(self):
        suite1 = unittest.TestLoader().loadTestsFromTestCase(TestMainMethods)
        testSuite = unittest.TestSuite([suite1])
        unittest.TextTestRunner(verbosity=2).run(testSuite)















if __name__ == '__main__':
    testController = TestController()
    testController.runTests()
