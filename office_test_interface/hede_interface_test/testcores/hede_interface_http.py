#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : yag8009
# @FileName  : HeDe_API
# @Time    : 2019/12/10
import requests


def hede_test():
    """
    创建保单
    """
    s = requests.session()
    base_url_login = "http://123.57.15.148/web/a/login"
    header = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
    hede_data_login = {"username": "0DCC1FB7100A1D8D31B3A55DFCC7DFA2",
                       "password": "A1EAF07BB51B073BB923BD5BEB1AC8F8"}
    res_login = s.post(url=base_url_login, data=hede_data_login, headers=header, timeout=(5, 10))
    # base_url = "http://123.57.15.148/web/a/bpm/bpmMyTask/listData?status=1"
    # res_base = s.post(url=base_url, headers=header, timeout=(5, 10))
    # for i in res_base.json()["list"]:
    #     # id_list.append(i["id"])
    #     dasta = ""
    #     rea = s.post(url="http://123.57.15.148/web/a/htclaimsettlementform/htClaimSettlementForm/save",data=dasta, headers=header, timeout=(5, 10))
    #     sb = rea.text
    #     print(sb)

    return res_login


if __name__ == '__main__':
    print(hede_test().text)

