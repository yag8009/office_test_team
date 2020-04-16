#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : yag8009
# @FileName  : random_string
# @Time    : 2020/3/19

import random
import string


# 随机大小写英文+数字字符
def random_string(size=1, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


# 随机大小写英文
def random_letters(size=1, chars=string.ascii_letters):
    return ''.join(random.choice(chars) for _ in range(size))


# 随机大写英文
def random_uppercase(size=1, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size))


# 随机小写英文
def random_lowercase(size=1, chars=string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))


if __name__ == "__main__":
    print("随机 大小写英文+数字:" + random_string(15))
    print("随机 大小写英文:" + random_letters(15))
    print("随机 大写英文:" + random_uppercase(15))
    print("随机 小写英文:" + random_lowercase(15))