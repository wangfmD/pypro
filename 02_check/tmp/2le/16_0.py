from sys import argv


script, filename = argv
print "We are going to erase %s " % filename
print "NO,hit Ctrl-C"
print "Yes,hist enter"

raw_input("?")

target = open(filename, 'w')
target.truncate()

print "Now Input three lines"

l1 = raw_input("line 1>")
l2 = raw_input("line 2>")
l3 = raw_input("line 3>")

# target.write(l1)
# target.write("\n")
# target.write(l2)
# target.write("\n")
# target.write(l3)
# target.write("\n")
# target.close()
target.write("%s\n%s\n%s\n" % (l1, l2, l3))
