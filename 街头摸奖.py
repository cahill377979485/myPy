#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time : 2021/4/7 16:36
# @File : 街头摸奖.py
# @Author:
import random
import time

win = 0
lose = 0
box = ('白1', '白2', '白3', '黑4', '黑5', '黑6')
z = int(input('请输入试验次数：'))
start_time = time.time()  # 注意计时 代码放的位置
for i in range(z):
    x = random.randint(0, 5)
    y = random.randint(0, 5)
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
