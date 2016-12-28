import sys
def f1(*args):
    print type(args)
    print args

# f2('a', 'c', 'd')


def f2(**kwargs):
    print type(kwargs)
    print kwargs

#  f2(a=1)

print sys.argv
print type(sys.argv)
print __file__
print __name__
print __debug__
print __package__
