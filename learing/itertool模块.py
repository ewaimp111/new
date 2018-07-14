#!/usr/bin/env python3

import itertools as it

def back():
    print('\n---------------')

#------count 无限迭代
for i in it.count(0,5):
    if i>60 :
        break
    print('迭代值：%d' % i,end=' ')


#------cycle 无限迭代一个序列
back()
x = it.cycle('ABC')
c = 0
for i in x:
    c += 1
    if c>10 :
        break
    print('迭代值：%s' % i,end=' ')

#------repeat 无限迭代一个元素
back()
x = it.repeat('ABC',10)
for i in x:
    print('迭代值：%s' % i,end=' ')

#------chain iterables为一个或多个可迭代序列
back()
a=(1,2,3)
l=['a','b','c']
x = it.chain(a,l)
for i in x:
    print('chain值为:%s' % i,end=' ')
back()

#-------combinations返回连续长度为r的的迭代器(对象)

s = '012'
x = it.combinations(s,3)
l = list(x)
print('组合为：',l,len(l))

back()
x = it.permutations(s,3)
l = list(x)
print('组合为:',l,len(l))

back()
x = it.combinations_with_replacement(s,3)
l = list(x)
print('组合为:',l,len(l))

back()

#--------group把迭代器中相邻的重复元素挑出来放在一起：

x = it.groupby('11112222333333344511')
for idx,i in x:
    print(idx,list(i))

