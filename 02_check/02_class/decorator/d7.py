# coding=utf-8


def deco(arg):
    def _deco(f):
        def __deco():
            print "before %s called,%s" % (f.__name__, arg)
            f()
            print "after"
        return __deco
    return _deco


@deco('module1')
def myfun():
    print 'exec myfunc'


@deco('model2')
def myfun1():
    print 'exec myfunc'

myfun()
myfun1()
