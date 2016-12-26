# coding=utf-8
import MySQLdb
from MySQLdb import cursors

# setting db
host = '127.0.0.1'
user = 'root'
passwd = '123456'
db = 'bookstore'


class getdb:
    def __init__(self, host=host, user=user, passwd=passwd, db=db):
        self.conn = MySQLdb.connect(host=host,
                                    user=user,
                                    passwd=passwd,
                                    db=db,
                                    cursorclass=MySQLdb.cursors.DictCursor)

    def execQury(self, sql):
        cur = self.conn.cursor()
        cur.execute(sql)
        reslist = cur.fetchall()
        return reslist
        self.con.close()


c = getdb()
result = c.execQury('select * from book')
# print result
print type(result)

for tuple_1 in result:
    print tuple_1
    print type(tuple_1)
    for k in tuple_1:
        if k == 'gst_user':
            print k, '++', tuple_1[k]
