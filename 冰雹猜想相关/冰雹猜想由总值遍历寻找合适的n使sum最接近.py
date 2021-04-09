#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time : 2021/4/9 14:20
# @File : 冰雹猜想由总值遍历寻找合适的n使sum最接近.py
# @Author:

target = 100_000
theMinDelta = 0
resultDelta = ''


# 冰雹猜想
def cal(n):
    global target
    global theMinDelta
    global resultDelta
    data = []
    t = 0
    my_sum = 0
    my_max = 0
    my_min = n
    x = n
    flag = True
    while flag:
        t += 1
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        if n <= 0:
            raise ValueError('数字太小了')
        my_sum += n
        # 补全数字前面的0，让其看起来更整齐
        k = str(t)
        for i in range(6):  # 保留位数直接写死就好
            if t < 10 ** i:
                k = '0' + k
        data.append(n)
        # print('第%s次的数是%d 当前和是%d' % (k, n, my_sum))
        if my_max < n:
            my_max = n
        if my_min > n:
            my_min = n
        if n == 1:
            flag = False
            delta = my_sum - target
            if delta < 0:
                continue
            print('目标总和为%d n=%d的冰雹数据中，总和是%d 最小值%d 最大值%d 差值为%d' % (target, x, my_sum, my_min, my_max, delta))
            if theMinDelta == 0:
                theMinDelta = delta
            elif delta < theMinDelta:
                theMinDelta = delta
                resultDelta = '更新最接近值：目标总和为%d n=%d的冰雹数据中，总和是%d 最小值%d 最大值%d 差值为%d' % (
                    target, x, my_sum, my_min, my_max, delta)
        elif n < 1:
            print("已完成n=%d" % x)


if __name__ == "__main__":
    for i in range(5, 9999):
        cal(i)
    print(resultDelta)
