import sqlite3

sql = '''
create table entries (
  id integer primary key autoincrement,
  title text not null,
  'text' text not null
);

'''
conn = sqlite3.connect('flaskr.db')
cursor = conn.cursor()
cursor.execute(sql)
conn.commit()
cursor.close()
conn.close()
