#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : yag8009
# @FileName  : random_num_digit
# @Time    : 2019/12/11

# 随机 n位数字字符
import random
import string


# 随机 数字
def random_num_digit(length=15):
    num = ''.join(random.choice(string.digits) for _ in range(length))
    return num


if __name__ == "__main__":
    print("随机 数字:" + random_num_digit(15))
