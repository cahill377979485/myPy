#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# 使用BeautifulSoup4来获取数据
from bs4 import BeautifulSoup
import requests


class TitleBean(object):

    def __init__(self, num, title, href):
        self.num = num
        self.title = title
        self.href = href


if __name__ == '__main__':
    url = 'http://top.baidu.com/buzz?b=1'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36',
        'Cookie': 'PSTM=1605747869; BIDUPSID=254792883FB8AC0DAC9E0E3CCB948509; bdshare_firstime=1610099489076; BAIDUID=D86A4A610A83A68E6378BCD9EBEA5ACF:FG=1; BDUSS=ppcVVaZlJIVS1OdktvaE9hV1VlRzZoVy01Z0JNYmxnM3Zwa0hzVUp0VVdXM0ZnRVFBQUFBJCQAAAAAAAAAAAEAAAC80EknusHO9AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbOSWAWzklgV2; MCITY=-%3A; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDSFRCVID=BvuOJeC62iGEuJJejt6yrnpjuTcysYOTH6aoTXkOUICYED_CscCmEG0PJf8g0Ku-hD88ogKK3mOTH4-F_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=JbAtoKD-JKvJfJjkM4rHqR_Lqxby26nGbjT9aJ5nJDoEsp5Gyx6qMR3B2q5XbPTtQI78QMTvQpP-HJ72W-Rc3fFdWtoRyMJeK27LKl0MLpctbb0xyn_VMM3beMnMBMPeamOnaI-E3fAKftnOM46JehL3346-35543bRTLnLy5KJYMDcnK4-Xj63-jHoP; H_PS_PSSID=33639_33751_33272_31253_33759_33392_33713_26350_33795; delPer=0; PSINO=2; BA_HECTOR=85858g0l2ka10g0koq1g6aqvn0q; Hm_lvt_79a0e9c520104773e13ccd072bc956aa=1617259516; Hm_lpvt_79a0e9c520104773e13ccd072bc956aa=1617259516',
        'Referer': 'https://www.baidu.com/link?url=Di5vYWlTOHiDSnTHsNWbYz-12Z-UlPs4tkB5FHhtYQGzZCY3DPTedfwsM--j8uXm&wd=&eqid=a5c8245d0000366c0000000260656b82'
    }
    response = requests.get(url, headers=headers)
    json = response.content.decode('gb2312')
    soup = BeautifulSoup(json, 'html.parser')
    print(soup.prettify())  # 打印获取到的网页源码
    listNum = []
    listTitle = []
    listHref = []
    listBean = []
    for item in soup.findAll('td', class_='first'):
        listNum.append(item.span.get_text())
    for item in soup.findAll('a', class_='list-title'):
        listTitle.append(item.get_text())
    for item in soup.findAll('a', class_='list-title'):
        listHref.append(item['href'])
    if len(listNum) != len(listTitle) or len(listTitle) != len(listHref):
        raise ValueError('数据的各数组元素个数不一致，请检查')
    for i in range(len(listNum)):
        rank = listNum[i]
        for j in range(2 - len(rank)):
            rank = '0{}'.format(rank)
        listBean.append(TitleBean(rank, listTitle[i], listHref[i]))
    for item in listBean:  # 输出的字符串中可能包含了很多空格或空行,使用 .stripped_strings 可以去除多余空白内容:
        print('%s、%s %s' % (item.num, item.title, item.href))
