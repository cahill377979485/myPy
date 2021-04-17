#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time:2021/4/17 9:51
# @File:整合版借还记录支付宝收益.py
# @Author:希尔
# @Email:377979485@qq.com
# @Desc:
import json

import requests
import time
import matplotlib.pyplot as plt
import warnings
import pandas as pd


list_bean = []


class Record(object):

    def __init__(self, date, money, the_sum):
        self.date = date
        self.money = money
        self.the_sum = the_sum


class SumRecord(object):

    def __init__(self, date, the_sum):
        self.date = date
        self.the_sum = the_sum


class GetEveryDay(object):

    def __init__(self, date, gain):
        self.date = date
        self.gain = gain


def get_gain_every_day():
    date_start = '2021-01-01'
    date_today = time.strftime('%Y-%m-%d', time.localtime())
    url = f'http://api.fund.eastmoney.com/f10/lsjz?callback=jQuery183023336459069593007_1618390055881&fundCode=000198&pageIndex=1&pageSize=200&startDate={date_start}&endDate={date_today}&_=1618390082880'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36 SE 2.X MetaSr 1.0',
        'Referer': 'http://fundf10.eastmoney.com/jjjz_000198.html'
    }
    response = requests.get(url, headers=headers).text
    # print(response)
    start = response.find(r'(')
    end = response.find(r')')
    final_response = response[start + 1:end]
    # print(final_response)
    dicts = json.loads(final_response)
    # print(dicts)
    global list_bean
    for item in dicts['Data']['LSJZList']:
        list_bean.append(GetEveryDay(item['FSRQ'], item['DWJZ']))
    # for item in list_bean:
    #     print('%s %f' % (item.date, float(item.get)))
    # with open(r'D:\myPy\借还记录\余额宝每日万份收益.txt', 'w+') as file:
    #     for item in list_bean:
    #         file.write('%s %f\n' % (item.date, float(item.get)))


def handle_data():
    get_gain_every_day()
    data = []
    rate = []
    with open(r'D:\myPy\借还记录\records.txt', 'r') as file:
        my_sum = 0
        for line in file.readlines():
            x, y = line.split('	')
            my_sum -= int(y)
            data.append(Record(int(x), -int(y), my_sum))

    for bean in list_bean:
        rate.insert(0, GetEveryDay(int(bean.date.replace('-', '')), float(bean.gain)))

    # print(rate)
    # 取出2021年开始的记录
    data_2021 = []
    start_sum = 0
    for item in data:
        if item.date > 20210101:  # 2021年开始起算
            data_2021.append(item)
            if start_sum == 0:
                start_sum = item.the_sum - item.money
    print('20210101时的总额是%d' % start_sum)
    the_sum = start_sum
    # 因为第一天存的，需要经过第二天的运作才能产生收益，所以将data的数据的日期进行改动，将money>0的日期加一，money<0的日期不变。
    for d in data_2021:
        if d.money > 0:
            reset_date = False
            for r in rate:
                if reset_date:
                    d.date = r.date
                    break
                if r.date == d.date:
                    reset_date = True
    data_final = []
    # 根据最新的数据进行累计每天的本金加收益
    for r in rate:
        money = 0
        for d in data_2021:
            if d.date == r.date:
                money = d.money
                break
        the_gain = (the_sum + money) * (r.gain / 10000)
        the_sum = (the_sum + money) + the_gain
        print('%s的总额为：%f，当天收益为%f' % (r.date, the_sum, the_gain))
        data_final.append(the_sum)

    # 输出结果
    last_data = data[len(data) - 1]
    print('计算收益前：%s的总额为%f' % (last_data.date, last_data.the_sum))
    print('计算收益后：%s的总额为%f' % (rate[len(rate) - 1].date, the_sum))
    print('计算收益后：%s的收益为%f' % (rate[len(rate) - 1].date, the_sum - last_data.the_sum))
    # 将数据生成图
    df = pd.DataFrame(data_final, columns=['总额'])
    df.plot()
    plt.show()


if __name__ == '__main__':
    warnings.filterwarnings('ignore')
    # 解决中文显示
    plt.rcParams['font.family'] = 'SimHei'
    plt.rcParams['axes.unicode_minus'] = False
    handle_data()
