# coding:utf-8
import unittest
from Calculator import Count

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


class Test_up_tear(unittest.TestCase):

    def setUp(self):
        # print "#" * 70
        print "test start"

    def tearDown(self):
        # print "#" * 70
        print "test end"


class TestSub(Test_up_tear):
    """两数相减功能测试"""

    def test_sub(self):
        """正数相减"""
        j = Count(5, 1)
        add = j.sub()
        self.assertEqual(j.sub(), 4, "add restult is not correct.")

    def test_sub1(self):
        """负数相减"""
        j = Count(5, 10)
        add = j.sub()
        self.assertEqual(j.sub(), -5, "add restult is not correct.")


if __name__ == '__main__':
    unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTest(TestAdd("test_add1"))   # 测试类下的测试用例方法
    # suite.addTest(TestAdd("test_add"))
    # suite.addTest(TestSub("test_sub"))

    # runner = unittest.TextTestRunner()
    # runner.run(suite)
