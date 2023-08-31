#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :process.py
# @Time      :8/31/2023 9:25
# @Author    :Kenny


import time
from multiprocessing import Process

def f(name):
    print('hello', name)
    print('subprocess')

if __name__ == '__main__':
    p = Process(target=f, args=('start',))
    p.start()
    time.sleep(3)
    print('Mainprocess')