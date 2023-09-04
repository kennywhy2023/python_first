#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :database_mysql.py
# @Time      :9/4/2023 9:32
# @Author    :Kenny

import MySQLdb

db = MySQLdb.connect(host='10.13.2.4', port=3307, user='root', password='123456',
                    db='mydb',charset='utf8')
cursor = db.cursor()
#cursor.execute("show tables;")
#data = cursor.fetchone()
#data = cursor.fetchall()
#for t in data:
#    print(t)

cursor.execute("select * from emp;")
data = cursor.fetchall()
for row in data:
    print(row)
db.close()
