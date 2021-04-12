#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time : 2021/4/12 16:59
# @File : 素数.py
# @Author:


import sys

# 修改递归深度的值，让它变大大一点
sys.setrecursionlimit(100000)

k = 0


def do(n, p):
    global k
    is_su = True
    if n <= p:
        for i in range(n // 2 + 1):
            if i > 1 and n % i == 0:
                is_su = False
                break
        if is_su:
            k += 1
            print('%d是素数 共%d' % (n, k))
        do(n + 1, p)


do(2, 999)
