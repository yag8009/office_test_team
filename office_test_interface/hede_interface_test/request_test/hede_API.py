#!/usr/bin/env python
# -*- coding: utf-8 -*-


# @Author  : yag8009
# @FileName  : hede_API
# @Time    : 2020/3/18
import json
import time
import requests

from encryption.md5_hede import md5_hede
from public_random.random_ID_card import random_ID_card
from public_random.random_cn_name import random_cn_name
from public_random.random_number import random_number
from public_random.random_phone import random_phone


def hede_api(url, data, key):
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
    print("请求地址: " + url)
    print("请求数据: " + str(datas))
    data_list = sorted(datas.items(), key=lambda e: e[0], reverse=False)
    datas_str = "&".join(u"{}={}".format(k, v) for k, v in data_list) + '&' + 'key' + '=' + key
    # print("加密前数据: " + datas_str)

    sign = md5_hede(datas_str).upper()
    # print("签名数据: " + sign)

    datas.update({"sign": sign})
    res = requests.post(url=url, data=datas, headers=headers)
    # print("请求地址: " + url)
    # print("请求数据: " + json.dumps(datas))
    return res


if __name__ == '__main__':
    url = 'http://apitest.dxtmobile.com/insure/channelPolicy/save'
    # url = "http://apitest.dxtmobile.com/insure/channelPolicy/updateStateDateById"
    # url = "http://apitest.dxtmobile.com/insure/channelPolicy/updateImei"
    data = {"channelType": "1477", "brand": "华为", "model": "mate30", "color": "亮黑色", "idcard": random_ID_card(),
            "imei": random_number(15), "price": "4999", "phone": "15101014687", "name": random_cn_name(), "city": "北京",
            "store": "旗舰店", "saleman": "售货员A"}
    # with open("C:\\Users\\admin\\Desktop\\test.txt","r", encoding='UTF-8') as f:
    #     for line in f.readlines():
    #         line = line.strip('\n')  # 去掉列表中每一个元素的换行符
    #         # print(eval(line))
    #         key = 'b0a44d2ac9bb4196b8977360554f91bb'
    #         print("返回数据: ", hede_api(url, eval(line), key).text)
    key = 'b0a44d2ac9bb4196b8977360554f91bb'
    print("返回数据: ", hede_api(url, data, key).text)
