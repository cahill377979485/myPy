#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time : 2021/4/23 16:06
# @File : 抽奖活动2.py
# @Author:

import random
import pandas as pd
import matplotlib.pyplot as plt


class Gift(object):

    def __init__(self, name, rate, gain):
        self.name = name
        self.rate = rate
        self.gain = gain


gifts = [Gift('全部拿走', 0.0001, 0), Gift('百倍奖励', 0.001, 100), Gift('十倍奖励', 0.005, 10),
         Gift('五倍奖励', 0.01, 5),
         Gift('两倍奖励', 0.02, 2),
         Gift('不输不赢', 0.2, 1)]
total = 0


def format_num(num, times):
    s = str(num)
    for j in range(len(str(times)) - len(s)):
        s = '0{}'.format(s)
    return s


def todo():
    global gift
    global total
    x = 0
    ticket = 2
    print('每次抽奖成本为%d' % ticket)
    times = 9000
    get = 0
    while True:
        x += 1
        new_total = total // 2
        get = get + total - new_total
        total = new_total
        list = []
        for i in range(times):
            total += ticket
            current = random.random()
            bingo = False
            get_all = False
            for gift in gifts:
                if gift.rate >= current:
                    print('%s次的结果是：%s 收入：%d' % (format_num(i + 1, times), gift.name, total))
                    bingo = True
                    if gift.name == '全部拿走':
                        get_all = True
                    else:
                        total -= gift.gain * ticket
                    break
            list.append(total)
            if not bingo:
                print('%s次的结果是：谢谢惠顾 收入：%d' % (format_num(i + 1, times), total))
            if get_all:
                print('%d今天%d已经被全拿走了，明日再来' % (x, total))
                print('庄家收益为：%d' % get)
                total = 0
                list.append(total)
                df = pd.DataFrame(list, columns=['gain'])
                df.plot()
                plt.show()
                return


if __name__ == '__main__':
    size = len(gifts)
    print('奖品有：%d种' % size)
    sum_rate = 0
    for gift in gifts:
        sum_rate += gift.rate
    fail_rate = 1 - sum_rate
    print('不中奖的概率为%f' % fail_rate)
    todo()
