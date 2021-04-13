#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time : 2021/4/13 11:33
# @File : 爬取破晓电影.py
# @Author:
from lxml import etree
import requests

if __name__ == '__main__':
    url = "https://www.poxiao.com/"
    response = requests.get(url)
    print('返回码：%s' % response)
    html_str = response.content.decode('gbk')
    html = etree.HTML(html_str)
    print('网页源码：%s' % html_str)

    # 获取知乎热榜排名标题热度
    resultDelta = html.xpath("//div[@class='indextop']/div/div/ul")
    print('result.len=%d' % len(resultDelta))
    print(resultDelta)
    for table in resultDelta:  # 不知道为啥，可能是数据结构的问题，第一次取出来就得到了所有的内容
        leixing = table.xpath(".//li/span[@class='leixing']/a[@href!='#']/text()")
        date = table.xpath(".//li/span[@class='date']/text()|.//li/span[@class='date']/font/text()")
        title = table.xpath(".//li/a/text()")
        href = table.xpath(".//li/a[@href!='https://www.jianpian.com/']/@href")
        # print(len(date))
        # print(len(leixing))
        # print(len(title))
        # print(len(href))
        for i in range(len(title)):
            print('%s %s %s   %s' % (date[i], leixing[i], title[i], 'https://www.poxiao.com{}'.format(href[i])))
