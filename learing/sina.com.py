#!/usr/bin/env python3
from threading import Thread
import  time

'''
解析新浪新闻
'''
from bs4 import BeautifulSoup
import requests
import json
res = requests.get('http://api.roll.news.sina.com.cn/zt_list?channel=news&cat_1=gnxw&cat_2==gdxw1||=gatxw||=zs-pl||=mtjj&level==1||=2&show_ext=1&show_all=1&show_num=22&tag=1&format=json&page=6&callback=newsloadercallback&_=1528559444110')
res.encoding = 'utf8'
jd = json.loads(res.text.lstrip('  newsloadercallback(').rstrip(');'))

ss =jd['result']['data']
for s in ss:
    print(s['title'])
    print(s['url'])
#print(ss)是

t = 'www.baidu.com/index{}/{}.html'

print(t.format(5,'s'))
