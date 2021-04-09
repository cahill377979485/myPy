from lxml import etree
import requests

if __name__ == '__main__':
    url = "https://movie.douban.com/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36",
        "Cookie": '_zap=c88686bf-d341-4148-8d4b-93778d38c997; _xsrf=aafca671-513d-4b19-adad-0d508424ca2f; d_c0="APCcTwoW4xKPTszC_oe4bfYEcF90LXKQMK8=|1617257135"; __snaker__id=0d3RTXB7C4KKWWkV; _9755xjdesxxd_=32; l_n_c=1; r_cap_id="YThlMDcwMjJhZjg0NDg1YzkxMTBmY2RkMjM1OTJhNzM=|1617257136|4c1e872f2218340d612a50c652a6fa8825efc2ad"; cap_id="ZTY4MjMwN2E2ZmRkNGZmNzkyYzFjOTFhNWQ2ODE5NjQ=|1617257136|c96526af7729a49d892d2e0afc1d4fbe458bb115"; l_cap_id="YmNhMTI3MWIyZWFlNDEyOWI2NzBmZTBkZWNjY2VjYWI=|1617257136|4d018d8b005aff8aff7f5d2424adaf8a836d6707"; n_c=1; tshl=; tst=h; captcha_session_v2="2|1:0|10:1617258363|18:captcha_session_v2|88:WEx3a2JueGpEdHpYRXVZbk4yRWdpOUlta2lDVGtCeUk4d1BlZVlzOHpiNGJGY1pRalhPMHdzK2VBejdHRkg4WQ==|2989454ac9b495e4c7854eed6851a2ac94be93d0d6ade509fd8e6095ae5ab4b2"; gdxidpyhxdE=%2Frusqdxx6mDvMAQNUV0yUuGfKC0rlXVxkjO0MWlo97N0Qh5GK3Du7HcRNmcfHCNM%2FAn2NK8P6n0t0LP%2Boit6LMZytzdUcWVpUwz%2BNHsp%5CBA%2B8T%2BQGzZSKRolIKX5JAzc0m44qDkzO%2Byo%2F%5CO3sEd%2FDJkuRgtPl2S%2FgyJ4GQ6qzOj4iMdf%3A1617259380116; z_c0=Mi4xNHBxVUNRQUFBQUFBOEp4UENoYmpFaGNBQUFCaEFsVk56ckJTWVFDZlJpUWR3NEtmXy13aWV2Q0ZuMnlsaGEwbkhR|1617257166|10a818da2fc9436d39b962e71b606ebaaf24d5ef; KLBRSID=4843ceb2c0de43091e0ff7c22eadca8c|1617258368|1617257134'}
    response = requests.get(url, headers=headers)
    print('返回码：%s' % response)
    html_str = response.content.decode()
    html = etree.HTML(html_str)
    print('网页源码：%s' % html_str)

    # 获取知乎热榜排名标题热度
    resultDelta = html.xpath("//div[@class='s']/div[@class='screening-bd']/ul")
    print('result.len=%d' % len(resultDelta))
    print(resultDelta)
    for table in resultDelta:  # 不知道为啥，可能是数据结构的问题，第一次取出来就得到了所有的内容
        title = table.xpath(".//li/@data-title")
        pic = table.xpath(".//li/ul/li[@class='poster']/a/img/@src")
        href = table.xpath(".//li/ul/li[@class='poster']/a/@href")
        # print(title)
        # print(pic)
        # print(href)
        for i in range(len(title)):
            r = str(i + 1)
            if i + 1 < 10:
                r = '0' + r
            print('%s、%s %s   %s' % (r, title[i], pic[i], href[i]))
