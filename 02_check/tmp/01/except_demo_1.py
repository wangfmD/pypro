# coding: utf-8

try:
    open("1.txt")
except IOError,e:
    print "error %s" % e
else:
    pass
