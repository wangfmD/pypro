from sys import argv

script, filename = argv

txt = open(filename)
print "Here is your file %s" % filename

print txt.read()

print "I will also ask you to type it again:"
file_again = raw_input("> ")
txt1 = open(file_again)

print txt1.read()
txt1.close()
txt.close()
