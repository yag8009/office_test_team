#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
import time


def MD5_tool(md5data):
    md5 = hashlib.md5()  # 使用MD5加密模式
    md5.update(md5data.encode("utf8"))  # 将参数字符串传入
    sign = md5.hexdigest()
    return sign

if __name__ == '__main__':
    data = "brand=华为&channelType=227&city=北京&color=白&imei=123456789012345&model=mate9&name=张三&phone=17066668888&price=3999&saleman=售货员A&store=旗舰店&timestamp=1496566760204&key=b0a44d2ac9bb4196b8977360554f91bb"
    md = MD5_tool(data).upper()
    print(md)
    timestamp = int(time.time()*1000)
    print(timestamp)