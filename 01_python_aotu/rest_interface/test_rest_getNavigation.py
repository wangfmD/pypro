# coding:utf-8

# 依赖包
import requests
import unittest
# 字符
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

class Test_restinterface_getNavigation(unittest.TestCase):
    """测试getNavigation接口"""
    def setUp(self):
        # print "#" * 70
        print "test start"

    def tearDown(self):
        # print "#" * 70
        print r.text
        print r.url
        print "test end"

    def Test_getNavigation(self):
        # 请求URL
        url = 'http://10.1.0.44/middlecenter/service/guest/api1/v1/navigation/getNavigation'
        # 请求头
        
        headers = {'Accept': 'application/json',
                   'Content-Type': 'application/x-www-form-urlencoded'}
        #请求
        r = requests.get(url,headers=headers)
        print r.text
        print r.url

if __name__ == '__main__':
    unittest.main()
