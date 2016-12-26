# coding: utf-8

class WrapMe(object):
    def __init__(self, obj):
        self.__data = obj
    def get(self):
        return self.__data

    def __repr__(self):
        return 'self.__data'

    def __str__(self):
        return str(self.__data)+1

    def __getattr__(self, attr):
        return getattr(self.__data, attr)

if __name__ == '__main__':
    wrapfushu = WrapMe(3.5+4.2j)
    # print wrapfush
