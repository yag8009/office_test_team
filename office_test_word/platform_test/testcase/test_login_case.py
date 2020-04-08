#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 导入方法
import unittest
import time
import xlrd
from public import saveScreenshot
from core import LoginPage
from public.log import logger
from public.pyse import Pyse
import configparser


# 定义测试类
class LoginTest(unittest.TestCase):
    # 测试前预设
    def setUp(self):
        cf = configparser.ConfigParser()
        cf.read("setting.ini")
        self.driver = Pyse(cf.get("Setting", "driver"))
        self.driver.wait(60)
        self.url = cf.get("Setting", "url")
        self.verificationErrors = []

    def action_login(self, case_id, case_name, username, password, *arge):
        # ***** 【登录模块】 *****
        login_page = LoginPage.LoginPage(self.driver, self.url)
        logger.info(u"===== 【" + case_id + u"】" + case_name + u" =====")
        logger.info("用户名:" + username + "  密码:" + password)
        # 调用用户名输入组件
        login_page.test_user_login(username, password)
        time.sleep(2)
        saveScreenshot.saveScreenshot(self.driver, "登录模块")
        try:
            self.assertEqual(self.driver.get_title(), u"系统")
            logger.info(u"***** 【登录成功】 *****")
        except:
            logger.info(u"***** 【登录失败】 *****")

    @staticmethod
    def getTestFunc(case_id, case_name, username, password, *arge):
        def func(self):
            self.action_login(case_id, case_name, username, password, *arge)

        return func

    # 测试结束后清理
    def tearDown(self):
        self.assertEqual([], self.verificationErrors)


def __TestCases():
    cf = configparser.ConfigParser()
    cf.read("setting.ini")
    data = xlrd.open_workbook(cf.get("FilePath", "file_path"))
    # 通过索引顺序获取Excel表
    table = data.sheets()[0]
    for args in range(1, table.nrows):
        txt = table.row_values(args)
        setattr(LoginTest, 'test_login_%s' % txt[1], LoginTest.getTestFunc(*txt))


__TestCases()
