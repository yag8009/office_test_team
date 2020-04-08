#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : yag8009
# @FileName  : random_ID_card
# @Time    : 2019/12/11

# 随机身份证
import random
import time


# 随机身份证
def random_ID_card():
    u''' 随机生成新的18为身份证号码 '''
    ARR = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
    LAST = ('1', '0', 'X', 'x', '9', '8', '7', '6', '5', '4', '3', '2')
    t = time.localtime()[0]
    x = '%02d%02d%02d%04d%02d%02d%03d' % (random.randint(10, 99),
                                          random.randint(1, 99),
                                          random.randint(1, 99),
                                          random.randint(t - 80, t - 18),
                                          random.randint(1, 12),
                                          random.randint(1, 28),
                                          random.randint(1, 999))
    y = 0
    for i in range(17):
        y += int(x[i]) * ARR[i]

    return '%s%s' % (x, LAST[y % 11])


if __name__ == "__main__":
    print("随机 身份证:" + random_ID_card()[6:14])
