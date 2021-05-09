#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time:2021/5/2 9:16
# @File:超椭圆.py
# @Author:希尔
# @Email:377979485@qq.com
# @Desc:超椭圆曲线


import numpy as np
import matplotlib.pyplot as plt

n = 3.5
x = np.arange(-1, 1, 0.01)
y = (1 - abs(x) ** n) ** (1 / n)
LogoX = np.append(x, 1)
LogoY = np.append(y, 0)
x = np.arange(1, -1, -0.01)
y = -(1 - abs(x) ** n) ** (1 / n)
LogoX = np.append(LogoX, x)
LogoY = np.append(LogoY, y)
LogoX = np.append(LogoX, -1)
LogoY = np.append(LogoY, 0)
plt.figure(figsize=(10, 10))
plt.title('Logo |X|^n+|Y|^n=1\nn=%s' % n)
plt.xlabel('X')
plt.ylabel('Y')
plt.plot(LogoX, LogoY)
plt.savefig('output_%f.png' % n)
plt.show()
