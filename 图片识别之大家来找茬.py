from PIL import Image, ImageChops
import matplotlib.pyplot as plt
import numpy as np

# 原理是将两张图片的矩阵数据相减，则不为零的部分就是目标部分
path = 'E:\\myPy\\test\\'
img1 = Image.open(path + '1.jpg')
img2 = Image.open(path + '2.jpg')
out = ImageChops.difference(img1, img2)
print(out)
img = np.array(out)  # 将图片的矩阵数据用数组装起来
print(img)
plt.imshow(img)
plt.show()
