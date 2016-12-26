# coding:utf-8
txt = open("write_to_file", 'w+')
while True:
    le = raw_input(">")
    if le == '#':
        break
    txt.write(le)

txt.close()
