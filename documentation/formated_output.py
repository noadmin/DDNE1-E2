__author__ = 'noadmin'

import unittest
import os


class TestDirectory(unittest.TestCase):

    def setUp(self):
        #Let do some preparations
        pass

    def test_TC001(self):
        self.assertEquals(1,0)


    def test_TC002(self):
        self.assertEquals(1,1)

    def test_TC003(self):
        self.assertEquals(1,1)

    def test_TC004(self):
        self.assertEquals(1,0)


if __name__ == '__main__':
    test_list = {}
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestDirectory))
    for test in suite._tests[0]:
        test_list[test._testMethodName] = 'Passed'

    file_o = open('test_log.txt', 'w')
    runner = unittest.TextTestRunner(stream=file_o)
    results = runner.run(suite)

    for result_err in results.errors:
        test_list[result_err[0]._testMethodName] = 'Errors'
    for result_fail in results.failures:
        test_list[result_fail[0]._testMethodName] = 'Fail'

    for test in test_list:
        print test + ': ' + test_list[test]