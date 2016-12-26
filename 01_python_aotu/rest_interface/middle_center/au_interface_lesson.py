# coding:utf-8

# 依赖包
import requests
import unittest
import unicodedata
# 字符
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

# url = 'http://10.1.0.44/middlecenter/service/guest/api1/v1/navigation/getNavigation'
url = 'http://10.1.0.90/middlecenter/oauth2/authorize'
h_ip = 'http://10.1.0.90/middlecenter'
urlplus = '/service/oauth_api/v1/interactive/interactMcuResources/query/lesson'

# 请求头
payload = {'username': 'administrator',
           'password': 'xungejiaoyu',
           'response_type': 'code',
           'platform': '4fdb212e-88ca-431f-a36e-9c990641d2d9',    # 4fdb212e-88ca-431f-a36e-9c990641d2d9
           'client_id': '6b4cfaea-7016-11e5-bd19-68f728833c05',   # t_auth_client 6b4cfaea-7016-11e5-bd19-68f728833c05
           'redirect_uri': '/oauth2/client/oauth_callback'}

headers = {'Accept': 'application/json',
           'Content-Type': 'application/x-www-form-urlencoded'}
# 请求
r = requests.post(url, data=payload)
# print help(r.text)
print r.text

access = r.text[17:53]
access_str = unicodedata.normalize('NFKD', access).encode('ascii', 'ignore')
print access_str
print type(access_str)
print r.url

payload_1 = {'lessonid': 'cce3d2d9-30bc-4ef5-b201-5176071efd1b',
             'checkresource': 'f',
             'access_token': access_str}

print payload_1
req = requests.post(h_ip + urlplus, headers=headers, data=payload_1)
# req = requests.post(h_ip + urlplus, headers=headers, data=payload_1)
print '-' * 80
print req.text
# print req.json()
print req.url
