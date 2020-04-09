#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/27 21:03
# @Author  : yag8009
# @File    : pin_fang_shu.py
# @Software: PyCharm
"""
题目:一个整数,它加上100后是一个完全平方数,再加上268又是一个完全平方数,请问该数是多少?
1程序分析:在10万以内判断,先将该数加上100后再开方,再将该数加上268后再开方如果开方后的结果满足如下条件,即是结果。
"""
import math


class pinfang:
    def __init__(self, data):
        self.data = int(data)
        self.lis = []

    def pinfang1(self):
        for i in range(0, self.data):
            x = int(math.sqrt(i + 100))
            y = int(math.sqrt(x + 268))
            if (x * x == i + 100) and (y * y == x + 268):
                self.lis.append(i)
        return self.lis

if __name__ == '__main__':
    print(pinfang(20000).pinfang1())
