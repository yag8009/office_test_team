#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : yag8009
# @Time    : 2018/12/19 15:25

# 判断一个字符串是否在另外一个字符串中


def is_flag(str_one, str_two):
    """
    str_one: 查找的字符串
    str_two:  被查找的字符串
    """
    flag = None
    if str_one in str_two:
        flag = True
    else:
        flag = False
    return flag
