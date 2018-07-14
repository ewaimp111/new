#!/usr/bin/env python3
# -*- coding: gb2312 -*-
# -*- coding: utf-8 -*-

import threading
import time
import random
import requests
import datetime
from bs4 import BeautifulSoup
import net_init_

"""
1��ץȡ���̴�����վ�Ĵ���ip
2��������ָ����Ŀ��url,��ץȡ��ip����Ч�Խ�����֤
3�����浽ָ����path
"""
targeturl = 'https://www.baidu.com'
# ------------------------------------------------------�ĵ�����--------------------------------------------------------
# д���ĵ�
def write(path,text):
    with open(path,'a') as f:
        f.writelines(text)
        f.write('\n')
# ����ĵ�
def truncatefile(path):
    with open(path, 'w') as f:
        f.truncate()
# ��ȡ�ĵ�
def read(path):
    with open(path, 'r') as f:
        txt = []
        for s in f.readlines():
            txt.append(s.strip())
    return txt
# ----------------------------------------------------------------------------------------------------------------------
# ����ʱ���,��ʽ: ʱ����
def gettimediff(start,end):
    seconds = (end - start).seconds
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    diff = ("%02d:%02d:%02d" % (h, m, s))
    return diff
# ----------------------------------------------------------------------------------------------------------------------
# ����һ�����������ͷ headers

# -----------------------------------------------------���ip�Ƿ����----------------------------------------------------
def checkip(ip):
    headers =net_init_.getheaders()  # ��������ͷ
    proxies = {"http": "http://"+ip, "https": "http://"+ip}  # ����ip
    #print(proxies['http'])
    #print(proxies['https']) #http://119.10.67.144:808
    try:
        response=requests.get(url=targeturl,proxies=proxies,headers=headers,timeout=5).status_code
        if response == 200 :
            return True
        else:
            return False
    except:
        return False

#-------------------------------------------------------��ȡ������----------------------------------------------------
# ��Ѵ��� XiciDaili
x = 0
def findip(type,pagenum,path): # ip����,ҳ��,Ŀ��url,���ip��·��
    list={'1': 'http://www.xicidaili.com/nt/', # xicidaili������ͨ����
          '2': 'http://www.xicidaili.com/nn/', # xicidaili���ڸ������
          '3': 'http://www.xicidaili.com/wn/', # xicidaili����https����
          '4': 'http://www.xicidaili.com/wt/'} # xicidaili����http����
    url=list[str(type)]+str(pagenum) # ����url
    headers = net_init_.getheaders() # ��������ͷ
    html=requests.get(url=url,headers=headers,timeout = 5).text
    soup=BeautifulSoup(html,'lxml')
    all=soup.find_all('tr',class_='odd')

    for i in all:
        t=i.find_all('td')
        ip=t[1].text+':'+t[2].text
        addr = '��  ַ  : '+ t[3].text
        typ  = '��  ��  : '+t[4].text
        https ='h t t p : '+t[5].text
        able  ='��Ч��  : '+t[8].text
        td  =  'ʱ  ��  : '+t[9].text

        is_avail = checkip(ip)
        if is_avail == True:

            write(path=path,text=ip)
            print('-------������ȡ��{}��--------'.format(x))
            print(ip)
            print(''.join( addr.split('\n')))
            print(typ)
            print(https)
            print(able)
            print(td)


#-----------------------------------------------------���߳�ץȡip���---------------------------------------------------
def getProxyIp(path):
     truncatefile(path) # ��ȡǰ����ĵ�
     start = datetime.datetime.now() # ��ʼʱ��
     threads=[]
     for type in range(4):   # ��������ip,ÿ������ȡǰ��ҳ,��12���߳�
         time.sleep(random.randint(3,10))
         for pagenum in range(1):  #��ȡҳ��
             t = threading.Thread(target=findip,args=(type+1,pagenum+1,path))
             threads.append(t)
     print('��ʼ��ȡ����ip')
     for s in threads: # �������߳���ȡ
         s.start()

     for e in threads: # �ȴ������߳̽���
         e.join()
     print('��ȡ���')
     end = datetime.datetime.now() # ����ʱ��
     diff = gettimediff(start, end)  # �����ʱ
     ips = read(path)  # ��ȡ������ip����
     print('һ����ȡ����ip: %s ��,����ʱ: %s \n' % (len(ips), diff))
     return ips
#-------------------------------------------------------����-----------------------------------------------------------
if __name__ == '__main__':
    path = 'ip.txt'
    getProxyIp(path)

# if checkip('119.10.67.144:808'):
#     print('yes')
# else:
#     print('no')