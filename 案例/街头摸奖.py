#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time : 2021/4/7 16:36
# @File : 街头摸奖.py
# @Author:
import random
import time

# 如果是不放回（即一次性直接拿出来两个球）：两球都是白球的概率等于C32/C62=(3*2)/(2*1)/(6*5)/(2*1)=3/15=1/5
# 如果是有放回（即拿完之后放回去再拿一个）：两球都是白球的概率等于C31*C31/C61*C61=(3*3)/(6*6)=1/4
win = 0
lose = 0
box = ('白1', '白2', '白3', '黑4', '黑5', '黑6')
z = int(input('请输入试验次数：'))
start_time = time.time()  # 注意计时 代码放的位置
for i in range(z):
    x = random.randint(0, 5)
    y = random.randint(0, 5)

    # while y == x:  # 这一步是表示不放回拿取
    #     y = random.randint(0, 5)

    a = box[x]
    b = box[y]
    #     print(a,b)
    if a[0] == b[0] and a[0] == "白":
        win = win + 1
    else:
        lose = lose + 1
end_time = time.time()
print('赢', win, '输', lose)
m = win / z
n = lose * 3 - win * 7
print("中奖概率是{:.3f},摊主最后获利{}".format(m, n))
total_time = end_time - start_time
print("*****运算耗时{:.4}秒*****".format(total_time))
