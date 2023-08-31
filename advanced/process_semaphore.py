#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :process_semaphore.py
# @Time      :8/31/2023 15:25
# @Author    :Kenny


from multiprocessing import Process
from multiprocessing import Semaphore
import time
import random

def go_ktv(sem, user):
    sem.acquire()
    print('%s 占坑' %user)
    time.sleep(random.randint(0, 3))
    sem.release()

if __name__ == '__main__':
    sem = Semaphore(4)
    p_1 = []
    for i in range(13):
        p = Process(target=go_ktv, args=(sem,'user%s' %(i+1),))
        p.start()
        p_1.append(p)
    for i in p_1:
        i.join()
    print('===========')