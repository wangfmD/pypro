# coding=utf-8
from Oauth0 import getAccesssToken, headers
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

host = '10.1.0.56'
h_ip = 'http://' + host
urlplus = '/middlecenter/service/api/v1/auth/role/select'

access_str = getAccesssToken(host)
print access_str
payload_1 = {'access_token': access_str}

r = requests.get(h_ip + urlplus, params=payload_1)
print r.text
