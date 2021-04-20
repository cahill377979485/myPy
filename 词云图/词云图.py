#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time : 2021/4/20 10:21
# @File : 词云图.py
# @Author:

import matplotlib.pyplot as plt
import jieba
from wordcloud import wordcloud

# 1.读出词语
text = open(r'D:\myPy\词云图\词云图.txt', 'r', encoding='utf-8').read()
print(text)
# 2.把歌词剪开
cut_text = jieba.cut(text)
# print(type(cut_text))
# print(next(cut_text))
# print(next(cut_text))
# 3.以空格拼接起来
result = " ".join(cut_text)
# print(result)
# 4.生成词云
wc = wordcloud.WordCloud(
    font_path=r'D:\myPy\词云图\优设好身体.ttf',  # 字体路径
    background_color='white',  # 背景颜色
    width=800,
    height=800,
    max_font_size=50,  # 字体大小
    min_font_size=10,
    mask=plt.imread(r'D:\myPy\词云图\xin.jpg'),  # 背景图片
    max_words=1000
)
wc.generate(result)
wc.to_file(r'D:\myPy\词云图\jielun.png')  # 图片保存

# 5.显示图片
plt.figure(r'D:\myPy\词云图\jielun')  # 图片显示的名字
plt.imshow(wc)
plt.axis('off')  # 关闭坐标
plt.show()
