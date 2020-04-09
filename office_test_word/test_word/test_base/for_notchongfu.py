# -*- coding: utf-8 -*-
# @Time    : 2018/11/27 18:42
# @Author  : yag8009
# @File    : for_notchongfu.py
# @Software: PyCharm

"""
题目:有1、2、3、4个数字,能组成多少个互不相同且无重复数字的三位数?都是多少?
1程序分析:
可填在百位、十位、个位的数字都是1、2、3、4。
组成所有的排列后再去掉不满足条件的排列

"""


class notchong:
    def __init__(self, data):
        self.data = data

    def notchong1(self, lis=[]):
        for i in self.data:
            for x in self.data:
                for y in self.data:
                    if i is not x and x is not y and i is not y:
                        lis.append((i, x, y))
        return lis


if __name__ == '__main__':
    print(notchong([1, 2, 3, 4]).notchong1())
