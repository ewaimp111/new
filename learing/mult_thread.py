#!/usr/bin/env python3

import threading
import time
import random


l = list(range(1,8))
l1 =[]
print(l)
def test(n):
    for x in range(n):
        if len(l)<=0:
            break
        i = random.choice(l)
        l1.append(i)
        idx = l.index(i)
        l.pop(idx)
        print('------------------')
        print('当前线程：'+threading.current_thread().getName()+'  pop: ' ,i)
        print('l1 : ' ,l1)
        print('l : ',l)
        time.sleep(0.01)


threadlist = []

for i in range(2):
    t = threading.Thread(target= test ,args=(5,),name='线程：'+str(i))
    threadlist.append(t)

for t1 in threadlist:
    t1.start()
    #t1.join()
# print('列表L',l)
# print('列表L1',l1)
print('main end')
