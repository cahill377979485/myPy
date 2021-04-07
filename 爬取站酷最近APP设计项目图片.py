import urllib.request
import re
import os
import urllib
import time
import random


def get_html(target):
    print('目标网址为：\n%s' % target)
    page = urllib.request.urlopen(target)
    html_a = page.read()
    return html_a.decode('utf-8')


def handle_img_list(html):
    reg = r'(?<=cover\":\")https:\/\/img\.zcool\.cn.{40,41}\.jpg(?=")'
    img_re = re.compile(reg)  # 转换成一个正则对象
    img_list = img_re.findall(html)  # 表示在整个网页过滤出所有图片的地址，放在imgList中
    size = len(img_list)
    print('通过正则表达式共找到%d张图片' % size)
    x = 1  # 声明一个变量赋值
    path = 'E:\\myPy\\{0}{1}'.format(time.strftime('%Y-%m-%d', time.localtime()), '最新APP设计')  # 设置图片的保存地址
    if not os.path.isdir(path):
        print('创建保存资源的文件夹路径')
        os.makedirs(path)  # 判断没有此路径则创建
    paths = path + '\\'
    time_start = time.time()
    for img_url in img_list:
        print('正在下载第%d张/%d 用时%s' % (x, size, time.time() - time_start))
        absolute_path = '{0}{1}.jpg'.format(paths, x)
        if os.path.isfile(absolute_path):
            x = x + 1
            continue
        try:
            urllib.request.urlretrieve(img_url, '{0}{1}.jpg'.format(paths, x))  # 打开imgList,下载图片到本地
            time.sleep(random.randint(2, 3))  # 休眠几秒，防止下载过快
        except Exception as e:
            print('第%d张/%d出错，原因是：%s' % (x, size, e.__cause__))
        finally:
            x = x + 1
    print('图片下载完成，注意查看文件夹%s 用时%s' % (path, time.time() - time_start))
    print(img_list)
    return img_list


url = "https://www.zcool.com.cn/discover.json?cate=17&subCate=757&hasVideo=0&city=0&college=0&recom"
res_code = get_html(url)  # 获取该网页的详细信息
print('~获取到的网页源码为：\n%s' % res_code)
handle_img_list(res_code)  # 从网页源代码中分析下载保存图片
