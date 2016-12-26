# coding=utf8

# seek()

# seek()函数是属于文件操作中的函数，用来移动文件读取指针到指定位置。

# 语法：


# fileObject.seek(offset[, whence])

# offset – 开始的偏移量，也就是代表需要移动偏移的字节数

# whence：可选，默认值为
# 0。给offset参数一个定义，表示要从哪个位置开始偏移；0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起。


f = open("test", 'r')
f.seek(1, 1)
print f.readline()
f.seek(1, 0)
print f.readline()
print f.readline()
print f.readline()
f.close()
