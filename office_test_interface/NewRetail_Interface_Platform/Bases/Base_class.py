#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : yag8009
# @Time    : 2018/12/17 16:28
import unittest


def tool_class(cls_list):
    """
    将测试类转化为测试用例
    """
    test_list = []
    for test_cls in cls_list:
        test_cases = unittest.TestLoader().loadTestsFromTestCase(test_cls)
        test_list.append(test_cases)
    return test_list
