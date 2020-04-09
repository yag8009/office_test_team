# -*- coding: utf-8 -*-
# @Time    : 2018/11/27 14:07
# @Author  : yag8009
# @File    : chengfabiao.py
# @Software: PyCharm

"""
一行代码实现9*9乘法表
"""


class chengfa:
    def __init__(self, data):
        self.data = int(data)

    def chengfa1(self):
        for i in range(1, self.data):
            for j in range(1, i + 1):
                print("%d*%d=%2d" % (i, j, i * j), end=" ")
            print(" ")

    def chengfa2(self):
        nums = '\n'.join([' '.join(['%s*%s=%-2s' % (y, x, x * y) for y in range(1, x + 1)]) for x in range(1, self.data)])
        return nums


if __name__ == '__main__':
    chengfa("5").chengfa1()
    print(chengfa("5").chengfa2())
