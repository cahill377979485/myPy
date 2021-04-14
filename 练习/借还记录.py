#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time : 2021/4/14 17:44
# @File : 借还记录.py
# @Author:

import pandas as pd
import matplotlib.pyplot as plt
import warnings


class Bean(object):

    def __init__(self, num, date, money, get=0):
        self.num = num
        self.date = date
        self.money = money
        self.get = get


def handle_data():
    data = []
    rate = []
    with open('E:\\myPy\\records.txt', 'r') as file:
        my_sum = 0
        for line in file.readlines():
            x, y = line.split('	')
            my_sum -= int(y)
            data.append((x, -int(y), my_sum))

    with open('E:\\myPy\\余额宝每日万份收益.txt', 'r') as file:
        for line in file.readlines():
            x, y = line.split(' ')
            rate.append((x.replace('-', ''), float(y)))

    # print(rate)
    # 取出2021年开始的记录
    data_2021 = []
    start_sum = 0
    for item in data:
        if int(item[0]) > 20210101:
            data_2021.append(item)
            if start_sum == 0:
                start_sum = int(item[2]) - item[1]
    print('20210101时的总额是%d' % start_sum)
    print(data_2021)
    # 20210101开始计算利息，并将每日利息加入总额中，起始总额是88165
    # 先取list_rate的第一个，如果跟list_date的第一个日期一样，则将list_date的第一个的money加上得到当天的总额，再乘以list_rate
    # 的万份收益率再除以1万。算出当天的收益（相当于利息），再加上总额，得到当天结束时的本息。然后将list_date去除头元素（用
    # pop(0)方法即可)。这样下次判断比较方便。最终可以得到当前甚至未来某一天的本息总额。
    for item in rate:
        pass


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
