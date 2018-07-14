#!/usr/bin/env python3
import json
import collections as cl
# 1 defaultdict
#
# 2 OrderedDict
#
# 3 deque
#
# 4 ChainMap
#
# 5 Couter
#
# 6 nametuple
#-------计数器Counter----------

l1=['a','b','c','e','c','a','b','a']
l2=[1,2,3,2,1,3,1,3,4,5]
d = dict(fonts ='red',fg = 'blue', bg ='yellow')
d1 = {'a':1 ,'b' :2 , 'a':2}


print('------------counter操作列表-----------')
print('原列表: ',l1)
r1 = cl.Counter(l1)
print('返回的是counter字典：',json.dumps(r1,indent=4))
print('返回的是counter列表: ',r1.most_common())
print('-----------counter操作列表----------')
#按照元素出现的次数进行从高到低的排序,返回前int个元素的字典

r2 = cl.Counter(l2)
print('原列表: ',l2)
print('counter统计后的字典：',json.dumps(r2,indent=4))
print('counter统计后的列表: ',r2.most_common(5))
print('排序后的counter列表：',sorted(r2.elements()))
#返回经过计数器Counter后的元素,返回的是一个迭代器

print('----------------counter操作字典--------------')
print('原字典: ',d1)
r3 = cl.Counter(d1.items())
print('counter统计后的字典：',r3,)
print('counter统计后的列表：',r3.most_common(),'\n')


print('-------------deque队列----------')
s='abc123123'
rs = cl.deque(s)
print('打印队列：',rs)
rs.appendleft('leftadd') # 左边添加
rs.append('rightadd')     # 末尾添加
print(rs,'统计s中字符1的个数为：',rs.count('1'))
ss = print('弹出的元素为：',rs.pop())          #弹出元素，默认末尾的
rs.rotate(2)
print('移动2位deque队列：',rs)

print('---------------格式化--------------')
print('格式化:{0} 结果为{1:>010.2f}'.format(s,23.232123))
print('格式化浮点数：%05.3f 格式化整数：%010d' % (23.24234,20))


print('----------有序字典OrdereDict------------')
#有序字典
dic=cl.OrderedDict
dic={1:'a',2:'c'}
dic[3]='e'
print('有序字典结果：%s' % dic)


print('---------元祖NameTuple ---------------')
#命名元祖

data = cl.namedtuple('data',['curr','next','number'])

data.curr='001'
data.next='002'
data.number ='34232'

print('当前期数：',data.number,data.next,data.curr,)

print('-------------有序字典生成缺省数据-------------')

#dd = cl.OrderedDict.fromkeys('abcdef',2)
dd = cl.OrderedDict.fromkeys('abcdef',2)
print(dd.items())
dds = ''.join(dd.keys())
print('连接字典所有key:',dds)
dd['g'] =5
print('弹出数据popitem参数last =False 先进先出：',dd.popitem(last =False))
print('字典：',dd.items())

