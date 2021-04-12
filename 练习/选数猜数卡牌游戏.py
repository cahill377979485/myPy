#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time : 2021/4/12 16:55
# @File : 选数猜数卡牌游戏.py
# @Author:

n = 6  # 二进制位数
arr = []
for i in range(n):
    arr.append([])
for i in range(2 ** n):
    s = bin(i)[2:]  # 二进制是以“0b”开头的，先用切片去掉“0b”
    print('%d 的二进制数是 %s' % (i, s))
    # 补全
    s = "0" * (n - len(s)) + s
    print('补全后为 %s' % s)
    for j in range(n):
        c = s[j]
        if c == "1":
            arr[j].append(i)
# 打印出来
print('\n最终的结果为：')
for i in range(len(arr)):
    print()
    print('第%d组：' % (i + 1))
    print(arr[i])
