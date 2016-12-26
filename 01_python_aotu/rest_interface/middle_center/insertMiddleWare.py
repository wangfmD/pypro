# coding=utf-8
from Oauth import getAccesssToken, headers
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

host = '10.1.0.56'
h_ip = 'http://' + host
urlplus = '/middlecenter/service/api/v1/equipment/middleware/insertMiddleWare'

access_str = getAccesssToken(host)
print access_str


payload_1 = {'host': '10.1.0.60',
             'port': '80',
             'username': 'administrator',
             'password': 'xungejiaoyu',
             'servicepath': '/interact',
             'islink': 1,
             'isSsl': 0,
             'type': 2,
             'keystoreurl': '',
             'keystorepwd': '',
             'cerurl': '',
             'description': 'abc',
             'access_token': access_str}

# payload_1 = {'lessonid': 'cce3d2d9-30bc-4ef5-b201-5176071efd1b',
#              'checkresource': 'f',
#              'access_token': access_str}

r = requests.post(h_ip + urlplus, headers=headers, data=payload_1)
print r.text
