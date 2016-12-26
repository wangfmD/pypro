# coding=utf-8
from sys import argv
'''参数'''
script = argv
# for str1 in script:
#     print str1
#     a = str1
for i in range(0, len(script)):
    print script[i], i
print ">>>>>>>>>>>>>\n%r\n>>>>>>>>>>>>>" % script
print ">>>\n", script[i] + "\n>>>"
