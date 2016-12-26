import sqlite3


def createdb():
    conn = sqlite3.connect('G:\\05_pypro\\01\\SQL\\test.db')
    print 'Opened databases successfully!'
    sql = '''
    CREATE TABLE COMPANY
           (ID INT PRIMARY KEY     NOT NULL,
           NAME           TEXT    NOT NULL,
           AGE            INT     NOT NULL,
           ADDRESS        CHAR(50),
           SALARY         REAL);
           '''
    conn.execute(sql)
    print 'create db successfully!'
    conn.close()


def insertdb():
    conn = sqlite3.connect('G:\\05_pypro\\01\\SQL\\test.db')
    print 'Opned databases successfully'
    conn.execute(
        "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (1, 'Paul', 32, 'California', 20000.00 )")

    conn.execute(
        "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (2, 'Allen', 25, 'Texas', 15000.00 )")
    conn.commit()
    conn.close()


def selectdb():
    conn = sqlite3.connect('G:\\05_pypro\\01\\SQL\\test.db')
    reslist = conn.execute('select id,name from COMPANY')
    for res in reslist:
        print "id:", res[0]
        print "name:", res[1]
    conn.close()

# insertdb()
selectdb()
