# coding=utf-8
from Oauth import getAccesssToken, headers
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

host = '10.1.0.54'
h_ip = 'http://' + host
urlplus = '/interact/api/oauth_api/v1/msgcenter/check_lesson_mcus'

access_str = getAccesssToken(host)

payload_1 = {'lessonId': 'a7c74826-21d3-49f3-8446-881c6e894db9',
             'equipmentids': '3fc3ff07-42d7-451f-8deb-03fa86f6eebb',
             'access_token': access_str}

# payload_1 = {'lessonid': 'cce3d2d9-30bc-4ef5-b201-5176071efd1b',
#              'checkresource': 'f',
#              'access_token': access_str}

r = requests.post(h_ip + urlplus, headers=headers, data=payload_1)
print r.text
