#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : yag8009
# @FileName  : http_update_hepei
# @Time    : 2020/4/21
import random
import sys
import requests

from public.log import logger


def http_update_hepei(login_url, login_data, identity, base_url, base_data, from_url, from_data):
    s = requests.session()

    # 登录请求
    login_url = login_url
    header = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
    login_data = dict(login_data)
    logger.info("请求数据：{}${}".format(login_url, login_data))
    req_login = s.post(url=login_url, data=login_data, headers=header, timeout=(5, 10))
    logger.info("返回状态：{}".format(req_login.status_code))

    if identity in req_login.text:
        # 待办列表查询
        base_url = base_url
        base_data = base_data
        logger.info("请求数据：{}${}".format(base_url, base_data))
        req_base = s.post(url=base_url, data=base_data, headers=header, timeout=(5, 10))
        logger.info("返回数据：{}".format(req_base))

        # 根据ID进行处理
        for i in req_base.json()["list"]:
            # 进行业务办理
            from_url = from_url
            from_data = dict(from_data)
            from_data["maintainType"] = random.choice([1,2])
            from_data["htFormInfo.id"] = i['procIns']['bizKey']
            from_data["bpm.taskId"] = i['id']
            from_data["bpm.procInsId"] = i['procIns']['id']
            logger.info("请求数据：{}&{}".format(from_url, from_data))
            res_base = s.post(url=from_url, data=from_data, headers=header, timeout=(5, 10))
            logger.info("返回数据：{}".format(res_base.text))
    else:
        logger.info("接口 - http_update_hepei - 请求失败！ 程序终止...")
        return req_login


if __name__ == '__main__':
    pass
