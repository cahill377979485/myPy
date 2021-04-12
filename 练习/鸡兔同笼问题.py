#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time : 2021/4/12 16:55
# @File : 鸡兔同笼问题.py
# @Author:
# 鸡兔同笼问题

# 穷举法验证
def cal(head, foot):
    for i in range(head):
        ji = i
        tu = head - ji
        if ji * 2 + tu * 4 == foot:
            print('ji=%d tu=%d' % (ji, tu))


# 让所有鸡兔都两只脚着地，那么没着地的那些多出来的脚都属于兔子，且每只兔子举着两只脚
def cal2(head, foot):
    tu = (foot - 2 * head) // 2
    ji = head - tu
    print('ji=%d tu=%d' % (ji, tu))


cal(55, 122)
cal2(55, 122)
