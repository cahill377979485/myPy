#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time : 2021/4/14 11:03
# @File : 通用图片爬虫.py
# @Author:

import re
import os
import time
import threading
import requests
import random


class Command(object):

    def __init__(self, name, url, reg, use_headers=False):
        self.name = name
        self.url = url
        self.reg = reg
        self.use_headers = use_headers


def get_headers_with_random_ua():  # 定义一个随机UA的子程序
    headers_list = [  # 定义一个UA列表，UA可以在百度搜索到
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
        "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
        "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
    ]
    headers = {'User-Agent': random.choice(headers_list)}  # choice是random包的一个方法，是从列表中随机取一个值
    return headers


def get_path_mid(path_name):
    return '{0}{1}{2}'.format('E:\\myPy\\', time.strftime('%Y-%m-%d', time.localtime()), path_name)


def get_res_code(the_command, the_semaphore):
    the_semaphore.acquire()
    if the_command.use_headers:
        res_code = requests.get(the_command.url, headers=get_headers_with_random_ua()).text
    else:
        res_code = requests.get(the_command.url).text
    print('获取到的网页源码为：\n%s' % res_code)
    img_list = re.compile(the_command.reg).findall(res_code)
    size = len(img_list)
    print('通过正则表达式共找到%d张图片' % size)
    x = 1  # 声明一个变量赋值
    path_mid = get_path_mid(the_command.name)
    if not os.path.isdir(path_mid):
        print('创建保存资源的文件夹路径')
        os.makedirs(path_mid)  # 判断没有此路径则创建
    path_final = path_mid + '\\'
    time_start = time.time()
    for img_url in img_list:
        print('正在下载第%d张/%d 用时%s' % (x, size, time.time() - time_start))
        absolute_path = '{0}{1}.jpg'.format(path_final, x)
        if os.path.isfile(absolute_path):
            x = x + 1
            continue
        try:
            with open(f'{absolute_path}', 'wb') as file_data:
                print("正在下载图片")
                file_data.write(requests.get(img_url).content)
        except Exception as e:
            print('第%d张/%d出错，原因是：%s' % (x, size, e.__cause__))
        finally:
            x = x + 1
    print('图片下载完成，注意查看文件夹%s 用时%s' % (path_final, time.time() - time_start))
    print(img_list)
    the_semaphore.release()


if __name__ == '__main__':
    command_list = [
        Command('站酷总榜前100项目图片',
                'https://www.zcool.com.cn/top/index.do',
                r'(?<=src=")https://img\.zcool\.cn.{40,42}\.jpg'),
        Command('站酷最近APP设计项目图片',
                'https://www.zcool.com.cn/discover.json?cate=17&subCate=757&hasVideo=0&city=0&college=0&recom',
                r'(?<=cover\":\")https://img\.zcool\.cn.{40,41}\.jpg(?=")')
    ]
    # 选择要执行的命令
    command = command_list[0]
    semaphore = threading.BoundedSemaphore(5)
    t = threading.Thread(target=get_res_code, args=(command, semaphore))
    t.start()
    while threading.active_count() != 1:
        pass
    else:
        print('全部图片下载完毕')
