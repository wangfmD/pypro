from sys import argv
from os.path import exists

script, from_file, to_file = argv

input = open(from_file)
print "Copy from %s to %s" % (from_file, to_file)

inp = open(from_file)
indate = inp.read()

print "The input file is %d bypes long " % len(indate)
print "output file exist? %r" % exists(to_file)
raw_input("continue:enter/Ctrl-c>")
oup = open(to_file, 'w')
oup.write(indate)
inp.close()
oup.close()
