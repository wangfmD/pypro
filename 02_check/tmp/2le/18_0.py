def print_2(*args):
    arg1, arg2 = args
    print "print_2 arg1: %s,arg2: %s" % (arg1, arg2)


def print_2_again(arg1, arg2):
    print "print_2_again arg1: %s, arg2: %s" % (arg1, arg2)


def print_1(arg1):
    print "print_1 arg1: %s" % arg1

print_1("11")
print_2(10 + 20, 20)
print_2_again("abca", "abca2")
