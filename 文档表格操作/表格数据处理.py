#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time : 2021/4/21 16:47
# @File : 表格数据处理.py
# @Author:
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('3月份数据.xlsx')
# print(data.head())
data_flower = data.loc[0:len(data) - 2, ['鲜花消耗', '鲜花生成', '购买鲜花']]
data_flower.columns = ['cost', 'create', 'buy']
data_flower['day_left'] = data_flower['create'] + data_flower['cost']
# data_flower['month_left'] = data_flower['day_left'].cumsum()  # sum()计算总计 cumsum()计算累加
print(data_flower)
df = pd.DataFrame(data_flower)
df.plot()
plt.show()
df.to_csv('3月份数据鲜花相关.csv')
