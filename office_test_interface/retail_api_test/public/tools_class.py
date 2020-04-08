#!/usr/bin/env python
# -*- coding: utf-8 -*-

# filename='tools_class'
# author='fayang'
# time='2017/10/23'
import unittest


def get_case_list_from_cls(test_cls_list):
    """
    将测试类转化为测试用例
    :return:
    """
    test_list = []
    for test_cls in test_cls_list:
        test_cases = unittest.TestLoader().loadTestsFromTestCase(test_cls)
        test_list.append(test_cases)
    return test_list
