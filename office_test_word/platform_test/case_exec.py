#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import time
from public import HTMLTestRunner

# 定义单元测试容器pip
from public.tools_class import get_case_list_from_cls
from testcase.test_login_case import LoginTest

# 装载测试用例
test_case_list = get_case_list_from_cls([
    # todo 在项目里面再定义别的测试类，然后装载进来即可
    LoginTest  # 登录单元测试

])

test_suit = unittest.TestSuite()
test_suit.addTests(test_case_list)  # 使用测试套件并打包测试用例

# 获取系统当前时间
now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))

# 定义个报告存放路径，支持相对路径
filename = "./result/" + now + "_result.html"
fp = open(filename, 'wb')

# 定义测试报告
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'自动化测试报告', description=u'用例执行情况：')

# 运行测试用例
runner.run(test_suit)
# 关闭报告文件
fp.close()
