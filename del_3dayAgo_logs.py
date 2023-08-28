#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
此脚本用于删除指定目录下，3天以前未被更改的文件。
多用于清理日志文件
'''
import os
import os.path
import time
import datetime

logdir = "C:/ProgramData/SAP BusinessObjects/Data Services/log/JOBSERVERS/dsprd_new__user"

for parent, dirnames, filenames in os.walk(logdir):
    for filename in filenames:
        fullname = parent + "/" + filename  # 文件全称
        createTime = int(os.path.getmtime(fullname))  # 文件修改时间
        nDayAgo = (
            datetime.datetime.now() -
            datetime.timedelta(
                days=3))  # 当前时间的n天前的时间
        timeStamp = int(time.mktime(nDayAgo.timetuple()))
        if createTime < timeStamp:  # 修改时间在n天前的文件删除
            try:
                os.remove(os.path.join(parent, filename))
            except Exception as e:
                print("Error, delete file failed!")
        continue
