# coding: utf-8

class person(object):
    def __init__(self,name,age,job,school):
        self.name = name
        self.__age = age
        self.__job = job
        self.__school = school

    def has_name(self):
        return hasattr(self, 'name')
