#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time : 2021/4/13 11:28
# @File : 爬取智趣接口文档.py
# @Author:

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    url = 'http://test.app.api.myenglish.com.cn:8089/swagger/ui/index#/'
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36',
    #     'Cookie': 'PSTM=1605747869; BIDUPSID=254792883FB8AC0DAC9E0E3CCB948509; bdshare_firstime=1610099489076; BAIDUID=D86A4A610A83A68E6378BCD9EBEA5ACF:FG=1; BDUSS=ppcVVaZlJIVS1OdktvaE9hV1VlRzZoVy01Z0JNYmxnM3Zwa0hzVUp0VVdXM0ZnRVFBQUFBJCQAAAAAAAAAAAEAAAC80EknusHO9AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbOSWAWzklgV2; MCITY=-%3A; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDSFRCVID=BvuOJeC62iGEuJJejt6yrnpjuTcysYOTH6aoTXkOUICYED_CscCmEG0PJf8g0Ku-hD88ogKK3mOTH4-F_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=JbAtoKD-JKvJfJjkM4rHqR_Lqxby26nGbjT9aJ5nJDoEsp5Gyx6qMR3B2q5XbPTtQI78QMTvQpP-HJ72W-Rc3fFdWtoRyMJeK27LKl0MLpctbb0xyn_VMM3beMnMBMPeamOnaI-E3fAKftnOM46JehL3346-35543bRTLnLy5KJYMDcnK4-Xj63-jHoP; H_PS_PSSID=33639_33751_33272_31253_33759_33392_33713_26350_33795; delPer=0; PSINO=2; BA_HECTOR=85858g0l2ka10g0koq1g6aqvn0q; Hm_lvt_79a0e9c520104773e13ccd072bc956aa=1617259516; Hm_lpvt_79a0e9c520104773e13ccd072bc956aa=1617259516',
    #     'Referer': 'https://www.baidu.com/link?url=Di5vYWlTOHiDSnTHsNWbYz-12Z-UlPs4tkB5FHhtYQGzZCY3DPTedfwsM--j8uXm&wd=&eqid=a5c8245d0000366c0000000260656b82'
    # }
    response = requests.get(url)  # , headers=headers
    json = response.content.decode('gbk')
    soup = BeautifulSoup(json, 'html.parser')
    print(soup.prettify())  # 打印获取到的网页源码
