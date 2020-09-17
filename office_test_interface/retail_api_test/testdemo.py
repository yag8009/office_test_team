#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : yag8009
# @FileName  : testdemo
# @Time    : 2019/12/17
import json
import time

import requests

from public.MD5_tools import MD5_tool


def testdemo():
    timestamp = int(time.time())
    data = {"username": "cn0101", "password": "123456", "mobileLogin": "1","method": "/login"}
    key = "KBmTWW0nvtC298rJ"
    url = "http://116.196.102.10/svc-xls/a/login?data="
    data.update({"timestamp": timestamp})
    data_list = sorted(data.items(), key=lambda e: e[0], reverse=False)
    data_str = "&".join(u"{}={}".format(k, v) for k, v in data_list) + '&' + key
    print("加密前数据: " + data_str)


    sign = MD5_tool(data_str)
    data.setdefault('sign', sign)
    print("签名数据: " + sign)

    r = requests.post(url + json.dumps(data), timeout=3)
    print("请求地址: " + url)
    print("请求数据: " + json.dumps(data))
    print("返回数据: ", r.status_code )


testdemo()