#!/usr/bin/env python3

import requests
import json
import requests

Base_Url='https://api.github.com'


def build_uri(end_point):
    return '/'.join([Base_Url,end_point])


def basic_auth():
    response=requests.get(build_uri('user'),auth=('ewaimp@qq.com','sg0211589'))
    print(response.status_code)
    print(response.text)
    print(response.request.headers)
# basic_auth()
#
# import base64
# s=base64.b64decode('ZXdhaW1wQHFxLmNvbTpzZzAyMTE1ODk=')
# print(s)
import  threading as thread

has_update = False
has_wait =False
c = 5
w = 10
import arrow
def loop():
    a = arrow.now()
    print('主循环:',a.format('HH:mm:ss'))
    thread.Timer(1,loop).start()
    global  has_update
    if has_update:
        print('检查更新程序启动。。。')
        checkupdate()
    if has_wait:
        print('等待程序启动。。。。')
        wait()


import time
def checkupdate():
    global has_update
    has_update = False
    global  c
    while c>0:
        time.sleep(1)
        print('更新倒计时',c)
        c-=1
        if c<=0:
            print('更新完成')
            c=5



def wait():
    global has_wait
    has_wait = False
    global  w
    while w>0:
        w -=1
        print('等待倒计时',w)
        if w<=0:
            print('等待程序完成')
            sendupdates()
        time.sleep(1)

def sendupdates():
    global has_update
    has_update = True
    print('发送更新信号')

def sendwait():
    global has_wait
    has_wait = True
    print('等待信号')


# loop()
#
# thread.Timer(5,sendupdates).start()
# thread.Timer(10,sendwait).start()
import  random
def test(a):
    for idx,i in enumerate(range(a)):
        s =random.randint(222,2222)+random.randint(111,1111)
        #print(idx,s)
    print('end---------')


t =thread.Thread(target=test,name='test',args=(100,))
t.start()
print('t------end')

t1 =thread.Thread(target=test,name='test',args=(100,))
t1.start()
print('t1------end')
t2=thread.Thread(target=test,name='test',args=(100000,))
t2.start()











