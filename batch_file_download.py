#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :batch_file_download.py
# @Time      :10/30/2023 15:15
# @Author    :Kenny

import os  # 导入os库
import urllib.request  # 导入urllib库
import requests as rb  # 导入requests库
from bs4 import BeautifulSoup  # 调用beautifulsoup库

#######文件下载
def file_downloand(fileUrl):
    # 文件基准路径
    basedir = "C:\\Users\\zzt\\Downloads\\filedownload"
    # 如果没有这个path则直接创建
    if not os.path.exists(basedir):
        os.makedirs(basedir)
    # 下载到服务器的地址
    file_path = basedir + '/' + fileUrl[fileUrl.rfind("/") + 1:len(fileUrl)]
    if os.path.exists(file_path) == False:  # 判断是否存在文件
        # 文件url
        try:
            print("下载链接：" + fileUrl)
            urllib.request.urlretrieve(fileUrl, filename=file_path)
            print("成功下载文件")
        except IOError as exception_first:  # 设置抛出异常
            print(1, exception_first)
        except Exception as exception_second:  # 设置抛出异常
            print(2, exception_second)
    else:
        print("文件已经存在！")


def get_download_url_from_page(base_url):
    fileList = []
    data = rb.get(base_url)  # 获取HTML网页，对应HTTP的GET
    soup = BeautifulSoup(data.text, "html.parser")  # 使用BeautifulSoup解析获取到的数据
    links = []  # 定义空列表links
    for link in soup.find_all("a"):
        # 输出网页中的a标签下的href内容到links中;; append()方法用于在列表末尾添加新的对象
        print(link.get("href"))
        if link.get("href").count('java') == 1:
            links.append(link.get("href"))
    for link_url in links:
        data_file = rb.get(base_url + link_url)
        soup_file = BeautifulSoup(data_file.text, "html.parser")
        for link_file in soup_file.find_all("a"):
            if str(link_file.get("href")).count('jar') == 1 and str(link_file.get("href")).count('jar.asc') != 1:
                fileList.append(base_url + link_url + link_file.get("href"))
    return fileList


if __name__ == "__main__":
    fileList = get_download_url_from_page("https://mirrors.tuna.tsinghua.edu.cn/mariadb/")
    # fileUrl = "https://unraid-dl.sfo2.cdn.digitaloceanspaces.com/stable/unRAIDServer-6.10.3-x86_64.zip"
    for fileUrl in fileList:
        file_downloand(fileUrl)
    # print(fileUrl[fileUrl.rfind("/") + 1:len(fileUrl)])
