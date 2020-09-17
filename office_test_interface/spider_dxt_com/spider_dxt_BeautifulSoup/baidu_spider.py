#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : yag8009
# @FileName  : baidu_spider
# @Time    : 2020/7/7
import json
import random
import re
import time

import requests

from spider_dxt_BeautifulSoup.header_spider import headers

s = requests.session()
username = "17301260888"
password = "dxt_12345"

# 获取毫秒级时间戳
def get_tt():
    return int(round((time.time()) * 1000))

# 将callback转换为json
def parsecallback_tojson(callbackstr):
    return json.loads(re.search(r'\(.*\)', callbackstr).group().replace("(", "").replace(")", ""))

# 随机生成callback
def get_callback():
    prefix = "parent.bd__pcbs__"  # callback 前缀
    char = "0123456789abcdefghijklmnopqrstuvwxyz"
    n = random.randint(0, 2147483648)
    suffix = []
    while n != 0:
        suffix.append(char[n % 36])
        n = n // 36
    suffix.reverse()
    print("callback: " + (prefix + ''.join(suffix)))
    return prefix + ''.join(suffix)

# 随机生成gid
def get_gid():
    gid = list("xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx")
    for x in range(len(gid)):
        r = int(random.random() * 16)
        if gid[x] == "x":  # 如果当前值为x
            gid[x] = hex(r).replace("0x", "").upper()
    print("gid: " + "".join(gid))
    return "".join(gid)

def get_token():
    gid = get_gid()
    token_time = get_tt()
    call_back = get_callback()
    token_url = "https://passport.baidu.com/v2/api/?getapi&tpl=pp&apiver=v3&class=login"
    response = s.get(token_url, headers=headers)
    response.encoding = "utf-8"
    token_all = response.text.replace(call_back, "")
    # token_all = eval(token_all)
    print("token:", token_all)
    # return token_all["data"]["token"]



if __name__ == '__main__':
    get_token()