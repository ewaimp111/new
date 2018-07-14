#!/usr/bin/env python3
# -*- coding: gb2312 -*-
# -*- coding: cp936 -*-
# -*- coding: encoding -*-
import threading
import time,sys
import arrow,sys,os
a = arrow.now()
print(sys.path)



print('学习git吧所有文件备份')


print('删除本机的python2.7，用全新的python3')


# sys.path.append('/usr/local/lib/python2.7/site-packages')
# print(sys.path)
exit(0)
print(a.format('YYYY-MM-DD'))
s = 30
ss ='打印'
while s > 0:
    sys.stdout.write('\rss %d' % (s))
    s -= 1
    print('打印',s)
    time.sleep(1)
    #print(s)

sys.stdout.flush()