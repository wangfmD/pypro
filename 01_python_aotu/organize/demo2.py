# encoding:utf-8
import unittest
from Calculator import Count
from HTMLTestRunner import HTMLTestRunner
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# print dir(unittest)
# ['BaseTestSuite', 'FunctionTestCase', 'SkipTest', 'TestCase',
#  'TestLoader', 'TestProgram', 'TestResult', 'TestSuite',
#  'TextTestResult', 'TextTestRunner', '_TextTestResult',
#  '__all__', '__builtins__', '__doc__', '__file__', '__name__',
#  '__package__', '__path__', '__unittest', 'case', 'defaultTestLoader',
#  'expectedFailure', 'findTestCases', 'getTestCaseNames', 'installHandler',
#  'loader', 'main', 'makeSuite', 'registerResult', 'removeHandler',
#  'removeResult', 'result', 'runner', 'signals', 'skip', 'skipIf',
#  'skipUnless', 'suite', 'util']


class TestAdd(unittest.TestCase):
    """两数相加功能测试"""

    def setUp(self):
        print "#" * 70
        print "start Test"

    def test_add(self):
        """正数相加"""
        j = Count(2, 4)
        add = j.add()
        self.assertEqual(j.add(), 6, "add restult is not correct.")

    def test_add1(self):
        """负数相加"""
        j = Count(2, 5)
        add = j.add1()
        self.assertEqual(j.add1(), 7, "add restult is not correct.")

    def tearDown(self):
        print "#" * 70
        print "Test end"


class TestSub(unittest.TestCase):
    """两数相减功能测试"""

    def setUp(self):
        print "#" * 70
        print "start Test"

    def tearDown(self):
        print "#" * 70
        print "Test end"

    def test_sub(self):
        """负数相减"""
        j = Count(5, 1)
        add = j.sub()
        self.assertEqual(j.sub(), 4, "add restult is not correct.")


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(TestAdd("test_add1"))
    suite.addTest(TestAdd("test_add"))
    suite.addTest(TestSub("test_sub"))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)

    fp = open('./restult.html', 'wb')
    runner = HTMLTestRunner(stream=fp, title='测试报告', description='用例执行情况：')
    runner.run(suite)
    fp.close()
