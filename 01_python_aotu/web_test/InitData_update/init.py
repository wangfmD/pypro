# coding=utf-8
import sys
import ConfigParser
reload(sys)
sys.setdefaultencoding("utf-8")

classroom_para = []
classroom_tmp = []
base_url = ''
db_conf = {}
cf = ConfigParser.ConfigParser()
cf.read("G:\\04py\\py_all_pro\\01_python_aotu\\web_test\\InitData_update\\init0.conf")
# cf.read("init0.conf")
# cf.read("/opt/myspace/pro/py_all_pro/02_tmp/01/init.conf")
sections = cf.sections()

for s in sections:
    if s.lower().find('classroom_para') != -1:
        classroom_tmp.append(s)
    if s.lower().find('base_url') != -1:
        base_url = 'http://' + cf.get(s, 'addr')
        interact_1 = cf.get(s, 'interact_1')
    if s.lower().find('db_conf') != -1:
        # host = cf.get(s, 'host')
        db_conf.setdefault('host', cf.get(s, 'host'))
        # hostadd = cf.get(s, 'hostadd')
        db_conf.setdefault('hostadd', cf.get(s, 'hostadd'))
        # user = cf.get(s, 'user')
        db_conf.setdefault('user', cf.get(s, 'user'))
        # passwd = cf.get(s, 'passwd')
        db_conf.setdefault('passwd', cf.get(s, 'passwd'))
        # db = cf.get(s, 'db')
        db_conf.setdefault('db', cf.get(s, 'db'))
        db_conf.setdefault('port', cf.get(s, 'port'))

for s in classroom_tmp:
    opts = cf.options(s)
    arr = {}
    for o in opts:
        name = cf.get(s, o)
        # print o,": ", name
        arr.setdefault(o, unicode(name).encode("utf-8"))
    classroom_para.append(arr)

if __name__ == '__main__':
    # print classroom_tmp
    # print base_url
    # for classroom in classroom_para:
    #     print classroom_para
    # print len(classroom_para)
    # print classroom_para[0]['classroomname']

    print db_conf
