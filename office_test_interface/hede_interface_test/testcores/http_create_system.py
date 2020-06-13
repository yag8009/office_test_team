#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : yag8009
# @FileName  : http_create_system
# @Time    : 2020/4/21
import sys
import requests

from public.log import logger


def http_create_system(login_url, login_data, identity, base_url, base_data):
    s = requests.session()

    # 登录请求
    login_url = login_url
    header = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
    login_data = dict(login_data)
    logger.info("请求数据：{}${}".format(login_url, login_data))
    req_login = s.post(url=login_url, data=login_data, headers=header, timeout=(5, 10))
    logger.info("返回状态：{}".format(req_login.status_code))

    if identity in req_login.text:
        # 进行业务办理
        base_url = base_url
        base_data = dict(base_data)
        logger.info("请求数据：{}&{}".format(base_url, base_data))
        req_base = s.post(url=base_url, data=base_data, headers=header, timeout=(5, 10))
        logger.info("返回状态：{}".format(req_base.status_code))
        return req_base
    else:
        logger.info("接口 - http_create_system - 请求失败！ 程序终止...")
        return req_login


if __name__ == '__main__':
    pass
