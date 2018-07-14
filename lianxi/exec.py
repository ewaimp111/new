#!/usr/bin/env python3

import  arrow
from faker import *
print('hello',arrow.now())
f = Faker(locale='zh-cn')
print(f.name(),f.address())