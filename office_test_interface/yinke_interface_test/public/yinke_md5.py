#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : yag8009
# @FileName  : yinke_md5
# @Time    : 2020/8/3
import hashlib


def MD5_tool(md5data):
    md5 = hashlib.md5()  # 使用MD5加密模式
    md5.update(md5data.encode(encoding='UTF-8'))  # 将参数字符串传入
    sign = md5.hexdigest()
    return sign
