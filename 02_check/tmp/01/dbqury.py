# conding:utf-8
import MySQLdb
from MySQLdb import cursors
# setting config
host = '127.0.0.1'
user = 'root'
passwd = '123456'
db = 'bookstore'


class sqlOperating:
    """doc"""

    def __init__(self,
                 host=host,
                 user=user,
                 passwd=passwd,
                 db=db):
        try:
            self.con = MySQLdb.connect(
                host=host, user=user, passwd=passwd, db=db, cursorclass=MySQLdb.cursors.DictCursor)
        except MySQLdb.Error, e:
            print "MySQL Error %d:%s" % (e.args[0], e.args[1])
            print "##" * 4

    def execQury(self, sql):
        cur = self.con.cursor()
        cur.execute(sql)
        res = cur.fetchall()
        return res
        self.con.close()

sql = "select * from base_kind"
c = sqlOperating("10.1.0.44", 'root', 'xungejiaoyu2016,06.20', 'middle')
result = c.execQury(sql)
# print result
for res in result:
    print res
