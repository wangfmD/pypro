# coding:utf-8
word = raw_input("please input string>")
word = word.upper()
txt = open("G:\\05_pypro\\01\\1.txt", 'w')
txt.write(word)
txt.close()
