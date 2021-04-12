#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time : 2021/4/12 17:05
# @File : 阶乘.py
# @Author:

import sys

# 修改递归深度的值，让它变大大一点
sys.setrecursionlimit(100000)


def fect(n):
    if n == 1:
        return 1
    return n * fect(n - 1)


print(fect(1))
print(fect(4))
print(fect(10))


def fe(n, p):
    if n == 1:
        return p
    return fe(n - 1, n * p)


print(fe(1000, 1))
