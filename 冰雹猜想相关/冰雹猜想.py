import pandas as pd
import matplotlib.pyplot as plt
import warnings


# 冰雹猜想
def cal(n):
    data = []
    t = 0
    tip = '冰雹猜想n={}'.format(n)
    my_sum = 0
    my_max = 0
    my_min = n
    print('计算%d次的冰雹数据' % n)
    x = n
    flag = True
    while flag:
        t += 1
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        if n <= 0:
            raise ValueError('数字太小了')
        my_sum += n
        # 补全数字前面的0，让其看起来更整齐
        k = str(t)
        for i in range(6):  # 保留位数直接写死就好
            if t < 10 ** i:
                k = '0' + k
        data.append(n)
        print('第%s次的数是%d 当前和是%d' % (k, n, my_sum))
        if my_max < n:
            my_max = n
        if my_min > n:
            my_min = n
        if n == 1:
            flag = False
            print('统计：最小值%d 最大值%d' % (my_min, my_max))
        elif n < 1:
            print("已完成n=%d" % x)
    # 将数据生成图
    df = pd.DataFrame(data, columns=[tip])
    df.plot()
    plt.show()


if __name__ == "__main__":
    warnings.filterwarnings('ignore')
    # 解决中文显示
    plt.rcParams['font.family'] = 'SimHei'
    plt.rcParams['axes.unicode_minus'] = False
    # cal(int(input('冰雹猜想：请输入一个>=1的数字：\n')))
    cal(8760)
