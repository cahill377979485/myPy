#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time:2021/4/17 9:51
# @File:整合版借还记录支付宝收益2.0.py
# @Author:希尔
# @Email:377979485@qq.com
# @Desc:优化点
# 1、获取余额宝收益信息增加本地缓存，如果发现今天已经有数据了就不需要从接口获取，直接从本地文件中获取数据。
# 2、增加可设置开始计算收益的时间。
# 3、增加无收益时的曲线和有收益的曲线，方便对比。

import json

import requests
import datetime
import matplotlib.pyplot as plt
import warnings
import pandas as pd
import numpy as np
import os


class Record(object):

    def __init__(self, date, money, the_sum):
        self.date = date
        self.money = money
        self.the_sum = the_sum


class Gain(object):

    def __init__(self, date, gain):
        self.date = date
        self.gain = gain


def get_gain_every_day():
    list_bean = []
    date_start = '2016-02-01'
    date_yesterday = (datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    file_name = r'D:\myPy\借还记录\余额宝每日万份收益.txt'

    # 内部方法，需放在方法调取之前，不然不能使用：从网站下载
    def get_from_net():
        url = f'http://api.fund.eastmoney.com/f10/lsjz?callback=jQuery183023336459069593007_1618390055881&fundCode=000198&pageIndex=1&pageSize=2000&startDate={date_start}&endDate={date_yesterday}&_=1618390082880'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36 SE 2.X MetaSr 1.0',
            'Referer': 'http://fundf10.eastmoney.com/jjjz_000198.html'
        }
        response = requests.get(url, headers=headers).text
        start = response.find(r'(')
        end = response.find(r')')
        final_response = response[start + 1:end]
        dicts = json.loads(final_response)
        for item in dicts['Data']['LSJZList']:
            list_bean.append(Gain(item['FSRQ'], item['DWJZ']))
        with open(file_name, 'w+') as f:
            for item in list_bean:
                f.write('%s %f\n' % (item.date, float(item.gain)))
            f.close()

    #  如果本地有每日收益文件则打开文件，如果文件包含昨天的数据则直接解析数据集合。
    #  如果本地没有每日收益文件或者文件不包含昨天的数据则通过网站下载最新的数据。并以最新的数据来生成集合并保存到本地。
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            lines = file.readlines()
            if lines[0].__contains__(date_yesterday):
                for line in lines:
                    arr = line.split(' ')
                    list_bean.append(Gain(arr[0], arr[1]))
            else:
                get_from_net()
            file.close()
    else:
        get_from_net()
    return list_bean


def handle_data():
    # 获取每日收益率
    rate = []
    for bean in get_gain_every_day():
        rate.insert(0, Gain(int(bean.date.replace('-', '')), float(bean.gain)))  # 倒序插入
    # 获取借还记录
    data = []
    path = r'D:\myPy\借还记录\records.txt'
    if os.path.exists(path):
        with open(path, 'r') as file:
            temp_sum = 0
            for line in file.readlines():
                x, y = line.split('	')
                temp_date = int(x)
                temp_money = -int(y)
                temp_sum += temp_money
                latest_index = len(data) - 1
                if latest_index >= 0:
                    data_last = data[latest_index]
                else:
                    data_last = None
                if data_last is not None and data_last.date == temp_date:  # 如果是同一天的记录则整合起来
                    data[latest_index].money = data_last.money + temp_money
                    data[latest_index].the_sum = data_last.the_sum + temp_money
                    # print('%d的记录进行了整合' % temp_date)
                else:
                    data.append(Record(int(x), -int(y), temp_sum))
    else:
        raise IOError('找不到借还记录文件：%s' % path)
    # 因为第一天存的，需要经过第二天的运作才能产生收益，所以将data的数据的日期进行改动，将money>0的日期加一，money<0的日期不变。
    for d in data:
        if d.money > 0:
            reset_date = False
            for r in rate:
                if reset_date:
                    d.date = r.date
                    break
                if r.date == d.date:
                    reset_date = True
    # 根据最新的数据进行累计每天的本金加收益
    list_sum = []
    list_ori_sum = []
    ori_sum = 0
    index = 0
    the_sum = 0
    start_date = 0  # 20201225
    for r in rate:
        money = 0
        for d in data:
            if d.date == r.date:
                money = d.money
                ori_sum = d.the_sum
                break
        the_gain = 0
        if r.date >= start_date:
            the_gain = (the_sum + money) * (r.gain / 10000)
            the_sum = (the_sum + money) + the_gain
        else:
            the_sum = ori_sum
        index += 1
        print('%d、%s的总额为：%f，当天收益为%f 原总额为%f 借出%d ' % (index, r.date, the_sum, the_gain, ori_sum, money))
        list_ori_sum.append(ori_sum)
        list_sum.append(the_sum)
    # 输出结果
    last_data = data[-1]
    print('计算收益前：%s的总额为%f' % (last_data.date, last_data.the_sum))
    print('计算收益后：%s的总额为%f' % (rate[-1].date, the_sum))
    print('计算收益后：%s的收益为%f' % (rate[-1].date, the_sum - last_data.the_sum))
    # 将数据生成图
    list_df = []
    for i in range(len(list_ori_sum)):
        list_df.append([list_ori_sum[i], list_sum[i]])
    df = pd.DataFrame(np.array(list_df), columns=['未加收益总额', '增加收益总额'])
    df.plot()
    plt.show()
    df.to_csv('整合版借还记录支付宝收益.csv')


if __name__ == '__main__':
    warnings.filterwarnings('ignore')
    # 解决中文显示
    plt.rcParams['font.family'] = 'SimHei'
    plt.rcParams['axes.unicode_minus'] = False
    handle_data()
