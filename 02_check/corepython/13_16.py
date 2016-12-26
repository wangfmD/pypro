# coding=utf-8

class DevNull(object):
    def __get__(self, obj, type=None):
        print 'Accessing attr... ignoring'

    def __set__(self, obj, val):
        print 'Attempt %r' % (val)

class C1(object):
    foo = DevNull()

c1 = C1()
c1.foo = 'bar'
print c1.foo
