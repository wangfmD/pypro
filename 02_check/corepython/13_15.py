# coding: utf-8

class WrapMe(object):
    def __init__(self, obj):
        self.data = obj
    def get(self):
        return self.data

    def __repr__(self):
        return 'self.data'

    def __str__(self):
        return str(self.data)

    def __getattr__(self, attr):
        return getattr(self.data, attr)

if __name__ == '__main__':
    wrapfushu = WrapMe(3.5+4.2j)
    print wrapfushu
    print wrapfushu.real
    print hasattr(wrapfushu, 'data')
