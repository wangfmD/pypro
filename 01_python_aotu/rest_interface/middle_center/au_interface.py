# coding:utf-8

# 依赖包
import requests
import unittest
import json
# 字符
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

# url = 'http://10.1.0.44/middlecenter/service/guest/api1/v1/navigation/getNavigation'
url = 'http://10.1.0.56/middlecenter/oauth2/authorize'
h_ip = 'http://10.1.0.56/middlecenter'
urlplus = '/service/oauth_api/v1/interactive/interactMcuResources/query/lesson'
# 请求头
# payload = {'username': 'administrator
# ', 'password':'xungejiaoyu', 'response_type':'code', 'platform':'29a5349d-aee2-4c30-894e-47124f4c6083
# ', 'client_id':'6b4cfaea-7016-11e5-bd19-68f728833c05
# '}
payload = {'username': 'administrator',
           'password': 'xungejiaoyu',
           'response_type': 'code',
           'platform': '29a5349d-aee2-4c30-894e-47124f4c6083',
           'client_id': '6b4cfaea-7016-11e5-bd19-68f728833c05',
           'redirect_uri': '/oauth2/client/oauth_callback'}

headers = {'Accept': 'application/json',
           'Content-Type': 'application/x-www-form-urlencoded'}
# 请求
r = requests.post(url, data=payload)
# print r.text
reqcont = r.text
# 转换为标准的json
agent = eval(reqcont,
             type('Dummy', (dict, ),
                  dict(__getitem__=lambda s, n: n))())
# print dir(reqcont)
print "原始json：", reqcont
print "转换后标准的json：", agent
print "access_token:", agent['access_token']
print '-' * 70
print '-' * 70
print r.url
