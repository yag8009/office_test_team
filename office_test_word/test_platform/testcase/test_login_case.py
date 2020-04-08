#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import time
import xlrd
from public import saveScreenshot
from core import LoginPage
from test import support
from public.log import logger
from public.pyse import Pyse


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = Pyse("chrome")
        self.driver.wait(10)
        self.url = "http://dxttest.dxtmobile.com/dxtyhch/a/login"
        self.verificationErrors = []


    def action_login(self, case_id='case_0000', case_summary=u'正确验证', username=u'73103741刘婷', password=u'000000'):
        login_page = LoginPage.LoginPage(self.driver, self.url, u"萃花销售助手 登录")
        login_page.iopen()
        logger.info(u"======== 【" + case_id + u"】" + case_summary + u" ========")
        logger.info("username:"+username+"  password:"+password)
        # 调用用户名输入组件
        login_page.type_username(username)
        login_page.type_password(password)
        login_page.submit()
        time.sleep(3)
        saveScreenshot.saveScreenshot(self.driver, u"登录")
        try:
            assert (self.driver.get_title() == u"萃花销售助手"), u"登录成功"
            logger.info(u"登录成功")
        except:
            logger.info(u"登录失败")

    @staticmethod
    def getTestFunc(case_id, case_summary, username, password):
        def func(self):
            self.action_login(case_id, case_summary, username, password)
        return func

    def tearDown(self):
        self.driver.close()
        self.assertEqual([], self.verificationErrors)

def __generateTestCases():
    data = xlrd.open_workbook(r"./data/login_126mail_data.xls")
    # 通过索引顺序获取Excel表
    table = data.sheets()[0]
    for args in range(1, table.nrows):
        txt = table.row_values(args)
        setattr(LoginTest, 'test_login_%s' % txt[1], LoginTest.getTestFunc(*txt))
__generateTestCases()
if __name__ == '__main__':
    support.run_unittest(LoginTest)

