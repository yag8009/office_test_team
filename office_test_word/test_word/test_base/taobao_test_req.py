#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : yag8009
# @FileName  : taobao_test_req
# @Time    : 2020/4/22
import requests


def taobao_test_req(url):
    header = {"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"}
    url = url
    req = requests.get(url=url, headers=header, timeout=(5, 10))
    return req

if __name__ == '__main__':
    url = "https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-17260442171.56.d44e63904zFupp&id=596269638185&rn=03bb95bb40a18bf1e1f96c056817ec16&abbucket=8"
    print(taobao_test_req(url).text)
