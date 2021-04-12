#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time : 2021/4/12 17:14
# @File : 模拟键盘鼠标操作.py
# @Author:

import pyautogui
import time

print(pyautogui)
# pyautogui.PAUSE = 2.5
# pyautogui.moveTo(100,100,duration=3000)
pyautogui.typewrite('Hello world!\n', interval=0.45)
