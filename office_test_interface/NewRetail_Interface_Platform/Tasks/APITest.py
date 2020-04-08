#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : yag8009
# @Time    : 2018/12/19 11:46
import unittest

import requests

from Bases.Base_http import request_http
from Bases.Base_log import get_log
from Bases.Base_assert import is_flag
from Bases.Base_yaml import tool_yaml

logging = get_log()


class APITest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.isaert = []
        self.reqs = request_http(requests.session())

    def http_test(self, method, url, data=None, isdata=None):

        logging.info(" --------- 测试开始 --------- ")
        httpcode = self.reqs.run_http(method=method, url=url, data=data)
        if isdata is not None and type(isdata) == list:
            for i in isdata:
                flag = is_flag(i, httpcode.text)
                self.isaert.append("断言：{}; 断言结果：{}".format(i, flag))
                logging.info(" --------- 断言：{}; 断言结果：{} --------- ".format(i, flag))
                self.assertTrue(flag)
        else:
            flag = is_flag(isdata, httpcode.text)
            self.isaert.append("断言：{}; 断言结果：{}".format(isdata, flag))
            logging.info(" --------- 断言：{}; 断言结果：{} --------- ".format(isdata, flag))
            self.assertTrue(flag)

    @staticmethod
    def getTestFunc(method, url, data=None, isdata=None):
        def func(self):
            self.http_test(method=method, url=url, data=data, isdata=isdata)
        return func

    @classmethod
    def tearDownClass(self):
        self.reqs.base_page_clear()
        logging.info(" --------- 测试结束 --------- ")


def __TestCases():

    datas = tool_yaml().read_yaml("..\Config_data\login.yaml")
    for args in datas:
        if args["data"] is not None and args["data"] != "None":
            setattr(APITest, 'test_{}'.format(args["titlle"]), APITest.getTestFunc(
            method=args["method"], url=args["url"], data=args["data"], isdata=args["isdata"]))
        else:
            setattr(APITest, 'test_{}'.format(args["titlle"]), APITest.getTestFunc(
                method=args["method"], url=args["url"], isdata=args["isdata"]))




__TestCases()
