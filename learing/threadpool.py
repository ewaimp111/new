#!/usr/bin/env python3
from concurrent.futures import ThreadPoolExecutor,as_completed,ALL_COMPLETED,FIRST_COMPLETED,wait
from concurrent.futures import ProcessPoolExecutor
import time
import random
import threading
def task(msg):
    time.sleep(2)
    return msg


url = 'https://www.baidu.com/'

def task1(s):
    time.sleep(0.1)
    ss = s[-1:]
    #new_list.append(ss)
    print('获取页面完成！',ss)
    return s


task_list=list(map(lambda x:url+str(x),range(10)))


pool=ThreadPoolExecutor(max_workers=2)
#-------------------
all_task = [pool.submit(task1,t) for t in task_list]
# all_task =list()
# for t in task_list:
#     all_task.append(pool.submit(task1,t))
#-------------------

#wait(all_task,return_when=ALL_COMPLETED)

for x in as_completed(all_task):
    data = x.result()
    print('页面 {} 解析成功！'.format(data))


print('main')



# thread_list = ['a','b','c','d','e','f']
#
#
# #------------map---------
# print('---------map--------')
# t = time.time()
# future =  pool.map(task,thread_list)
# for f in future:
#     print('执行结果',f)
#     time.sleep(0.1)
# e = time.time()  - t
# print(e)
#
# #----------submit--------
# print('--------submit--------')
# t = time.time()
# future = pool.submit(task,thread_list)
# for f in future.result():
#     print('执行结果',f)
#     time.sleep(0.1)
# e = time.time() - t
# print(future.result() )
# print(e)