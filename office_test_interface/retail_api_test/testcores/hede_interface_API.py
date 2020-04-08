#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : yag8009
# @FileName  : HeDe_API
# @Time    : 2019/12/10
import json
import time

import requests

from public.log import logger
from public.MD5_tools import MD5_tool


def hede_test(url, data, key):
    """
    和德创建保单
    测试秘钥(secret)为：b0a44d2ac9bb4196b8977360554f91bb
    正式秘钥(secret)为：6c6d55134dc74946aad0601cf1171808
    测试地址：http://apitest.dxtmobile.com/insure/channelPolicy/save
    正式地址：http://insure.hollardchina.com.cn/insure/channelPolicy/save
    :return:
    """
    timestamp = int(time.time() * 1000)
    headers = {"Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"}
    datas = dict(data)
    datas.update({"timestamp": timestamp})
    logger.info("传入数据: " + str(datas))
    data_list = sorted(datas.items(), key=lambda e: e[0], reverse=False)
    datas_str = "&".join(u"{}={}".format(k, v) for k, v in data_list) + '&' + 'key' + '=' + key
    logger.info("加密前数据: " + datas_str)

    sign = MD5_tool(datas_str).upper()
    logger.info("签名数据: " + sign)

    datas.update({"sign": sign})
    res = requests.post(url=url, data=datas, headers=headers)
    logger.info("请求地址: " + url)
    logger.info("请求数据: " + json.dumps(datas))
    return res