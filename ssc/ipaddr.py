#!/usr/bin/env python3
# -*- coding: gb2312 -*-
from bs4 import BeautifulSoup

import requests
import random
import time,sys
import sendmail
import threading
import net_init_
import proxy_ip_pool

'''
从ipurl字典中的网页获取IP地址
函数：getNetIp() 获取单个url的ip
函数：getAll_NetIp() 获取所有列表中url中的ip
函数：getNetIp_timer(count=5,times=60) 定时获取全部字典中的URL的ip
'''

# 查询外网ip的网站地址
# curl ipinfo.io/ip
# curl ipecho.net/plain
# curl http://icanhazip.com/

#ip字典

IPURL = {'1':'http://ipinfo.io/ip',
         '2':'http://ipecho.net/plain',
         '3':'http://icanhazip.com/'}

# 返回一个随机的请求头 headers



def get_NetIp(urls,proxyip=''):
    headers =net_init_.getheaders()  # 定制请求头
    #proxies = {"http": "http://"+ip, "https": "http://"+ip}  # 代理ip
    proxies={"http":'http://'+proxyip,'https':'http://'+proxyip}  # 代理ip
    try:
        if proxyip == '':  #如果没有使用代理IP
            response=requests.get(url=urls,headers=headers,timeout=30)
        else:
            response=requests.get(url=urls,headers=headers,proxies =proxies ,timeout=30)

        if response.status_code == 200:
            s= response.text.strip().rstrip().lstrip()
            return s
        else:
            s ='获取IP失败!'
            print(s)
            return s
    except Exception as e:
        s ='ip请求错误'
        print(s)
        return ''


ipdata = {}
def getAll_NetIp(proxyip=''):
    for _url in IPURL.values():
        print('请求地址：',_url)
        if proxyip == '':
            _ip=get_NetIp(_url)
        else:
            _ip = get_NetIp(_url,proxyip)
        print('ip地址：',_ip)
        ipdata.setdefault(_url,_ip)


def getNetIp_timer(count,times,proxyip=''):
    c = 0
    while c <count:
        c += 1
        print('\r定时获取外网ip地址任务第 %d 次 总执行次数: %d' % (c,count))
        t = times
        while t>0 :
            sys.stdout.write('\r剩余执行时间：%d'%(t))
            t -= 1
            time.sleep(1)
            if t <= 0:
                break
        sys.stdout.flush()
        print('')
        if proxyip =='':  #如果没有使用代理IP
            t = threading.Thread(target=getAll_NetIp)
        else:
            t = threading.Thread(target=getAll_NetIp,args=(proxyip,))
        t.start()
        t.join()
        print('-'*50)
        data=str(ipdata)
        #sendMail('home ipaddress',data)


# print(get_NetIp(IPURL['3'],'221.7.255.168:8080')) #使用代理ip去获取
# print(get_NetIp(IPURL['3']))  #不使用代理
#getAll_NetIp(proxyip='221.7.255.168:8080')
#sendMail('home ipaddress',data)

#--------------------------------------------------
proxyip_list =list()
proxyip_list = proxy_ip_pool.getProxyIp('ip.txt')
print(proxyip_list)

getNetIp_timer(count=5,times=60,proxyip=random.choice(proxyip_list))


