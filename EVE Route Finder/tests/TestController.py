import unittest
from MainTests import TestMainMethods
from SystemTests import TestSystemMethods
from RoutesTests import TestRouteMethods

class TestController():
    def runTests(self):
        suite1 = unittest.TestLoader().loadTestsFromTestCase(TestMainMethods)
        suite2 = unittest.TestLoader().loadTestsFromTestCase(TestSystemMethods)
        suite3 = unittest.TestLoader().loadTestsFromTestCase(TestRouteMethods)
        testSuite = unittest.TestSuite([suite3])
        unittest.TextTestRunner(verbosity=2).run(testSuite)

















if __name__ == '__main__':
    testController = TestController()
    testController.runTests()
