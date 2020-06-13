#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : yag8009
# @FileName  : test_update_hepei
# @Time    : 2020/4/21
import configparser
import unittest

import xlrd

from public.log import logger
from testcores.http_update_hepei import http_update_hepei

cf = configparser.ConfigParser()
cf.read("api_setting.ini")
file_path = cf.get("HepeiFilePath", "file_path")


class test_update_hepei(unittest.TestCase):
    # 测试前预设
    def setUp(self):
        logger.info(" --------- 测试开始 --------- ")
        self.verificationErrors = []

    def action_hede(self, case_id, case_name, login_url, login_data, identity, base_url, base_date, from_url, from_data, assertion):
        logger.info(u" ====== 【" + case_id + u":" + case_name + u"】 ====== ")
        action_page = http_update_hepei(login_url, eval(login_data), identity, base_url, eval(base_date), from_url, eval(from_data))
        logger.info(u"返回数据:  " + action_page.text)
        self.assertEqual(action_page.json()["message"], assertion, action_page.text)

    @staticmethod
    def getTestFunc(case_id, case_name,login_url, login_data, identity, base_url, base_date, from_url, from_data, assertion):
        def func(self):
            self.action_hede(case_id, case_name,login_url, login_data, identity, base_url, base_date, from_url, from_data, assertion)
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
        setattr(test_update_hepei, 'test_hede_%s' % txt[1], test_update_hepei.getTestFunc(*txt))


__TestCases()