#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : yag8009
# @FileName  : yinke_solr_API
# @Time    : 2020/8/3

import json
import random
import time

import requests

import xlrd

from public.yinke_md5 import MD5_tool


def yinke_solr_API(url, data, key):
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
    data_list = sorted(data.items(), key=lambda e: e[0], reverse=False)

    # 格式化加密前的排序方式
    data_str = "&".join(u"{}={}".format(k, v) for k, v in data_list) + '&' + key
    # print("加密前数据: " + data_str)

    # 加密数据
    sign = MD5_tool(data_str)
    data.setdefault('sign', sign)
    print("签名数据: " + sign)

    # 向服务器端发送请求
    rnum = 0
    while rnum != 200:
        try:
            r = requests.post(url + json.dumps(data))
            print("请求数据: " + json.dumps(data))
            print("请求地址: " + url)
            time.sleep(random.randint(1, 3))
            return r
        except:
            rnum = 0
            time.sleep(random.randint(1, 3))

if __name__ == '__main__':
    key = "KBmTWW0nvtC298rJ"
    url = "http://116.196.102.10/svc-xls/a/basics/product/product/solrList?data="
    # url = "http://116.196.102.10/svc-xls/a/basics/product/product/list?data="

    datas = {
        "method": "/basics/product/product/list",
        "companycode": "974267",
        "ktypeid": "edd513bdbecb4892bb0330f52ef695a7",
        # "categoryId": "018a09d89ee446899c87b50d8f1900ec",
        "searchKey": "华为mate9",
        "pageNo": "1",
        "pageSize": "999"
    }
    result = yinke_solr_API(url, datas, key).json()
    print(result)

    # data = xlrd.open_workbook("F:\\result.xls")
    # # 通过索引顺序获取Excel表
    # table = data.sheets()[0]
    # wb = copy(data)
    # w_sheet = wb.get_sheet(0)
    # for args in range(1, table.nrows):
    #     txt = table.row_values(args)
    #     datas = {
    #         "method": "/basics/product/product/list",
    #         "companycode": "974277",
    #         "ktypeid": "61256",
    #         # "categoryId": txt[0],
    #         "searchKey": txt[1],
    #         "pageNo": "1",
    #         "pageSize": "60"
    #     }
    #     result = yinke_solr_API(url, datas, key).json()
    #     print(result)
    #     time.sleep(random.randint(1, 3))
    #     w_sheet.write(args, 4, str(result))
    #     wb.save("F:\\result.xls")


