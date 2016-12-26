# coding:utf-8
import MySQLdb
from MySQLdb import cursors

#======setting databases==========================
host = '127.0.0.1'
user = 'root'
password = '123456'
db = 'bookstore'

# print dir(MySQLdb)

# 建立数据库连接时指定cursorclassdd值，可以返回指定类型的查询返回集
# 字典(dict)MySQLdb.cursors.DictCursor
# 队列


class mysqlOperating(object):
    """docstring for mysqlOperating"""

    def __init__(self):
        try:
            self.connect = MySQLdb.connect(host=host,
                                           user=user,
                                           passwd=password,
                                           db=db,
                                           cursorclass=MySQLdb.cursors.DictCursor)
        except MySQLdb.OperationalError, e:
            print "mysql err %d:%s" % (e.args[0], e.args[1])

    def ExecQury(self, sql):
        cur = self.connect.cursor()
        if not cur:
            raise(NameError, "connect failed")
        cur.execute(sql)
        resultlist = cur.fetchall()
        self.connect.close()
        return resultlist


def test():
    sql = "select gst_id,gst_user,gst_title,gst_content,gst_time from book"
    sql_1 = "select gst_id,gst_user from book"
    c = mysqlOperating()
    res = c.ExecQury(sql_1)
    # print res
    # # con =MySQLdb.connect()
    # print dir(res)
    # print type(res)
    print "-" * 70
    for result in res:
        print result
        # for attribute in result:
        #     print attribute

    # print res[0][1], res[1][1]
    # print help(MySQLdb.connect.func_closure)

test()
