#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time : 2021/4/12 17:08
# @File : 求一元二次方程的解.py
# @Author:

# -*- coding: utf-8 -*-
# 求一元二次
import math


def quadratic(a, b, c):
    if not isinstance(a, int) or not isinstance(b, int) or not isinstance(c, int):
        raise TypeError('a and b and c must be integer!')
    if a == 0:
        raise TypeError('a can not be zero')
    m = math.sqrt(b ** 2 - 4 * a * c)
    x1 = (-b + m) / (2 * a)
    x2 = (-b - m) / (2 * a)
    return x1, x2


# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
