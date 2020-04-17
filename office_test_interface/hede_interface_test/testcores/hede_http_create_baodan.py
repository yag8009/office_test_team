#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : yag8009
# @FileName  : hede_http_create_baodan
# @Time    : 2020/4/17

import sys
import requests

from public.log import logger


def http_create_bandan(login_url, login_data, base_url, base_data):
    """
    创建保单
    :param login_url: 登录地址
    :param login_data: 登录信息
    :param base_url: 创建保单地址
    :param base_data: 创建保单数据
    :return:
    """
    s = requests.session()

    login_url = login_url
    header = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
    login_data = dict(login_data)
    req_login = s.post(url=login_url, data=login_data, headers=header, timeout=(5, 10))
    if "超级管理员" in req_login.text:
        # logger.info("接口 - 登录系统 - 请求成功！")

        base_url = base_url
        base_data = dict(base_data)
        req_base = s.post(url=base_url, data=base_data, headers=header, timeout=(5, 10))

        logger.info("请求数据：{}&{}".format(base_url, base_data))
        return req_base
    else:
        logger.info("接口 - {} - 请求失败！ 程序终止...").format(sys._getframe().f_code.co_name)
        return req_login


if __name__ == '__main__':
    pass
