# coding:utf-8
import unittest
import requests
from Calculator import Count
import sys
reload(sys)
sys.setdefaultencoding('utf8')




class Test_up_tear(unittest.TestCase):

    def setUp(self):
        # print "#" * 70
        print "test start"

    def tearDown(self):
        # print "#" * 70
        print "test end"


class TestAdd(Test_up_tear):
    """测试selectGrade"""
    def test_getNavigation(self):
        """测试selectGrade"""
        url = 'http://10.1.0.44/middlecenter/service/guest/api/v1/base/grade/selectGrade'
        # 请求头

        headers = {'Accept': 'application/json',
                   'Content-Type': 'application/x-www-form-urlencoded'}
        #请求
        r = requests.get(url,headers=headers)
        dict_res = r.json()
        for i in dict_res:
            print i
        for k in dict_res:
            print k, "<===>", dict_res[k]
        print r.url


if __name__ == '__main__':
    unittest.main()
