#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :process_sync.py
# @Time      :8/31/2023 11:15
# @Author    :Kenny


import os
import time
import random
from multiprocessing import Process,Lock

def work(lock, n):
    lock.acquire()
    print('%s: %s is running' %(n, os.getpid()) )
    time.sleep(random.random())
    #time.sleep(1)
    print('%s:%s is done' %(n, os.getpid()))
    lock.release()

if __name__ == "__main__":
    lock = Lock()
    for i in range(3):
        p = Process(target=work, args=(lock,i))
        p.start()
