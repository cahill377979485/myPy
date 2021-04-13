#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time : 2021/4/13 10:02
# @File : 生成一个乱序的数组.py
# @Author:

import random

num = 5
# 方法一
temp = []
for i in range(num):
    temp.append(i)
count = num
result = [0] * num
for i in range(count):
    n = random.randint(0, count - i - 1)
    result[i] = temp[n]
    temp.pop(n)
print(result)

# 方法二
s = ''
for i in range(num):
    s += str(i)
my_set = set(s)
print(my_set)
