#!/usr/bin/env python3


import requests as reqs
import xml.dom.minidom
from bs4 import BeautifulSoup
import threading
import time
import arrow
import random
import sscDB

ssclist = dict(xj='xjssc',cq='cqssc',tj='tjssc',yn='ynssc')
cqurl ='http://kaijiang.500.com/static/public/ssc/xml/qihaoxml/'
#       http://kaijiang.500.com/static/public/ssc/xml/qihaoxml/20180529.xml?

#       http://kaijiang.500.com/static/info/kaijiang/xml/xjssc/20151201.xml?  有效，之前日期无效
xjurl ='http://kaijiang.500.com/static/info/kaijiang/xml/xjssc/20180507.xml?'
tjurl ='http://kaijiang.500.com/static/info/kaijiang/xml/tjssc/20180525.xml?'
ynurl ='http://kaijiang.500.com/static/info/kaijiang/xml/ynssc/20180614.xml?'
url   ='http://kaijiang.500.com/static/info/kaijiang/xml/'

headers = {'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
               'Accept-Encoding':'gzip, deflate, sdch',
               'Accept-Language':'zh-CN,zh;q=0.8',
               'Connection':'keep-alive',
               'Host':'kaijiang.500.com',
               'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36 QQBrowser/4.1.4656.400'}


class GetLishiData():
    def __init__(self,cp_type):
        pass
        #print(self._url)
        self._req =None
        self._cp_type = cp_type
        self.number_list = []
        self.url_list =[]
        self._url = ''
        self.thread_list =[]

    def parserHtml(self):

        if len(self.url_list) > 0 :
            self._url =  random.choice(self.url_list)
            idx = self.url_list.index(self._url)
            self.url_list.pop(idx)
        print('解析URL：'+self._url)

        time.sleep(random.randint(1,5))
        print('请求数据中。。。')
        self._req = reqs.session()
        html = reqs.get(self._url,headers=headers)
        html.encoding='utf8'


        soup = BeautifulSoup(html.text,'lxml')
        for r in soup.select('row'):
            qs=r['expect']
            hm=''.join(r['opencode'].split(','))
            #print(qs,hm)
            self.number_list.append(qs+' '+hm)
        print('数据解析完成。')
        #print(self.number_list)


    def starts(self,thread_count = 1):
        if len(self.url_list)<=0 :
            print('URL列表是空的，请先执行getURL函数')
            exit(0)
        for i in range(thread_count):
            t = threading.Thread(target = self.parserHtml ,name = self._cp_type+' 线程 '+ str(i))
            self.thread_list.append(t)
            print('线程',t.name+'-','启动')

        for j in self.thread_list:
            j.start()
            j.join()


    def getUrl(self,*date):
        start=arrow.get(date[0],'YYYYMMDD')
        if len(date)==2:
            end = arrow.get(date[1] ,'YYYYMMDD')
        else:
            end = start
            #print(start,end)
        while start <= end:
            sd = start.format('YYYYMMDD')
            start = start.shift(days=+1)

            if self._cp_type=='cqssc':
                self._url=cqurl+ sd +'.xml?'
            else:
                self._url=url+ self._cp_type+'/'+sd+'.xml?'
            self.url_list.append(self._url)
            #print(self._url)

print('---------必须要用线程池------------')
db = sscDB.DataBase('cp.db')
db.connectDB()
# exit(0)
cq = GetLishiData(ssclist['cq'])
cq.getUrl('20180101')
cq.starts(1)


cq.number_list.sort()
print('-' * 50)
print(cq.number_list)
print('-' * 50)
db.insert_data(cq._cp_type,cq.number_list)
print('执行完成')










