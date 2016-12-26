# coding=utf-8
import sys
import ConfigParser
reload(sys)
sys.setdefaultencoding("utf-8")

classroom_para = []
classroom_tmp = []
base_url = ''
cf = ConfigParser.ConfigParser()
# config = ConfigParser.ConfigParser()




# config.read("G:\\05_pypro\\01\\init.conf")
cf.read("/opt/myspace/pro/py_all_pro/02_tmp/01/init.conf")

sections = cf.sections()






# sections = config.sections()
for s in sections:
    if s.lower().find('classroom_para') != -1:
        classroom_tmp.append(s)
    if s.lower().find('base_url') != -1:
        base_url = cf.get(s,'addr')

print classroom_tmp
print base_url



for s in classroom_tmp:
    opts = cf.options(s)
    arr = {}
    for o in opts:
        name = cf.get(s,o)
        # print o,": ", name
        arr.setdefault(o, name)
    classroom_para.append(arr)
print classroom_para

# for s in sections:
#     kvs = cf.items(s)
#     print 'name:', kvs


# di = {}
# print(dir(di))

# for s in sections:
#     name = cf.get("classroom_para","name")

# opts = cf.options("classroom_para")
# print 'options:', opts
#
# kvs = cf.items("classroom_para")
# print 'name:', kvs
# name = cf.get("classroom_para","name")
# print name
