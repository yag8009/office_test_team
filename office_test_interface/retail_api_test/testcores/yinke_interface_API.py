#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
import json

import requests
import time

from public.log import logger


def api_test(url, datas, key):
    """
    将数据排序，使用MD5加密，拼接后post请求
    :param url: 
    :param data: 
    :param key: 
    :return: r.json()
    """
    timestamp = int(time.time())
    data = dict(datas)
    data.update({"timestamp": timestamp})
    data_list = sorted(data.items(), key=lambda e: e[0], reverse=False)
    data_str = "&".join(u"{}={}".format(k, v) for k, v in data_list) + '&' + key
    logger.info("加密前数据: " + data_str)

    md5 = hashlib.md5()  # 使用MD5加密模式
    md5.update(data_str.encode("utf8"))  # 将参数字符串传入
    sign = md5.hexdigest()
    data.setdefault('sign', sign)
    logger.info("签名数据: " + sign)

    r = requests.post(url + json.dumps(data))
    logger.info("请求地址: " + url)
    logger.info("请求数据: " + json.dumps(data))

    return r
