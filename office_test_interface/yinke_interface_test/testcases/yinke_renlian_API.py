#!/usr/bin/env python
# -*- coding: utf-8 -*-
import base64
import json
import sys
sys.path.append("./public/")
from yinke_md5 import *

import random
import time
import requests
import xlrd



def yinke_renlian_API(url, data, key):
    # 排除值为的空信息
    for k in list(data.keys()):
        if not data[k]:
            del data[k]

    if "sign" in data:
        data = data.pop('sign')
    else:
        pass

    # 时间戳
    timestamp = int(time.time() * 1000)
    data = dict(data)
    data.update({"timestamp": timestamp})

    # 排序 A-Z
    # data_list = sorted(data.items(), key=lambda e: e[0], reverse=False)

    # # 格式化加密前的排序方式
    # data_str = "&".join(u"{}={}".format(k, v)
    #                     for k, v in data_list) + '&' + key
    data_str = json.dumps(data, sort_keys=True, separators=(
        '&', '=')).strip("{}").replace('"', '')
    # print("加密前数据: " + data_str)

    # 加密数据
    sign = MD5_tool(data_str)
    data.setdefault('sign', sign)
    # print("签名数据: " + sign)

    # 向服务器端发送请求
    rnum = 0
    while rnum != 200:
        try:
            r = requests.post(url + json.dumps(data))
            # print("请求数据: " + json.dumps(data))
            # print("请求地址: " + url)
            time.sleep(random.randint(1, 3))
            return r
        except:
            rnum = 0
            time.sleep(random.randint(1, 3))


if __name__ == '__main__':

    key = "KBmTWW0nvtC298rJ"
    url = "http://116.196.102.10/svc-xls/a/retail/retailOrder/payOrder?data="
    with open("F:/base64.txt", "r") as f:
        strs = f.read()
    # imgbase = base64.b64decode(strs)
    data = {
        "method": "/retail/retailOrder/payOrder",
        # 设备号111
        "machineType": "123",
        # 实收金额（指的是：最后客户真正支付的金额）111
        "proceedsAmount": "1",
   	    # 商户代码（必填）
   	    "companycode": "974323",
        # 销售单号（必填）111
   	    "vchcode": "SO974323-202009030007TEST",
        "base64Str": strs,
   	    # 收款方式集合 111
   	    "retailPays": [{
                "shroffType": "21",
                "payMoney": "1000",
                "changeMoney": "0",
                "shroffMethod": "大地"
            }],
   	    # 组合收款的种类（必填）
   	    "combinationOfProceeds": "1"
    }

    # sad = json.dumps(data, sort_keys=True, separators=('&', '=')).strip("{}").replace('"','')
    # print(sad)
    result = yinke_renlian_API(url, data, key).text
    print("返回",result)
    
