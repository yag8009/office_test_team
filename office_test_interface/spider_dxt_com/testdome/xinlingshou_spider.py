#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : yag8009
# @FileName  : xinlingshou_spider
# @Time    : 2020/8/20
import requests
from bs4 import BeautifulSoup


def xinlingshuou(url):
    # url = "http://www.scyicheng.net/erp/jxcrj"
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
    }
    res = requests.get(url=url, headers=header)
    # print(res.text)
    bs_page = BeautifulSoup(res.content, features='lxml', from_encoding='utf8')
    article_info = bs_page.find_all(class_='productContent_box')
    for article in article_info:
        article.encode('gb18030')
        with open('f:\\cmp.txt', 'a+') as f:
            f.write(article.text + "\n")
            print(article.text)


if __name__ == '__main__':
    url = input("请输入URL：")
    xinlingshuou(url=url)
