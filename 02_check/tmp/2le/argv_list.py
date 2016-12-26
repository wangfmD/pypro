from sys import argv

for i in range(0, len(argv)):
    print "argv[%d]:is %s" % (i, argv[i])

# output
# argv[0]:is E:\python_aotu\2le\argv_list.py

# E:\python_aotu\2le>python argv_list.py abc -ab 111 22
# argv[0]:is argv_list.py
# argv[1]:is abc
# argv[2]:is -ab
# argv[3]:is 111
# argv[4]:is 22