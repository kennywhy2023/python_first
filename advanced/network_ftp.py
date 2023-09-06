#!/usr/bin/env python
#-*- coding: UTF-8 -*-


from ftplib import FTP

def ftpconnect(host, username, password):
    ftp = FTP()
    ftp.connect(host, 21)
    ftp.login(username, password)
    return ftp

def downloadfile(ftp, remotepath, localpath):
    bufsize = 1024
    fp = open(localpath, 'wb')
    ftp.retrbinary('RETR' + remotepath, fp.write, bufsize)
    fp.close()

def uploadfile(ftp, remotepath, localpath):
    bufsize = 1024
    fp = open(localpath, 'rb')
    ftp.storebinary('STOR' + remotepath, fp, bufsize)
    fp.close()

if __name__ == "__main__":
    ftp = ftpconnect('***','***','***')
    downloadfile(ftp,'***','***')
    uploadfile(ftp, '***', '***')
    ftp.quit()