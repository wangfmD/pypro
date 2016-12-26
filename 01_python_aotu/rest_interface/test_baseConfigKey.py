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
    """测试baseConfigKey"""

    def test_getNavigation(self):
        """测试baseConfigKey接口"""
        url = 'http://10.1.0.44/middlecenter/service/guest/api/v1/auth/sysConfig/baseConfigKey'
        # 请求头

        headers = {'Accept': 'application/json',
                   'Content-Type': 'application/x-www-form-urlencoded'}
        #请求
        r = requests.get(url, headers=headers)
        dict_res = r.json()
        print "*" * 80
        for i in dict_res:
            print i

        print "*" * 80
        for k in dict_res:
            print k, "<===>", dict_res[k]
        print "*" * 80
        print "*" * 80
        print r.url


if __name__ == '__main__':
    unittest.main()
