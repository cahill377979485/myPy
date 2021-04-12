#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time : 2021/4/12 16:59
# @File : @Property相关.py
# @Author:


# 请利用@property给一个Screen对象加上width和height属性，
# 以及一个只读属性resolution：

class Screen(object):

    # Python内置的@property装饰器就是负责把一个方法变成属性调用的
    @property
    def set_width(self, width):
        self._width = width

    @property
    def set_height(self, height):
        self._height = height

    @set_width.getter
    def get_width(self):
        return self._width

    @set_height.getter
    def get_height(self):
        return self._height

    @property
    def resolution(self):
        return self.width * self.height


# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
