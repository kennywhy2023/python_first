#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :process_inherit.py
# @Time      :8/31/2023 10:45
# @Author    :Kenny


from multiprocessing import Process
import os
import time

class Download(Process):
    def __init__(self, interval):
        Process.__init__(self)
        self.interval = interval

    def run(self):
        t_start = time.time()
        print('start process: %s download' %os.getpid())
        print('child process(%s) start, father process(%s)' %(os.getpid(), os.getppid()))
        time.sleep(self.interval)
        t_stop = time.time()
        print('child process(%s) runned over, elapsed time %f seconds'%(os.getpid(), t_stop-t_start))

if __name__ == '__main__':
    t_start = time.time()
    print('current process(%s)' %os.getpid())
    p = Download(2)
    p.start()
    time.sleep(10)
    t_stop = time.time()
    print('father process(%s) runned over, elapsed time %f seconds'%(os.getpid(), t_stop-t_start))