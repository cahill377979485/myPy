#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time : 2021/4/13 12:00
# @File : 爬取破晓电影BeautifulSoup.py
# @Author:
import re

import requests
from bs4 import BeautifulSoup


class TitleBean(object):

    def __init__(self, leixing, date, title, href):
        self.leixing = leixing
        self.date = date
        self.title = title
        self.href = href


if __name__ == '__main__':
    url = "https://www.poxiao.com/"

    response = requests.get(url)
    json = response.content.decode('gbk')
    soup = BeautifulSoup(json, 'html.parser')
    # print(soup.prettify())  # 打印获取到的网页源码
    list_leixing = []
    list_date = []
    list_title = []
    list_href = []
    list_bean = []
    for the_div in soup.findAll('div', class_='indextop'):
        # print(the_div.div.div.ul)
        for item in the_div.div.div.ul:
            # print('~~~')
            # print(item)
            if len(item) <= 1 or str(item).__contains__('<a href="#"'):
                continue
            soup2 = BeautifulSoup(str(item), 'html.parser')
            list_leixing.append(soup2.find('span', class_='leixing').a.get_text())
            date = soup2.find('span', class_='date')
            if date is None or len(date.get_text()) <= 0:
                date = soup2.find('span', class_='date').font.get_text()
            list_date.append(date.get_text())
            list_title.append(soup2.findAll('a', target='_blank')[1].get_text())
            list_href.append('https://www.poxiao.com{}'.format(soup2.findAll('a', target='_blank')[1]['href']))
    print('共有%d个条目' % len(list_leixing))
    if len(list_leixing) != len(list_date) or len(list_date) != len(list_title) or len(list_title) != len(list_href):
        raise ValueError('数据的各数组元素个数不一致，请检查')
    for i in range(len(list_leixing)):
        list_bean.append(TitleBean(list_leixing[i], list_date[i], list_title[i], list_href[i]))
    for item in list_bean:  # 输出的字符串中可能包含了很多空格或空行,使用 .stripped_strings 可以去除多余空白内容:
        print('%s %s %s   %s' % (item.leixing, item.date, item.title, item.href))
