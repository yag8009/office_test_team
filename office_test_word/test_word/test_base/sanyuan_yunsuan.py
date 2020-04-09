# -*- coding: utf-8 -*-
# @Time    : 2018/11/27 11:25
# @Author  : yag8009
# @File    : sanyuan_yunsuan.py
# @Software: PyCharm
"""
三元运算规则
small = a if a < b else b
ss = [i for i in range(1, 11) if i % 2 == 0]
"""
def main():
    a = 10
    b = 20
    small = a if a < b else b
    print(small)
    ss = [i for i in range(1, 11) if i % 2 == 0]
    print(ss)


if __name__ == '__main__':
    main()
