#!/usr/bin/env python3
'''
解析html标签的库
两种解析库，1，lxml，2，html-parser
'''
import lxml.html
from bs4 import BeautifulSoup
import requests

etree = lxml.html.etree  #声明etree
txt = requests.get('https://www.ittime.com.cn/news/zixun.shtml')
txt.encoding = 'utf8'
soup =BeautifulSoup(txt.text,'lxml')
#res = soup.select('.newsList > dd > h2')


print(soup.h2.string)


