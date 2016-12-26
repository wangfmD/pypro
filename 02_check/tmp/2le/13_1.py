from sys import argv

script, name = argv

print "Hi %s I am %s script" % (name, script)

promp = '$ '
print "you like ?"
like = raw_input(promp)

print "you loves?"
loves = raw_input(promp)

print "what kind computer do you have?"
computer = raw_input(promp)

print "aa %r bb %r cc %r" % (like, loves, computer)
