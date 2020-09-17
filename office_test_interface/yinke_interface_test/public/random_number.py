#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : yag8009
# @FileName  : random_number
# @Time    : 2020/3/19
import random
import string


def random_number(length=15):
    num = ''.join(random.choice(string.digits) for _ in range(length))
    return num


if __name__ == "__main__":
    print("随机 数字:" + random_number(15))