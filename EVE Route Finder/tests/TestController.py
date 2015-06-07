import unittest
from MainTests import TestMainMethods
from SystemTests import TestSystemMethods

class TestController():
    def runTests(self):
        suite1 = unittest.TestLoader().loadTestsFromTestCase(TestMainMethods)
        suite2 = unittest.TestLoader().loadTestsFromTestCase(TestSystemMethods)
        testSuite = unittest.TestSuite([suite1, suite2])
        unittest.TextTestRunner(verbosity=2).run(testSuite)

















if __name__ == '__main__':
    testController = TestController()
    testController.runTests()
