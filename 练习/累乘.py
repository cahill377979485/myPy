#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time : 2021/4/12 17:06
# @File : 累乘.py
# @Author:

# -*- coding: utf-8 -*-
def mul(x, y=1, *args):
    m = x * y
    for i in args:
        m *= i
    return m


# 测试
print('mul(5) =', mul(5))
print('mul(5, 6) =', mul(5, 6))
print('mul(5, 6, 7) =', mul(5, 6, 7))
print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
if mul(5) != 5:
    print('测试失败!')
elif mul(5, 6) != 30:
    print('测试失败!')
elif mul(5, 6, 7) != 210:
    print('测试失败!')
elif mul(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        mul()
        print('测试失败!')
    except TypeError:
        print('测试成功!')
