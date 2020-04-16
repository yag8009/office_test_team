#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : yag8009
# @FileName  : random_phone
# @Time    : 2020/3/19

# 随机手机号
import random

from public_random.random_number import random_number


def random_phone():
    ps = ["139", "138", "137", "136", "135", "134", "178", "170", "188", "187", "183", "182", "159", "158", "157",
          "152", "199", "198",
          "150", "147", "186", "185", "170", "156", "155", "130", "131", "132", "189", "180", "170", "153", "133"]
    # ps = ["155"]
    phone = str(random.choice(ps)) + str(random_number(8))
    return phone


if __name__ == "__main__":
    print("随机 手机号:" + random_phone())
