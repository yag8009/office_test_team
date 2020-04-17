#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : yag8009
# @FileName  : hede_http_update_liucheng
# @Time    : 2020/4/17
import configparser
import unittest

import xlrd

from public.log import logger
from testcores.hede_http_update_liucheng import test_update_liucheng

cf = configparser.ConfigParser()
cf.read("api_setting.ini")
login_url = cf.get("LoginUrl", "url")
base_url = cf.get("DaiBanUrl", "url")
file_path = cf.get("LiuChengFilePath", "file_path")

class UpdateLiuChengTest(unittest.TestCase):
    # 测试前预设
    def setUp(self):
        self.verificationErrors = []

    def action_liucheng(self, case_id, case_name, login_data, identity, url, base_save_data, assertion, *arge):
        logger.info(" ====== 【" + case_id + ":" + case_name + "】 ====== ")
        action_page = test_update_liucheng(login_url, eval(login_data), identity, base_url, url, eval(base_save_data))

        logger.info("返回数据:  " + action_page.text)
        self.assertEqual(action_page.json()["message"], assertion, action_page.text)

    @staticmethod
    def getTestFunc(case_id, case_name, login_data, identity, url, base_save_data, assertion, *arge):
        def func(self):
            self.action_liucheng(case_id, case_name, login_data, identity, url, base_save_data, assertion, *arge)

        return func

    # 测试结束后清理
    def tearDown(self):
        logger.info(" --------- 测试结束 --------- ")
        self.assertEqual([], self.verificationErrors)


def __TestCases():
    data = xlrd.open_workbook(file_path)
    # 通过索引顺序获取Excel表
    table = data.sheets()[0]
    for args in range(1, table.nrows):
        txt = table.row_values(args)
        setattr(UpdateLiuChengTest, 'test_hede_%s' % txt[1], UpdateLiuChengTest.getTestFunc(*txt))


__TestCases()