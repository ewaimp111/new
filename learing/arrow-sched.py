#!/usr/bin/env python3

import arrow
import time,sched,threading
import schedule

t=arrow.now()
print('年:%s-月%s-日%s 时%s:分%s:秒%s 星期:%s' % (t.year,t.month,t.day,t.hour,t.minute,t.second,t.week))

ft = t.format('HH:mm:ss')
ct = '20:00:00'

print(ft,ct)
if ft>ct :
    print('大于')
else:
    print('小于')

t1 = arrow.now()
t1=t1.shift(minutes=10)
t1=t1.shift(days=3)

st=t1.format('HH:mm:ss')

#------------sched--------


# 被调度触发的函数
def event_func(msg):
    print("当前时间:",st,'msg:',time.time())



    # 初始化sched模块的scheduler类
s=sched.scheduler(time.time,time.sleep)
    # 设置两个调度
s.enter(1,2,event_func,("Small event.",))
s.enter(2,1,event_func,("Big event.",))
s.run()

#----------------threading.Timer
def printHello():
    print("start")

timer = threading.Timer(1,printHello)
#timer.start()

#----------------schedule定时调度
import os
def show_ospath(s):
    print(os.system('ls'),s)

schedule.every(2).seconds.do(show_ospath,'test')
while True:
    schedule.run_pending()
    time.sleep(10)
















