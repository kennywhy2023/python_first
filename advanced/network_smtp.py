#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :network_smtp.py
# @Time      :9/5/2023 16:06
# @Author    :Kenny


import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host="smtp.163.com"
mail_user="XX"
mail_pass="XXXXX"
sender='XX@163.com'
receivers = ['XXX@qq.com']
message = MIMEText('邮件测试', 'plain', 'utf-8')
message['From'] = Header("XX", 'utf-8')
message['To'] = Header("X", 'utf-8')
subject = 'SMTP邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("发送成功")
except smtplib.SMTPException:
    print("发送失败")