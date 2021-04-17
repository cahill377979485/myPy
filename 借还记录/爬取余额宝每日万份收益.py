#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time : 2021/4/14 16:49
# @File : 爬取余额宝每日万份收益.py
# @Author:
import json

import requests
import time


class Bean(object):

    def __init__(self, date, get):
        self.date = date
        self.get = get


def query():
    date_start = '2021-01-01'
    date_today = time.strftime('%Y-%m-%d', time.localtime())
    url = f'http://api.fund.eastmoney.com/f10/lsjz?callback=jQuery183023336459069593007_1618390055881&fundCode=000198&pageIndex=1&pageSize=200&startDate={date_start}&endDate={date_today}&_=1618390082880'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36 SE 2.X MetaSr 1.0',
        'Referer': 'http://fundf10.eastmoney.com/jjjz_000198.html'
    }
    response = requests.get(url, headers=headers).text
    # print(response)
    start = response.find(r'(')
    end = response.find(r')')
    final_response = response[start + 1:end]
    # print(final_response)
    dicts = json.loads(final_response)
    # print(dicts)
    list_bean = []
    for item in dicts['Data']['LSJZList']:
        list_bean.append(Bean(item['FSRQ'], item['DWJZ']))
    for item in list_bean:
        print('%s %f' % (item.date, float(item.get)))
    with open(r'D:\myPy\借还记录\余额宝每日万份收益.txt', 'w+') as file:
        for item in list_bean:
            file.write('%s %f\n' % (item.date, float(item.get)))


if __name__ == '__main__':
    query()
