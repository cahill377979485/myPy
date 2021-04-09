#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time : 2021/4/6 15:51
# @File : 测试爬取一张图片.py
# @Author:https://ae01.alicdn.com/kf/Ue16c54cac6574a06a0c1afdad979b007W.jpg

import urllib.request
import os
import urllib
import time

if __name__ == '__main__':
    path = 'E:\\myPy\\{0}{1}'.format(time.strftime('%Y-%m-%d', time.localtime()), '测试下载图片')  # 设置图片的保存地址
    if not os.path.isdir(path):
        print('创建保存资源的文件夹路径')
        os.makedirs(path)  # 判断没有此路径则创建
    paths = path + '\\'
    #  防反爬虫
    url = 'https://ae01.alicdn.com/kf/Ue16c54cac6574a06a0c1afdad979b007W.jpg'
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent',
                          'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36')]  # 必须用数组装元组，方法的源码要求的
    urllib.request.install_opener(opener)
    filename, header = urllib.request.urlretrieve(url, '{0}{1}.jpg'.format(paths, 1))
    print(filename, header)
