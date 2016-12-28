# coding=utf-8

class animal(object):
    def __init__(self, name=None):
        self.name = name

    def run(self, *args, **kwargs):
        print "animal", args[0]

    def __call__(self, *args, **kwargs):
        return self.run(*args, **kwargs)
        #  print 'call',args[0]

class cat(animal):
    def run(self, *args, **kwargs):
        print "cat call", args[0]

#  a = animal()
a = cat()
a('mao')
#  a.run(1)
