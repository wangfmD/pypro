# coding=utf-8


def deco(myfunc):
    def _deco(*args, **kwargs):
        print "before %s() called." % myfunc.__name__
        ret = myfunc(*args, **kwargs)
        print "after %s() called. result: %s" % (myfunc.__name__, ret)
        return ret
    return _deco


@deco
def myfunc(a, b):
    print "myfunc(%s,%s) called." % (a, b)
    return a + b


@deco
def myfunc1(a, b, c):
    print "myfunc(%s, %s, %s) called." % (a, b, c)
    return a + b + c

myfunc(1, 2)
myfunc(1, 3)
myfunc1(1, 2, 3)

#@   ==
#fun_wrap = deco(fun)
# fun_wrap()
