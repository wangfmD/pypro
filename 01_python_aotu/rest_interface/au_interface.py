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
url = 'http://10.1.0.90/middlecenter/oauth2/authorize'
h_ip = 'http://10.1.0.90/middlecenter'
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
#请求
r = requests.post(url, data=payload)
# print r.text
reqcont = r.text
agent = eval(reqcont,
             type('Dummy', (dict, ),
                  dict(__getitem__=lambda s, n: n))())
# print dir(reqcont)
print reqcont
print agent

# s1 = json.loads(agent)
print agent['access_token']
print '-' * 70
# print type(s1)
# print s1['access_token']
print '-' * 70
# print type(s)
# print 's：', s
# print type(s1)
# print 's1:', s1
# reqcont_s = reqcont_s1.split(',')
# reqcont_s1 = reqcont_s.strip('{')
# print reqcont_s1
# print reqcont_s
# print reqcont_s[0]
# access_token_v = r.text[17:53]
# access_token_s = access_token_v.encode('utf-8')
# print type(access_token_v)
# print type(access_token_s)
# print dir(reqcont)
print r.url
#
# payload_1 = {'lessonid': 'cce3d2d9-30bc-4ef5-b201-5176071efd1b',
#              'checkresource': 'f',
#              'access_token': access_token_v}
#
# print payload_1
# req = requests.post(h_ip + urlplus, headers=headers, data=payload_1)
# print '-' * 80
# print req.text
# print req.url
