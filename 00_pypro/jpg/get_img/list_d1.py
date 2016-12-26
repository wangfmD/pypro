# coding:utf-8

list = []
for it in range(0, 10):
    tmp = 'd%s' % it
    print tmp
    list.append(tmp)
    print list

for it in list:
    print it

for it in range(0, len(list)):
    print list[it]

b = []

for it in range(0, len(list)):
    tmp = list.pop()
    b.append(tmp)

print b, list
