# coding:utf-8
import unittest
import requests
from Calculator import Count
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


class Test_up_tear(unittest.TestCase):

    def setUp(self):
        # print "#" * 70
        print "test start"

    def tearDown(self):
        # print "#" * 70
        print "test end"


class TestAdd(Test_up_tear):
    """两数相加功能测试"""

    # def setUp(self):
    #     print "#" * 70
    #     print "start Test"

    def test_add(self):
        """正数相加"""
        j = Count(2, 4)
        add = j.add()
        self.assertEqual(j.add(), 6, "add restult is not correct.")

    def test_add1(self):
        """负数相加"""
        j = Count(-2, -5)
        add = j.add1()
        self.assertEqual(j.add1(), -7, "add restult is not correct.")

    def test_getNavigation(self):
        """测试getNavigation接口"""
        url = 'http://10.1.0.44/middlecenter/service/guest/api1/v1/navigation/getNavigation'
        # 请求头

        headers = {'Accept': 'application/json',
                   'Content-Type': 'application/x-www-form-urlencoded'}
        #请求
        r = requests.get(url,headers=headers)
        dict_res = r.json()
        print "*" * 80
        for i in dict_res:
            print i

        print "*"*80
        for k in dict_res:
            print k, "<===>", dict_res[k]
        print "*" * 80
        print "*" * 80
        print r.url


if __name__ == '__main__':
    unittest.main()
