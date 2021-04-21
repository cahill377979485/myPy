#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time : 2021/4/21 14:11
# @File : pandas2.py
# @Author:

import pandas as pd
import matplotlib.pyplot as plt

companys = 'DAACACABB'
salarys = [43, 8, 28, 42, 33, 20, 48, 25, 39]
ages = [21, 41, 26, 28, 26, 18, 43, 23, 18]
data = []
for i in range(len(companys)):
    data.append((companys[i], salarys[i], ages[i]))
df = pd.DataFrame(data, columns=['company', 'salary', 'age'])
print(df)
# df.plot()
# plt.show()



