# coding=utf-8

# class Fruit(object):
# def __init__(self, total=0):
# self.__total = total

# def set(self, total):
# self.__total = total

# def print_total(self):
# print "total is {}".format(self.__total)

# app = Fruit()
# app.print_total()
# app.set(10)
# app.print_total()

# class Apple(Fruit):
# def set(self, total):
# self.__total = total

# def print_total(self):
# print "total is {}".format(self.__total)

# a = Apple()
# a.set(100)
# a.print_total()


class Fruit(object):
    total = 0

    @classmethod
    def print_total(cls):
        print 'total is {}'.format(cls.total)

    @classmethod
    def set(cls, total):
        print 'Calling class_method {} {}'.format(cls, total)
        cls.total = total


class Apple(Fruit):
    pass


class Orange(Fruit):
    pass


a = Apple()
a.set(100)
o = Orange()
o.set(200)
Fruit.set(300)
Apple.set(400)
Orange.set(500)
a.print_total()
