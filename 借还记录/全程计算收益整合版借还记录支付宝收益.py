#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time:2021/4/17 9:51
# @File:全程计算收益整合版借还记录支付宝收益.py
# @Author:希尔
# @Email:377979485@qq.com
# @Desc:优化点
# 1、获取余额宝收益信息增加本地缓存，如果发现今天已经有数据了就不需要从接口获取，直接从本地文件中获取数据。
# 2、增加可设置开始计算收益的时间。
# 3、增加无收益时的曲线和有收益的曲线，方便对比。

import json

import requests
import time
import matplotlib.pyplot as plt
import warnings
import pandas as pd


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
    date_start = '2016-02-01'
    date_today = time.strftime('%Y-%m-%d', time.localtime())
    url = f'http://api.fund.eastmoney.com/f10/lsjz?callback=jQuery183023336459069593007_1618390055881&fundCode=000198&pageIndex=1&pageSize=2000&startDate={date_start}&endDate={date_today}&_=1618390082880'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36 SE 2.X MetaSr 1.0',
        'Referer': 'http://fundf10.eastmoney.com/jjjz_000198.html'
    }
    response = requests.get(url, headers=headers).text
    start = response.find(r'(')
    end = response.find(r')')
    final_response = response[start + 1:end]
    dicts = json.loads(final_response)
    list_bean = []
    for item in dicts['Data']['LSJZList']:
        list_bean.append(Gain(item['FSRQ'], item['DWJZ']))
    return list_bean


def handle_data():
    rate = []
    for bean in get_gain_every_day():
        rate.insert(0, Gain(int(bean.date.replace('-', '')), float(bean.gain)))
    data = []
    with open(r'D:\myPy\借还记录\records.txt', 'r') as file:
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
    ori_sum = 0
    index = 0
    the_sum = 0
    for r in rate:
        money = 0
        for d in data:
            if d.date == r.date:
                money = d.money
                ori_sum = d.the_sum
                break
        the_gain = (the_sum + money) * (r.gain / 10000)
        the_sum = (the_sum + money) + the_gain
        index += 1
        print('%d、%s的总额为：%f，当天收益为%f 原总额为%f 借出%d ' % (index, r.date, the_sum, the_gain, ori_sum, money))
        list_sum.append(the_sum)
    # 输出结果
    last_data = data[len(data) - 1]
    print('计算收益前：%s的总额为%f' % (last_data.date, last_data.the_sum))
    print('计算收益后：%s的总额为%f' % (rate[len(rate) - 1].date, the_sum))
    print('计算收益后：%s的收益为%f' % (rate[len(rate) - 1].date, the_sum - last_data.the_sum))
    # 将数据生成图
    df = pd.DataFrame(list_sum, columns=['总额'])
    df.plot()
    plt.show()


if __name__ == '__main__':
    warnings.filterwarnings('ignore')
    # 解决中文显示
    plt.rcParams['font.family'] = 'SimHei'
    plt.rcParams['axes.unicode_minus'] = False
    handle_data()
