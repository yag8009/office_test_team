#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import time
from public import HTMLTestRunner_PY3
from public.tools_class import get_case_list_from_cls
from testcases.test_create_system import test_create_system
from testcases.test_update_hepei import test_update_hepei
from testcases.test_update_hepeizhuguan import test_update_hepeizhuguan
from testcases.test_update_huiweishouhuo import test_update_huiweishouhuo
from testcases.test_update_shouhuozhuguan import test_update_shouhuozhuguan
from testcases.test_update_weixiu import test_update_weixiu


# 装载测试用例interface
test_case_list = get_case_list_from_cls([
    # todo 在项目里面再定义别的测试类，然后装载进来即可
    # 登录单元测试

    # test_create_system,
    # test_update_hepei,
    test_update_weixiu,
    # test_update_hepeizhuguan,
    # test_update_huiweishouhuo,
    # test_update_shouhuozhuguan,
    # test_update_hepeizhuguan,

])

test_suit = unittest.TestSuite()
test_suit.addTests(test_case_list)  # 使用测试套件并打包测试用例

# 获取系统当前时间
now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))

# 定义个报告存放路径，支持相对路径
filename = "./result/" + now + "_result.html"
fp = open(filename, 'wb')

# 定义测试报告
runner = HTMLTestRunner_PY3.HTMLTestRunner(stream=fp, title=u'接口测试报告', description=u'接口数据执行情况：')

# 运行测试用例
runner.run(test_suit)
# 关闭报告文件
fp.close()
