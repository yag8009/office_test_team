#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : yag8009
# @FileName  : HeDe_API
# @Time    : 2019/12/10
import requests

from public.log import logger


def hede_test(login_data, url, data):
    """
    和德创建保单
    测试秘钥(secret)为：b0a44d2ac9bb4196b8977360554f91bb
    正式秘钥(secret)为：6c6d55134dc74946aad0601cf1171808
    测试地址：http://apitest.dxtmobile.com/insure/channelPolicy/save
    正式地址：http://insure.hollardchina.com.cn/insure/channelPolicy/save
    :return:
    """
    s = requests.session()
    base_url_login = "http://123.57.15.148/web/a/login"
    header = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
    hede_data_login = dict(login_data)
    res_login = s.post(url=base_url_login, data=hede_data_login, headers=header, timeout=(5, 10))
    if "超级管理员" in res_login.text:
        logger.info("接口 - 登录系统 - 请求成功！")

        base_url_ibaodan = url
        hede_data_ibaodan = dict(data)
        res_ibaodan = s.post(url=base_url_ibaodan, data=hede_data_ibaodan, headers=header, timeout=(5, 10))

        logger.info("请求数据：{}&{}".format(base_url_ibaodan,hede_data_ibaodan))
        return res_ibaodan
    else:
        logger.info("接口 - .../login - 请求失败！ 程序终止...")
        return res_login

if __name__ == '__main__':
    print(hede_test().text)