# coding=utf-8


class C(object):
    def instance_method(self, x=None):
        print "Calling instance_method {} {}".format(self, x)

    @staticmethod
    def static_method(x):
        print "Calling static_method {}".format(x)

    @classmethod
    def class_method(cls, x):
        print 'Calling class_method {} {}'.format(cls, x)


c_instance = C()
c_instance.instance_method()
C.static_method('static')
C.class_method('classmethod')
