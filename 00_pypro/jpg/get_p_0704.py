#!/usr/bin/env python
# encoding: utf-8

import re
import urllib
from time import sleep


def gethtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html


def getimg(html, name, x):
    #     http://img.mztuku.com/20/20323/44.jpg
    #     http://img.mztuku.com/20/20305/0.jpg
    reg = r'src="(http://im.*?[^0]\.jpg)"'
    # reg = r'src="(.*?20323/.*\.jpg)"' #ok
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    # return imglist  E:\python_aotu\jpg

    for im in imglist:

        print im
        urllib.urlretrieve(
            im, "E:\\python_aotu\\jpg\\save3\\%s_%s.jpg" % (x, name))
        # urllib.urlretrieve(im, "%s.jpg" % x)

        # sleep(1)
# http://img.mztuku.com/20/20323/4.jpg

for x in xrange(0, 24):
    name = '20340'  # '20312'  # '20348'
    url = "http://www.mztuku.com/xinggan/%s/%s" % (name, x)
    url1 = url + '.html'
    res_txt = gethtml(url1)
    print getimg(res_txt, x, name + str(x))
