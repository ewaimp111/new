#!/usr/bin/env python3

import time,threading
import random
import arrow
import time
import requests
from bs4 import BeautifulSoup
from sscDB import DataBase as DB
from tqdm import *
import sys
import net_init_
CAIZHONG = {'cq':'cqssc','xj':'xjssc','tj':'tjssc','yn':'ynssc'}
def geturl(caizhong = None,getcount =30) :
    _url1='https://zst.cjcp.com.cn/cjwssc/view/ssc_zonghe2-'
    _url2='-0-3-'
    _url3='.html'
    url = _url1+caizhong+_url2+str(getcount)+_url3
    return url

#新疆001 - 096 期
#https://www.km28.com/gp_chart/tjssc/1/200.html

#天津001 - 084 期
#https://www.km28.com/gp_chart/tjssc/1/200.html

#云南001 - 072 期
#https://www.km28.com/gp_chart/ynssc/1/200.html

#重庆001 - 120 期
#https://zst.cjcp.com.cn/cjwssc/view/ssc_zonghe2-cqssc-0-3-5.html


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

class sscParser():

    def __init__(self,caizhong):
        self._c = 0
        self.hasupdate = None
        self.interval =5
        self.waittime = 0
        self.updatetime = 30
        self._caizhong=caizhong
        self.curr =''
        self.next =''
        self.number =''
        self.qishu =''
        self.lishi_numlist = []
        self._scount = 35
        self.dt = TimeProcess()
        self._arrow = arrow.now()
        self._once = True
        print('初始化参数')
        print('-'* self._scount)
        print('更新间隔时间 :',self.interval)
        print('更 新 彩 种 :',self._caizhong)
        print('-'*self._scount)
        print('')

    def calc_wait_time(self):
        self._arrow = arrow.now()
        sys_time=self._arrow.format('HH:mm:ss')

        if (sys_time>='09:50:00') and (sys_time<='22:00:00'):
            self.interval=10
        elif (sys_time>='01:55:00') and (sys_time<='09:50:00'):
            self.interval=0
        else:
            self.interval=5
        self._arrow =arrow.now()
        _fz=int(self._arrow.format('mm'))
        _mz=int(self._arrow.format('ss'))
        if self.interval == 10:  # 如果数据更新间隔时间是10分钟一期
            self.waittime = ((10-_fz%10)*60)-_mz
        elif self.interval == 5:
            self.waittime = ((5-_fz%5)*60)-_mz
        else:
            # 获取开奖时间减去现在的时间
            d1=self.dt.get_fix_timestamp('09:50:00')
            d2=self.dt.get_curr_timestamp()
            t=self.dt.get_timegap(d1,d2)
            self.waittime = t
        print('-'*self._scount)
        print('')

    def getData(self,count=1):  # isappend 是否追加新数据到历史列表
        print('HTML数据解析')
        print('-'* self._scount)
        _url = geturl(self._caizhong,count)
        print('解析URL...',_url)
        headers = net_init_.getheaders()
        res=requests.get(_url,headers=headers)
        res.encoding='utf-8'
        soup=BeautifulSoup(res.text,'html.parser')
        alink2=soup.select('.z_tr_hui')
        alink1 =soup.select('.z_tr_fen')
        print('数据解析完成')
        alink1 = alink1 + alink2
        #print(alink)
        for link in alink1:
            s=link.text
            s1 = s[1:17]
            self.qishu=s1[0:11]
            self.curr=self.qishu[8:]
            self.number=s1[11:]
            time.sleep(0.05)
            self.lishi_numlist.append('%s %s'%(self.qishu,self.number))
        _tmp =list(set(self.lishi_numlist))  #号码去重排序
        self.lishi_numlist = _tmp.copy()
        _tmp.clear()
        self.lishi_numlist.sort()
        print('获取号码列表完成')
        print(self.lishi_numlist)
        return self.lishi_numlist


        #self.save_to_database()

    def __get_next(self,prior):  # 获取下期期数

        s=int(prior)
        if self._caizhong == 'cqssc':
            if s==120:
                s=1
            else:
                s+=1
        elif self._caizhong == 'xjssc':
            if s==96:
                s=1
            else:
                s+=1
        elif self._caizhong == 'tjssc':
            if s==84:
                s=1
            else:
                s+=1
        elif self._caizhong == 'ynssc':
            if s==72:
                s=1
            else:
                s+=1
        self.next='%03d'%s

        return self.next

    def getUpdate(self):  # 检查更新期数
        print('检查是否有新数据')
        print('-'*self._scount)
        self.__get_next(self.curr)  # 获得下期期数
        self.getData()  # 参数为空只获取一条记录
        if self.curr==self.next:
            self.__get_next(self.curr)  # 获得下期期数
            print('检查完成，有新数据更新')
            print('当前期数:',self.curr)
            print('下期期数:',self.next)
            print('当前号码:',self.number)
            self.lishi_numlist.pop(0)
            self.hasupdate = True
        else:
            print('获取完成，没有数据更新')
            self.hasupdate = False

        return self.hasupdate
        print('-'*self._scount)
        print('')

    def updateLoop(self,_time ):
        for n in range(_time,1,-1):
            time.sleep(1)
            sys.stdout.write('\r[总刷新时间]--> %.0f   [剩余刷新时间]----------> %.0f ' %(_time , n))
        print('数据更新获取完成')
        sys.stdout.flush()
        #执行数据抓取过程


    def updateWait(self,_time):
        for i in range(_time,1,-1):
            time.sleep(1)
            sys.stdout.write('\r[总等待时间]--> %.0f   [等待更新时间]--> %.0f '%(_time,i))
        sys.stdout.flush()
        print('更新等待函数执行完毕')


    def mainloop(self):
        while True:
            time.sleep(1)
            self._c += 1
            #print('主循环...',self._c)
            #self.getData()
            self.getUpdate()
            if self.hasupdate:
                self.hasupdate =False
                self.calc_wait_time()
                self.updateWait(self.waittime)
            else:
                self.updateLoop(self.updatetime)  #循环刷新数据
            #self.getUpdate()

t = sscParser(CAIZHONG['cq'])


t.getData(5)      #1，获取当天新的数据
t.calc_wait_time() #2，计算剩余等待时间
t.updateWait(t.waittime) #在执行等待函数
t.mainloop()


