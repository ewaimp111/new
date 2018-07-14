#!/usr/bin/env python3

from packed1 import parser
#从包的init中导入parser模块
from packed1 import DataFenxi
#从包的init中导入datafenxi中的DataFenxi类

#  #直接导入模块
from packed1 import th

atest = parser.Atest('aaaa')
atest.prints()

btest =parser.Btest('bbb')
btest.printB()

df = DataFenxi('重庆彩票分析')
df.start()

t = th.Threads('aaa')
t.start()



