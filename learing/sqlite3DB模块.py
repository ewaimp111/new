#!/usr/bin/env python3
import sqlite3,faker

conn = sqlite3.connect('sscdb.db')
print('链接数据库成功')

cur = conn.cursor()
fk = faker.Faker()
print('    ID     ','   NAME','               ADDRESS      ','        PHONE')
for i in range(1):
    cur.execute("insert into test(name,addr,phone) values('{0}','{1}','{2}')".format(fk.name(),fk.address(),fk.phone_number()))
conn.commit()

c = cur.execute("select * from test limit 5")
for i in c:
    print('|{0:>5} | {1:>10.5} | {2:>20.8} | {3:>20.11} |'.format(i[0],i[1],i[2],i[3]))


#cur.execute("delete from test") # 删除表内容
conn.commit()
conn.close()