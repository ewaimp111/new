#!/usr/bin/env python3
import time

import sys
from tqdm import tqdm

from time import sleep


def viewBar(i):
    output=sys.stdout
    s = show()
    for count in range(0,3):
        output.write('\r剩余时间：:%.0f秒  实时数据 %.s:'% (count,'a'))
        sleep(1)

    output.flush()

def show():
    return  ('001 234','002 343')

for i in range(100):

    viewBar(100)
