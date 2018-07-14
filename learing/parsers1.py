#!/usr/bin/env python3
import arrow
import time
import requests
from bs4 import BeautifulSoup
from sscDB import DataBase as DB

CAIZHONG = {'cq':'cqssc','xj':'xjssc','jx':'jxssc','tj':'tjssc','yn':'ynssc','hlj':'hljssc'}

def geturl(caizhong = None,getcount =30) :
    _url1='https://www.km28.com/gp_chart/'
          #https://www.km28.com/gp_chart/cqssc/1.html
    _url2='1/'
    _url3='.html'
    url = _url1+caizhong+_url2+str(getcount)+_url3
    return url


class ParserData():
   def __init__(self,caizhong):
       self._caizhong = caizhong
       self.curr =''
       self.next =''
       self.number =''
       self.date =''
       self.lishi_numlist = []
       self.curr_numlist = []
       self.db = DB('/Users/BigZeus/PycharmProjects/notes/ssc/cp.db')
       self.db.connectDB()

       print('ParserData 类初始化完成...')

   def save_to_database(self): #保存到数据库
       # for i in self.lishi_numlist:
       #     qs,hm = i.split()
          # print(qs,'-',hm)
       self.db.insert_data('cqssc',self.lishi_numlist)

   def query(self,t):
        L=self.db.query_data(t)
        for l in L:
            a,b = l[0],l[1]
            print('x',a,b)



   def htmlTolist(self,count=1,isappend = False): #isappend 是否追加新数据到历史列表
       print('HTML数据获取中...')
       res = requests.get( geturl(self._caizhong,count) )
       res.encoding = 'utf-8'
       soup = BeautifulSoup(res.text,'html.parser')
       alink = soup.select('.t_tr2')
       print('HTML解析完成')
       for link in alink:
           s = link.text
           #print(s)
           self.curr = s[:3]
           self.date = s[3:14]
           self.number=s[15:20]
           if count == 1 :
              self.curr_numlist=['%s %s' %(self.date,self.number)]
              if not isappend:
                  if len(self.lishi_numlist) >1:
                      self.lishi_numlist.pop(0)
           self.lishi_numlist.append('%s %s'%(self.date,self.number))

       print('--------打印历史号码-------')
       print(self.lishi_numlist)
       print('------------保存数据-------')
       self.save_to_database()

       #self.query('cqssc')
       #self.db.delete_data('cqssc')
       #print('删除成功')




# data = DataGet(CAIZHONG['cq'])
# data.htmlTolist(1)
# print( data.get_next(data.curr))


class TimeProcess():
    '''
    时间截和日期相互转换
    '''

    def get_fix_timestamp(self,fix_date):  # 转换固定时间到时间截
        now=arrow.now()
        da1=now.format('YYYY-MM-DD')
        dt=da1+' '+fix_date
        r1=arrow.get(dt)
        return r1.timestamp

    def get_curr_timestamp(self):
        now=arrow.now()
        da1=now.format('YYYY-MM-DD')
        dt=da1+' '+now.format('HH:mm:ss')
        r1=arrow.get(dt)
        return r1.timestamp

    def timestampTotime(self,timestamp):  # 时间截转换到时间格式
        st=arrow.get(timestamp)
        return st.format('HH:mm:ss')

    def get_timegap(self,stamp1,stamp2):  # 计算两个时间截的差
        st=stamp1-stamp2
        r=arrow.get(st)
        return st


class Timers():
    '''
    数据更新时间等处理
    '''
    parser_data=ParserData(CAIZHONG['cq'])
    parser_data.htmlTolist(50)




    def __init__(self,utime):

        self.param={}  # 参数字典
        self.param['refresh_time']=utime  # 循环间隔刷新开奖时间
        self.param['update_intval']=0  # (5,10,0)   #开奖时间类型，白天10分钟一期，晚上5分钟
        self.param['refresh_remain_time']=0  # (540 240 0) #数据更新后等待刷新时间
        self.aw=''
        self.__refresh_time=utime
        self.__refresh_remain_time=0
        self.dp=TimeProcess()

        self.loop_stop = True
        self.wait_time = True
        print('Timers 定时器类初始化完成...')

    def __get_refresh_remain_time(self):
        aw=arrow.now()
        sys_time=aw.format('HH:mm:ss')
        if (sys_time>='09:50:00') and (sys_time<='22:00:00'):
            self.param['update_intval']=10

        elif (sys_time>='01:55:00') and (sys_time<='09:50:00'):
            self.param['update_intval']=0

        else:
            self.param['update_intval']=5

        if self.param['update_intval']==10:  # 如果数据更新间隔时间是10分钟一期
            self.param['refresh_remain_time']=540
            self.__refresh_remain_time=540
        elif self.param['update_intval']==5:
            self.param['refresh_remain_time']=240
            self.__refresh_remain_time=240
        else:
            # 获取开奖时间减去现在的时间
            d1=self.dp.get_fix_timestamp('09:50:00')
            d2=self.dp.get_curr_timestamp()
            s=self.dp.get_timegap(d1,d2)
            self.param['refresh_remain_time']=s
            self.__refresh_remain_time=s  # 剩余开奖刷新时间

        # print(self.__refresh_remain_time)
        return self.__refresh_remain_time


    def start(self):
        print('程序开始。。。。')
        self.__get_refresh_remain_time()  # 获取开奖间隔分钟，剩余刷新时间等
        if self.param['update_intval']==0:
            self.wait_time = False
            self.waitTime()
        else:
            now=arrow.now()
            fz=int(now.format('mm'))
            # print(fz)
            if self.param['update_intval']==10:
                self.__refresh_time=(10-(fz%10))*60
            elif self.param['update_intval']==5:
                self.__refresh_time=(5-(fz%5))*60
            self.loop_stop = False
            self.loopRefresh()


    def waitTime(self):
        self.__get_refresh_remain_time()  # 获取开奖间隔分钟，剩余刷新时间等
        print('执行waittime函数中。。。')
        while not self.wait_time:
            print('-------剩余更新时间:',self.dp.timestampTotime(self.__refresh_remain_time),'-------')
            self.__refresh_remain_time -= 1
            if self.__refresh_remain_time <= 0:
                self.__get_refresh_remain_time()  # 获取开奖间隔分钟，剩余刷新时间等

                if self.param['update_intval']==0:
                    self.loop_stop = True
                    self.wait_time=False
                    self.waitTime()
                else:
                    self.loop_stop = False  # 循环停止
                    self.loopRefresh()
                    self.wait_time = True

            time.sleep(1)

    def loopRefresh(self):
        while not self.loop_stop:  # 这里可以执行 has_update函数
            print('循环刷新时间：',self.dp.timestampTotime(self.__refresh_time))
            self.__refresh_time -= 1
            if self.__refresh_time <= 0:
                self.__refresh_time=self.param['refresh_time']  # 刷新时间更新正常
                if self.parser_data.has_next_update():  #检查更新是否完成
                    self.wait_time=False
                    self.waitTime()
                    self.loop_stop=True  # 循环停止
            time.sleep(1)

    def get_remain_time(self,times):

        d1=self.dp.get_fix_timestamp(times)
        d2=self.dp.get_curr_timestamp()
        s=self.dp.get_timegap(d1,d2)
        return timestampTotime(s)
