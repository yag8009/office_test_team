#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Author  : yag8009
# @Time    : 2018/12/23 15:22
import requests

from Bases.Base_log import get_log

"""
http配置类，封装get，post方法。
输入信息包括：
请求域名，请求url，http头设置，请求数据
"""
logging = get_log()


class Base_page(object):
    def __init__(self, requests_session):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/69.0.3497.100 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9'
        }

        self.req = requests_session
        self.req.headers.update(headers)

    def base_page_clear(self):
        return self.req.close()


class request_http(Base_page):
    def __init__(self, req):
        super(request_http, self).__init__(req)

    def run_http(self, method, url, data=None):
        if method == "post" or method == "Post" or method == "POST":
            if data is not None:
                res = self.req.post(url, data)
                logging.info(
                    "请求参数：method={method},url={url},data={data}".format(
                        method=method, url=url, data=data))
            else:
                res = self.req.post(url)
                logging.info(
                    "请求参数：method={method},url={url}".format(method=method, url=url))
        elif method == "get" or method == "Get" or method == "GET":
            if data is not None:
                res = self.req.post(url, data)
                logging.info(
                    "请求参数：method={method},url={url},data={data}".format(
                        method=method, url=url, data=data))
            else:
                res = self.req.get(url)
                logging.info(
                    "请求参数：method={method},url={url}".format(method=method, url=url))
        else:
            logging.info("请选择请求方式：POST or GET ")

        logging.info("响应状态码:--- {} ---".format(res.status_code))
        return res


if __name__ == '__main__':
    method = "post"
    url = "http://123.196.123.106/web-xls/a/login"
    params = {'username': 'xv01111', 'password': "123456"}
    reqs = request_http(requests.session())
    res = reqs.run_http(method=method, url=url, data=params)
    # print(res.text)
    print(res.cookies)
    print(res.headers)
    method = "post"
    url = "http://123.196.123.106/web-xls/a/basics/product/productCategory/"
    params = {'name': '国', 'beginCreateDate': None, 'endCreateDate': None, 'beginUpdateDate': None, 'endUpdateDate': None}
    res = reqs.run_http(method=method, url=url, data=params)
    print(res.text)
    print(res.cookies)
    print(res.headers)

