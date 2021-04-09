import requests
import json

if __name__ == '__main__':
    post_url = 'https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    keyword = input('请输入要查询的城市：')

    data = {
        'cname': '',
        'pid': '',
        'keyword': keyword,
        'pageindex': '1',
        'pageSize': '10'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    response = requests.post(url=post_url, data=data, headers=headers)

    # 持久化存储
    # page_text = response.text
    # fileName = keyword + '.html'
    # with open(fileName, 'w', encoding= 'utf-8') as fp:
    #     fp.write(page_text)
    # print(fileName, 'Over!')

    # 直接打印出来
    page = response.json()
    for dic in page['Table1']:
        storeName = dic['storeName']
        address = dic['addressDetail']
        print('店名：' + storeName, '地址：' + address + '\n')
