# coding=utf-8
import urllib

# https://www.1688.com/robots.txt

# print dir(urllib)  # 帮助
# output
# ['ContentTooShortError', 'FancyURLopener', 'MAXFTPCACHE', 'URLopener',
# '__all__', '__builtins__', '__doc__', '__file__', '__name__', '__package__',
# '__version__', '_asciire', '_ftperrors', '_have_ssl', '_hexdig', '_hextochr',
# '_hostprog', '_is_unicode', '_localhost', '_noheaders', '_nportprog',
# '_passwdprog', '_portprog', '_queryprog', '_safe_map', '_safe_quoters',
# '_tagprog', '_thishost', '_typepro g', '_urlopener', '_userprog', '_valueprog',
# 'addbase', 'addclosehook', 'addinfo', 'addinfourl', 'always_safe', 'base64',
# 'basejoin', 'c', 'ftpcache', 'ftperrors', 'ftpwrapper', 'getproxies',
# 'getproxies_environment', 'getproxies_registry', 'i', 'localhost', 'noheaders',
# 'os', 'pathname2url', 'proxy_bypass', 'proxy_bypass_environment',
# 'proxy_bypass_registry', 'quote', 'quote_plus', 're', 'reporthook', 'socket',
# 'splitattr', 'splithost', 'splitnport', 'splitpasswd', 'splitport', 'splitquery',
# 'splittag', 'splittype', 'splituser', 'splitvalue', 'ssl', 'string', 'sys', 'test1',
# 'thishost', 'time', 'toBytes', 'unquote', 'unquote_plus', 'unwrap', 'url2pathname',
# 'urlcleanup', 'urlencode', 'urlopen', 'urlretrieve']
# [Finished in 0.3s]

# print help(urllib.urlopen)  # 帮助

# output
# urlopen(url, data=None, proxies=None, context=None)
#     Create a file-like object for the specified URL to read from.

# url = 'http://izzs.co/boluoshe057.html'
# url = 'http://www.163.com/'
# html = urllib.urlopen(url)
# print html.read()

url = 'http://www.163.com/'
html = urllib.urlopen(url)
# 错误print html.read().decode("gb2312").encode('utf-8')
# print html.read().decode("gbk").encode('utf-8')

# print dir(html)
# output
# ['__doc__', '__init__', '__iter__', '__module__', '__repr__', 'close', 'code',
#  'fileno', 'fp', 'getcode', 'geturl', 'headers', 'info', 'next', 'read', 'readline',
#  'readlines', 'url']
# [Finished in 0.5s]

print html.info()  # 参看头部信息
# output
# Expires: Sat, 02 Jul 2016 14:46:10 GMT
# Date: Sat, 02 Jul 2016 14:44:50 GMT
# Server: nginx
# Content-Type: text/html; charset=GBK
# Vary: Accept-Encoding,User-Agent,Accept
# Cache-Control: max-age=80
# X-Via: 1.1 hdwt42:8080 (Cdn Cache Server V2.0), 1.1 awt86:5 (Cdn Cache Server V2.0)
# Connection: close

# html = urllib.urlopen(url)print html.read().decode("gb2312").encode('utf-8')

# print html.getcode()   # 状态码信息比较重要（200的状态码才可以正常抓取，203等不可用）
"""
网页状态码200
3xx开头的 重定向了如：301永久重定向
403禁止访问
# 书籍：http权威指南
"""
# print html.geturl() #可以返回url


# E:\python_aotu\jpg\get_html.py
# urllib.urlretrieve(url, "E:\\python_aotu\\jpg\\save.html")  # 网页抓取，下载页面
