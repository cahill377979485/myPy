#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time : 2021/4/13 18:04
# @File : 爬取分段视频并合成.py
# @Author:

import requests
import re
import json
import os
from threading import Thread
import sys

import time

requests.packages.urllib3.disable_warnings()


def progress():
    width = 30
    while True:
        global all_num
        global now_num
        percent = now_num / all_num * 100
        left = int(width * percent // 100)
        right = width - left
        print('\r[', '#' * left, ' ' * right, ']', f' {percent:.0f}%', sep='', end='', flush=True)
        if all_num == now_num:
            break
        time.sleep(1)


def hecheng(sh, path):
    # 判断是否只是一段视频
    if len(os.listdir(path)) <= 2:
        os.remove(path + os.sep + "1.txt")
    else:
        os.system(sh)
        for i in os.listdir(path):
            if i != 'output.mp4':
                os.remove(path + os.sep + i)


def download(url, id_, name):
    global now_num
    data = requests.get(url, headers={"Range": "bytes=0-"}, stream=True).content
    with open(name + os.sep + str(id_) + '.mp4', 'wb') as f:
        f.write(data)
    now_num += 1


def api_get(id_):
    global all_num
    global now_num
    all_num = 0
    now_num = 0

    api_url = f"https://web-play.pptv.com/webplay3-0-{id_}.xml?o=0&version=6&type=mhpptv&appid=pptv.web.h5&appplt=web&appver=4.0.7&cb=a"
    s = requests.get(api_url, verify=False, headers=headers)
    data = json.loads(s.text[2:-4])
    try:
        name = data['childNodes'][2]['nm']
    except Exception:
        name = data['childNodes'][0]['nm']
    print("正在下载:" + name)

    rid = data['childNodes'][-4]['rid']
    all_num = len(data['childNodes'][-4]['childNodes']) - 1
    kk = data['childNodes'][-5]['childNodes'][-1]['childNodes'][0].split('%26')[0]
    if not os.path.exists(name):
        os.makedirs(name)

    # 合成命令
    a1 = os.path.abspath(name + os.sep + '1.txt')
    a2 = os.path.abspath(name + os.sep + 'output.mp4')
    sh = f'ffmpeg -f concat -safe 0 -i "{a1}" -c copy "{a2}" -loglevel error'
    path = os.path.dirname(a1)

    # 启动进度条线程
    progress_t = Thread(target=progress)
    progress_t.start()

    t_list = []
    t_list.append(progress_t)

    f = open(name + os.sep + '1.txt', 'w')
    for i in range(all_num):
        video_url = f"https://10314.vcdn.pplive.cn/{i}/0/1/{rid}?h5vod.ver=2.1.3&k={kk}&type=mhpptv"
        f.write("file " + os.path.abspath(name + os.sep + f'{i}.mp4') + "\n")

        t = Thread(target=download, args=(video_url, i, name))
        t_list.append(t)
        t.start()

        if not mul_t:
            t.join()

    f.close()
    for t in t_list:
        t.join()

    # print(sh)
    print("\n" + name + " 正在合成...")
    hecheng(sh, path)
    print(name + " 合并成功")


def start(url, is_all, s, e, mul_t):
    response = requests.get(url, verify=False, headers=headers)
    if response.status_code == 200:
        result = re.findall("var webcfg = (.*?);", response.text)
        data = json.loads(result[0])

        if is_all:
            # 下载剧集
            try:
                for item in data['playList']['data']['list'][s - 1:e]:
                    api_get(item['id'])
            except Exception:
                for item in data['playList']['data']['list']:
                    api_get(item['id'])
        else:
            # 下载单集
            api_get(data['id'])


if __name__ == "__main__":
    all_num = 0
    now_num = 0
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
    }

    url = input("输入地址:")
    is_all = input("是否下载全剧(默认否):")
    if is_all:
        r = input("请输入下载剧集(例如1-5,默认全部):")
        if r:
            s, e = r.split("-")
            s = int(s)
            if e:
                e = int(e)
            else:
                e = None
        else:
            s = None
            e = None

    mul_t = input("是否启用多线程下载(默认否):")
    start(url, is_all, s, e, mul_t)
