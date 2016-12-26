# coding:utf-8
import MySQLdb
from MySQLdb import cursors
# setting cfg
host = '127.0.0.1'
user = 'root'
passwd = '123456'
db = 'bookstore'
class sqlOperating:
    def __init__(self,
                host=host,
                user=user,
                passwd=passwd,
                db=db):
        self.con = MySQLdb.connect(
                host=host,user=user,passwd=passwd,db=db,cursorclass=MySQLdb.cursors.DictCursor)

    def execQury(self,sql):
        cur = self.con.cursor()
        cur.execute(sql)
        reslist = cur.fetchall()
        return reslist
sql = 'select * from book'
c = sqlOperating()
result = c.execQury(sql)
print result
