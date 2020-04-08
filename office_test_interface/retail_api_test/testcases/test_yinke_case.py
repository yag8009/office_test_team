#!/usr/bin/env python
# -*- coding: utf-8 -*-
import configparser
import unittest

import xlrd

from public.log import logger
from testcores import yinke_interface_API


class ActionYinKeTest(unittest.TestCase):
    # 测试前预设
    def setUp(self):
        cf = configparser.ConfigParser()
        cf.read("api_setting.ini")
        self.key = cf.get("interface", "sign_key")
        self.verificationErrors = []

    def action_login(self, case_id, case_name, url, data, assertion, *arge):
        logger.info(u" ====== 【" + case_id + u":" + case_name + u"】 ====== ")
        action_page = yinke_interface_API.api_test(url, eval(data), self.key)
        logger.info(u"返回数据:  " + action_page.text)
        self.assertEqual(action_page.json()["flag"], assertion, action_page.text)

    @staticmethod
    def getTestFunc(case_id, case_name, url, data, assertion,  *arge):
        def func(self):
            self.action_login(case_id, case_name, url, data, assertion)

        return func

    # 测试结束后清理
    def tearDown(self):
        logger.info(" --------- 测试结束 --------- ")
        self.assertEqual([], self.verificationErrors)


def __TestCases():
    cf = configparser.ConfigParser()
    cf.read("api_setting.ini")
    data = xlrd.open_workbook(cf.get("FilePath", "file_path"))
    # 通过索引顺序获取Excel表
    table = data.sheets()[0]
    for args in range(1, table.nrows):
        txt = table.row_values(args)
        setattr(ActionYinKeTest, 'test_login_%s' % txt[1], ActionYinKeTest.getTestFunc(*txt))


__TestCases()
