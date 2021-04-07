#!usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time : 2021/4/7 9:12
# @File : 爬取知乎热榜前50BeautifulSoup.py
# @Author: 希尔
import re
from bs4 import BeautifulSoup
import requests


class Item(object):

    def __init__(self, rank, title, popular, href):
        self.rank = rank
        self.title = title
        self.popular = popular
        self.href = href


if __name__ == '__main__':
    url = "https://www.zhihu.com/hot"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36",
        "Cookie": '_zap=c88686bf-d341-4148-8d4b-93778d38c997; _xsrf=aafca671-513d-4b19-adad-0d508424ca2f; d_c0="APCcTwoW4xKPTszC_oe4bfYEcF90LXKQMK8=|1617257135"; __snaker__id=0d3RTXB7C4KKWWkV; _9755xjdesxxd_=32; l_n_c=1; r_cap_id="YThlMDcwMjJhZjg0NDg1YzkxMTBmY2RkMjM1OTJhNzM=|1617257136|4c1e872f2218340d612a50c652a6fa8825efc2ad"; cap_id="ZTY4MjMwN2E2ZmRkNGZmNzkyYzFjOTFhNWQ2ODE5NjQ=|1617257136|c96526af7729a49d892d2e0afc1d4fbe458bb115"; l_cap_id="YmNhMTI3MWIyZWFlNDEyOWI2NzBmZTBkZWNjY2VjYWI=|1617257136|4d018d8b005aff8aff7f5d2424adaf8a836d6707"; n_c=1; tshl=; tst=h; captcha_session_v2="2|1:0|10:1617258363|18:captcha_session_v2|88:WEx3a2JueGpEdHpYRXVZbk4yRWdpOUlta2lDVGtCeUk4d1BlZVlzOHpiNGJGY1pRalhPMHdzK2VBejdHRkg4WQ==|2989454ac9b495e4c7854eed6851a2ac94be93d0d6ade509fd8e6095ae5ab4b2"; gdxidpyhxdE=%2Frusqdxx6mDvMAQNUV0yUuGfKC0rlXVxkjO0MWlo97N0Qh5GK3Du7HcRNmcfHCNM%2FAn2NK8P6n0t0LP%2Boit6LMZytzdUcWVpUwz%2BNHsp%5CBA%2B8T%2BQGzZSKRolIKX5JAzc0m44qDkzO%2Byo%2F%5CO3sEd%2FDJkuRgtPl2S%2FgyJ4GQ6qzOj4iMdf%3A1617259380116; z_c0=Mi4xNHBxVUNRQUFBQUFBOEp4UENoYmpFaGNBQUFCaEFsVk56ckJTWVFDZlJpUWR3NEtmXy13aWV2Q0ZuMnlsaGEwbkhR|1617257166|10a818da2fc9436d39b962e71b606ebaaf24d5ef; KLBRSID=4843ceb2c0de43091e0ff7c22eadca8c|1617258368|1617257134'}
    response = requests.get(url, headers=headers)
    json = response.content.decode()
    soup = BeautifulSoup(json, 'html.parser')
    print(soup.prettify())
    listRank = []
    listTitle = []
    listPopular = []
    listHref = []
    for item in soup.findAll('div', class_='HotItem-index'):
        r = item.div.get_text()
        if int(r) < 10:
            r = '0' + r
        listRank.append(r)
    for item in soup.findAll('div', class_='HotItem-content'):
        listTitle.append(item.a['title'])
    for item in soup.findAll('div', class_=re.compile('HotItem-metrics')):
        listPopular.append(item.get_text()[:-2])  # 这里获得的必须用切片去掉“分享”两个字
    for item in soup.findAll('div', class_='HotItem-content'):
        listHref.append(item.a['href'])
    listItem = []
    if len(listRank) != len(listTitle) or len(listTitle) != len(listPopular) or len(listPopular) != len(listHref):
        raise ValueError('数据的各数组元素个数不一致，请检查')
    if len(listRank) > 0:
        for i in range(len(listRank)):
            listItem.append(Item(listRank[i], listTitle[i], listPopular[i], listHref[i]))
    #  打印
    for item in listItem:
        print('%s、%s %s %s' % (item.rank, item.title, item.popular, item.href))
