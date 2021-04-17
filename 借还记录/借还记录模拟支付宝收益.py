#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time : 2021/4/14 17:44
# @File : 借还记录模拟支付宝收益.py
# @Author:

import matplotlib.pyplot as plt
import warnings


class Record(object):

    def __init__(self, date, money, the_sum):
        self.date = date
        self.money = money
        self.the_sum = the_sum


class GetEveryDay(object):

    def __init__(self, date, get):
        self.date = date
        self.get = get


def handle_data():
    data = []
    rate = []
    with open(r'D:\myPy\借还记录\records.txt', 'r') as file:
        my_sum = 0
        for line in file.readlines():
            x, y = line.split('	')
            my_sum -= int(y)
            data.append(Record(int(x), -int(y), my_sum))

    with open(r'D:\myPy\借还记录\余额宝每日万份收益.txt', 'r') as file:
        for line in file.readlines():
            x, y = line.split(' ')
            rate.insert(0, GetEveryDay(int(x.replace('-', '')), float(y)))

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
    # 根据最新的数据进行累计每天的本金加收益
    for r in rate:
        money = 0
        for d in data_2021:
            if d.date == r.date:
                money = d.money
                break
        the_get = (the_sum + money) * (r.get / 10000)
        the_sum = (the_sum + money) + the_get
        print('%s的总额为：%f，当天收益为%f' % (r.date, the_sum, the_get))

    # 输出结果
    last_data = data[len(data) - 1]
    print('计算收益前最后的记录：%s的总额为%f' % (last_data.date, last_data.the_sum))
    print('计算收益后：%s的总额为%f' % (rate[len(rate) - 1].date, the_sum))
    print('%s的收益为%f' % (rate[len(rate) - 1].date, the_sum - last_data.the_sum))
    # 将数据生成图
    # df = pd.DataFrame(data, columns=['日期', '借出', '总额'])
    # df.plot()
    # plt.show()
    # 根据计算总值


if __name__ == '__main__':
    warnings.filterwarnings('ignore')
    # 解决中文显示
    plt.rcParams['font.family'] = 'SimHei'
    plt.rcParams['axes.unicode_minus'] = False
    handle_data()
