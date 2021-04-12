#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time : 2021/4/9 17:32
# @File : set相关.py
# @Author:
x = set('runoob')
y = set('google')
print('\nx,y')
print(x, y)

print('\n交集')
print(x & y)  # 交集
print('\n并集')
print(x | y)  # 并集
print('\n差集')
print(x - y)  # 差集=x-x&y
print('\n补集')
print(x ^ y)  # 补集
