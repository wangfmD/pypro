# coding=utf-8

file_o = open("G:\\05_pypro\\01\\1.txt", 'r')
cont = file_o.readline()
print cont
print type(cont)
c1 = cont.split(' ')

print c1
file1_0 = open("G:\\05_pypro\\01\\2.txt", 'w')
for w1 in c1:
    file1_0.write(w1 + '\n')

print help(file1_0.write)

file1_0.close()
