# coding:utf-8
# url1 = 'http://www.mztuku.com/xinggan/20346/3.html'
url1 = 'http://www.mztuku.com/xinggan/20346/3.html'

for x in xrange(1, 48):
    url = "http://www.mztuku.com/xinggan/20346/%s" % x
    url1 = url + '.html'
    print url1
