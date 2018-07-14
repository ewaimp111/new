#!/usr/bin/env python3

class Tools():
    def __init__(self,name):
        self._name = name

    def destion(self):
        print('我是一个工具模块，模块名字叫：',self._name)