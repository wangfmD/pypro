# encoding: utf-8

import urllib2

url = "http://www.mzitu.com/61622"

req = urllib2.Request(url)

req.add_header(
    "User-Agent",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/51.0.2704.79 Chrome/51.0.2704.79 Safari/537.36")
req.add_header("GET", url)
req.add_header("Host", "www.mzitu.com")
req.add_header("Referer", "http://www.mzitu.com/61622")

print req.get_data()
html = urllib2.urlopen(req)
print html.read()

# Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
# Accept-Encoding:gzip, deflate, sdch
# Accept-Language:zh-CN,zh;q=0.8
# Cache-Control:max-age=0
# Connection:keep-alive
# Host:www.mzitu.com
# If-Modified-Since:Tue, 02 Aug 2016 12:49:40 GMT
# Upgrade-Insecure-Requests:1
# User-Agent:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/51.0.2704.79 Chrome/51.0.2704.79 Safari/537.36
