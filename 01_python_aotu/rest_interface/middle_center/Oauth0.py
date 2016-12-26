# coding:utf-8

# 依赖包
import requests
# 字符集
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

headers = {'Accept': 'application/json',
           'Content-Type': 'application/x-www-form-urlencoded'}


def getAccesssToken(host):

    h_ip = 'http://' + host + '/middlecenter'
    url_oauth = '/oauth2/authorize'
    # 请求头

    payload = {'username': 'hnsadm1in',
               'password': '111111',
               'response_type': 'code',
               'platform': 'f886b66c-9763-403d-88ab-307d6701dc4e',
               'client_id': '6b4cfaea-7016-11e5-bd19-68f728833c05',
               'redirect_uri': '/oauth2/client/oauth_callback'}

    # 请求
    r = requests.post(h_ip + url_oauth, data=payload)

    # 转换为标准的json
    # agent = eval(r.text,
    #              type('Dummy', (dict, ),
    #                   dict(__getitem__=lambda s, n: n))())

    return r.text

if __name__ == '__main__':
    print getAccesssToken('10.1.0.56')
