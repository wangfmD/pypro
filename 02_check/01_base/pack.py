# coding=utf-8

def c(x=0):
    co = [x]
    def i():
        co[0]+=1
        return co[0]
    return i

c1 = c(4)
print c1()
print c1()
print c1()
c2 = c(100)
print c2()
print c1()
