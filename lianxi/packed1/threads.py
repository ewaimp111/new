#!/usr/bin/env python3

import arrow

class Threads():
    def __init__(self,name):
        self.name= name

    def start(self):
        print('我是线程模块',self.name,'run:',arrow.now())