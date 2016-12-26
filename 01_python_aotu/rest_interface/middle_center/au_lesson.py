# coding:utf-8

# 依赖包
import requests
from Oauth import getAccesssToken, headers

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

host = '10.1.0.56'
h_ip = 'http://' + host + '/middlecenter'
urlplus = '/service/oauth_api/v1/interactive/interactMcuResources/query/lesson'

# 获取token（str）
access_str = getAccesssToken(host)

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
