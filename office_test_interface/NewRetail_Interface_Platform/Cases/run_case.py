#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : yag8009
# @Time    : 2018/12/17 16:34
import time
import unittest

from Bases.Base_class import tool_class
from Bases.Base_mail import base_email
from Bases.HTMLTestRunner_PY3 import HTMLTestRunner

from Tasks.APITest import APITest

test_case_list = tool_class([
    # todo 在项目里面再定义别的测试类，然后装载进来即可
    APITest
])
test_suit = unittest.TestSuite()
test_suit.addTests(test_case_list)  # 使用测试套件并打包测试用例
# 获取系统当前时间
now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
# 定义个报告存放路径，支持相对路径
filename = "../Result/" + now + "_result.html"
fp = open(filename, 'wb')
# 定义测试报告
runner = HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例执行情况：')
# 运行测试用例
runner.run(test_suit)
# 关闭报告文件
fp.close()
filenames = "../Result/logging.log"
base_email().run_mail(filename, filenames)
