#!/usr/bin/env python
# encoding: utf-8

import re
import urllib
from time import sleep


def gethtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html
# f = open("1.html", "w")

# print res_txt
#  print >>f, res_txt
#  f.close()


def getimg(html, name):
    # <img alt = "" src = "http://img.pic123456.com/girl/FEILIN/第二十八期/02.jpg" / > < br / >
    # <img src = "http://1.pengyijie.com/uploads/2016/07/0011.jpg" > <br / >
    reg = r'src="(.*?\.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    # return imglist  E:\python_aotu\jpg
    x = 0
    for im in imglist:
        print im
        urllib.urlretrieve(
            im, "E:\\python_aotu\\jpg\\save\\%s_%s.jpg" % (name, x))
        # urllib.urlretrieve(im, "%s.jpg" % x)
        x += 1
        sleep(1)
http://www.mzitu.com/70274
url = 'http://www.nblvdong.net/archives/2015092934520.html'
html1 = gethtml(url)
print html1

# res_txt = gethtml("http://izzs.co/tuinvlang070.html")
# res_txt = gethtml("http://www.lesmao.com/thread-4246-3-1.html")
# url1 = 'http://www.flkong.net/19013.html'
# url1 = 'http://www.mztuku.com/xinggan/20346/3.html'
# url1 = 'http://www.mztuku.com/xinggan/20346/3.html'

# for x in xrange(1, 48):
#     url = "http://www.mztuku.com/xinggan/20346/%s" % x
#     url1 = url + '.html'
#     res_txt = gethtml(url1)
#     print getimg(res_txt, x)
