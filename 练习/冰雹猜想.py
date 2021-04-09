# 冰雹猜想
def cal(n):
    t = 0
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
        my_sum += n
        # 补全数字前面的0，让其看起来更整齐
        k = str(t)
        for i in range(6):  # 保留位数直接写死就好
            if t < 10 ** i:
                k = '0' + k
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


if __name__ == "__main__":
    cal(27)
    # cal(7*10_0000_0000_0000)
