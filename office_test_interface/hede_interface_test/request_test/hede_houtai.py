#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : yag8009
# @FileName  : hede_houtai
# @Time    : 2020/4/16
import requests


def hede_houtai_login():
    s = requests.session()
    base_url_login = "http://123.57.15.148/web/a/login"
    header = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
    hede_data_login = {"username": "F3EDC7D2C193E0B8DCF554C726719ED2",
                       "password": "235880C505ACCDA5C581A4F4CDB81DA0"}
    res_login = s.post(url=base_url_login, data=hede_data_login, headers=header, timeout=(5, 10))
    if "超级管理员" in res_login.text:
        print("接口 - 登录系统 - 请求成功！")

        base_url_ibaodan = "http://123.57.15.148/web/a/forminfo/htFormInfo/save"
        hede_data_ibaodan = {"id": "",
                             "policyInfo.id": "1232217095095058432",
                             "remarks": "自动化测试数据-00003",
                             "status": "4",
                             "bpm.taskId": "",
                             "bpm.procInsId": "",
                             "bpm.activityId": "undefined"}
        res_ibaodan = s.post(url=base_url_ibaodan, data=hede_data_ibaodan, headers=header, timeout=(5, 10))
    else:
        print("接口 - .../login - 请求失败！ 程序终止...")
    return res_ibaodan




if __name__ == '__main__':
    print(hede_houtai_login().text)
    # print(hede_houtai_login().status_code)
    # print(hede_houtai_login().cookies)
