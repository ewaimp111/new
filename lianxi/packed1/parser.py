#!/usr/bin/env python3
class Atest():
    def __init__(self,name):
        self._name =name

    def prints(self):
        print('我是 file1 > A 类',self._name)


class Btest(Atest):
    def __init__(self,name):
        super().__init__(name)

    def printB(self):
        print('我是 file1 > B 类')