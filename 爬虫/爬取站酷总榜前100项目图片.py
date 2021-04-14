import re
import os
import time
import threading
import requests


def handle_img_list(path_pre, the_semaphore):
    the_semaphore.acquire()
    url = "https://www.zcool.com.cn/top/index.do"
    res_code = requests.get(url).text  # 获取该网页的详细信息
    print('获取到的网页源码为：\n%s' % res_code)
    img_list = re.compile(r'(?<=src=")https://img\.zcool\.cn.{40,42}\.jpg').findall(
        res_code)  # 表示在整个网页过滤出所有图片的地址，放在imgList中
    size = len(img_list)
    print('通过正则表达式共找到%d张图片' % size)
    x = 1  # 声明一个变量赋值
    path_mid = '{0}{1}{2}'.format(path_pre, time.strftime('%Y-%m-%d', time.localtime()), '3排行榜前100')  # 设置图片的保存地址
    if not os.path.isdir(path_mid):
        print('创建保存资源的文件夹路径')
        os.makedirs(path_mid)  # 判断没有此路径则创建
    path_final = path_mid + '\\'
    time_start = time.time()
    for img_url in img_list:
        print('正在下载第%d张/%d 用时%s' % (x, size, time.time() - time_start))
        absolute_path = '{0}{1}.jpg'.format(path_final, x)
        if os.path.isfile(absolute_path):
            x = x + 1
            continue
        try:
            with open(f'{absolute_path}', 'wb') as file_data:
                print("正在下载图片")
                file_data.write(requests.get(img_url).content)
        except Exception as e:
            print('第%d张/%d出错，原因是：%s' % (x, size, e.__cause__))
        finally:
            x = x + 1
    print('图片下载完成，注意查看文件夹%s 用时%s' % (path_final, time.time() - time_start))
    print(img_list)
    the_semaphore.release()


if __name__ == '__main__':
    semaphore = threading.BoundedSemaphore(5)
    path = 'E:\\myPy\\'
    t = threading.Thread(target=handle_img_list, args=(path, semaphore))
    t.start()
    while threading.active_count() != 1:
        pass
    else:
        print('全部图片下载完毕')
