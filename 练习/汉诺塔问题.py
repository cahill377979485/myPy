#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time : 2021/4/12 17:02
# @File : 汉诺塔问题.py
# @Author:

# 汉诺塔问题

def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c, 'n==1')
    else:
        move(n - 1, a, c, b)
        print(a, '-->', c, 'else中的print')
        move(n - 1, b, a, c)


move(3, 'A', 'B', 'C')
