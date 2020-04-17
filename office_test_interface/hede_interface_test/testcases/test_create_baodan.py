#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : yag8009
# @FileName  : test_hede_case
# @Time    : 2019/12/10

import configparser
import unittest
import xlrd

from public.log import logger
from testcores.hede_http_create_baodan import http_create_bandan

cf = configparser.ConfigParser()
cf.read("api_setting.ini")
login_url = cf.get("LoginUrl", "url")
baoban_url = cf.get("BaoDanUrl", "url")
file_path = cf.get("BaoDanFilePath", "file_path")


class CraeteBaoDan(unittest.TestCase):
    # 测试前预设
    def setUp(self):
        self.verificationErrors = []

    def action_login(self, case_id, case_name, login_data, baodan_data, assertion):
        logger.info(u" ====== 【" + case_id + u":" + case_name + u"】 ====== ")
        action_page = http_create_bandan(login_url, eval(login_data), baoban_url, eval(baodan_data))
        logger.info(u"返回数据:  " + action_page.text)
        self.assertEqual(action_page.json()["message"], assertion, action_page.text)

    @staticmethod
    def getTestFunc(case_id, case_name, login_data, baodan_data, assertion):
        def func(self):
            self.action_login(case_id, case_name, login_data, baodan_data, assertion)
        return func

    # 测试结束后清理
    def tearDown(self):
        logger.info(" --------- 测试结束 --------- ")
        self.assertEqual([], self.verificationErrors)


def __TestCases():
    filedata = xlrd.open_workbook(file_path)
    # 通过索引顺序获取Excel表
    table = filedata.sheets()[0]
    for args in range(1, table.nrows):
        txt = table.row_values(args)
        setattr(CraeteBaoDan, 'test_hede_%s' % txt[1], CraeteBaoDan.getTestFunc(*txt))


__TestCases()
