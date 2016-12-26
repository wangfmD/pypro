# coding=utf-8

'''示例函数(装饰)
装饰函数的参数为被装饰函数对象，返回原函数对象
装饰的实质語句
myfun = deco(myfun)'''


def deco(func):
    print "before myfunc() called"
    func()
    print "after myfunc() called"
    return func

#
# def myfunc():
#     print "myfun() called."
#
#
# a = deco(myfunc)
# a()


@deco
def myfunc():
    print "myfunc() called."

myfunc()
