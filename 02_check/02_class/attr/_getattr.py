# coding: utf-8

from tmpclass import person

p1 = person('www', 18 , 'coder', 'NJDX')

name = getattr(p1, 'name', False)
name = getattr(p1, 'name', False)
print getattr(p1, 'name1', 'not exist name1')
print getattr(p1, 'name', 'not exist name')
print getattr(p1, '__age', 'not exist __age')
print p1.has_name()
print isinstance(p1, person)
