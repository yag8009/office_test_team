#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : yag8009
# @FileName  : hede_http_update_lipei
# @Time    : 2020/4/17
import sys

import requests

from public.log import logger


def test_update_liucheng(login_url, login_data, identity, base_url, base_save_url, base_save_data):

    s = requests.session()

    # 登录信息
    login_url = login_url
    header = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
    login_data = dict(login_data)
    req_login = s.post(url=login_url, data=login_data, headers=header, timeout=(5, 10))

    if identity in req_login.text:

        # 获取列表信息（ID）
        base_url = base_url
        logger.info("请求数据：{}".format(base_url))
        base_data = {"pageNo": "1", "pageSize": "100"}

        req_base = s.post(url=base_url, data=base_data, headers=header, timeout=(5, 10))
        logger.info("返回数据：{}".format(req_base.text))

        # 根据ID进行处理
        for i in req_base.json()["list"]:
            base_save_url = base_save_url
            base_save_data = dict(base_save_data)
            base_save_data["bpm.taskId"] = i["id"]
            logger.info("请求数据：{}&{}".format(base_save_url, base_save_data))

            res_base = s.post(url=base_save_url, data=base_save_data, headers=header, timeout=(5, 10))
            logger.info("返回数据：{}".format(res_base.text))
    else:
        logger.info("接口 - {} - 请求失败！ 程序终止...").format(sys._getframe().f_code.co_name)
        return req_login
