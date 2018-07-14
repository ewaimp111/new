#!/usr/bin/env python3
import sqlite3
import sys

class DataBase():
    def __init__(self,dbname):
        self._dbname = dbname
        self._conn = None
        self._cur = None

    def __del__(self):
        self._cur.close()
        self._conn.close()

    def connectDB(self):
        self._conn=sqlite3.connect(self._dbname)
        print('------链接数据库成功-------')
        self._cur=self._conn.cursor()

    def insert_data(self,table_name,*data):
        for i in list(*data):
            line = i.split()
            #print(line[0],line[1])
            sql ="insert Or IGNORE into {}  values ({},{})".format(table_name,"'"+line[0]+"'","'"+line[1]+"'")
        #param = (table_name,data[0],data[1])
        self._cur.execute(sql)
        self._conn.commit()
        print('插入数据库成功！')



    def query_data(self,table_name):
        result = self._cur.execute('select * from {0}'.format(table_name))
        self._conn.commit()
        l = []
        for r in result :
            l.append(r)
        return l

    def delete_data(self,table_name):
        self._cur.execute('delete from {}'.format(table_name))
        self._conn.commit()

   # def save_to_database(self): #保存到数据库
   #     for i in self.lishi_numlist:
   #         qs,hm = str(i).split()
   #         #print(qs,hm)
   #         self.db.insert_data('lishinumber',[qs,hm])



# db = DataBase('/Users/BigZeus/PycharmProjects/notes/ssc/cp.db')
# db.connectDB()
# l = ['0023 00345','0024 98923']
# db.insert_data('cqssc',l)

# for i in l:
#     q,h = str(i).split()
#     db.insert_data('cqssc',["'"+q+"'","'"+h+"'"])
#     print(q,h)
# l1 = db.query_data('cqssc')
# print(l1)
#
# x= '02'
# '"'.join(x).join("-")
# print(x)

