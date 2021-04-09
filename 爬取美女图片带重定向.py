#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time : 2021/4/7 11:45
# @File : 爬取美女图片带重定向.py
# @Author: 希尔
import urllib.request
import re
import os
import urllib
import time
import random

pages = 5
time_start = time.time()
path = 'E:\\myPy\\{0}{1}'.format(time.strftime('%Y-%m-%d', time.localtime()), '美女图片')  # 设置图片的保存地址
x = 1  # 声明一个变量记录当前的图片脚标


def handle_img_list(html):
    global x
    global pages
    global time_start
    global path
    reg = r'(?<="url":")http:\/\/gank.io\/images.{30,40}(?=",)'
    img_re = re.compile(reg)  # 转换成一个正则对象
    img_list = img_re.findall(html)  # 表示在整个网页过滤出所有图片的地址，放在imgList中
    size = pages * 10
    print('通过正则表达式共找到%d张图片' % len(img_list))
    if not os.path.isdir(path):
        print('创建保存资源的文件夹路径')
        os.makedirs(path)  # 判断没有此路径则创建
    paths = path + '\\'
    # 防反爬虫
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent',
                          'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36')]
    urllib.request.install_opener(opener)
    for img_url in img_list:
        absolute_path = '{0}{1}.jpg'.format(paths, x)
        if os.path.isfile(absolute_path):  # 如果已经有同名文件则跳过
            x = x + 1
            continue
        try:
            urllib.request.urlretrieve(img_url, absolute_path)
            print('下载完成第%d张/%d 用时%s' % (x, size, time.time() - time_start))
            time.sleep(random.randint(2, 3))  # 休眠几秒，防止下载过快
        except Exception as e:
            print('第%d张/%d出错，原因是：%s' % (x, size, e))
        finally:
            x = x + 1
    print(img_list)
    return img_list


if __name__ == '__main__':
    for page in range(pages):
        url = "https://gank.io/api/v2/data/category/Girl/type/Girl/page/" + str(page + 1) + "/count/10"
        res_code = urllib.request.urlopen(url).read().decode('utf-8')  # 获取该网页的详细信息
        print('~获取到的网页源码为：\n%s' % res_code)
        handle_img_list(res_code)  # 从网页源代码中分析下载保存图片
    print('图片下载完成，注意查看文件夹%s 用时%s' % (path, time.time() - time_start))
