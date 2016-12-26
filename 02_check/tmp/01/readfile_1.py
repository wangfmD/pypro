# coding=utf-8
filecon = []
with open('G:\\05_pypro\\01\\1.txt') as f:
    for line in f:
        a = line.split(':')
        filecon.append(a)
        print type(a)

print filecon
