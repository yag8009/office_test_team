#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : yag8009
# @FileName  : testDemoYear
# @Time    : 2020/6/17
import unittest

from testdome.DemoYear import testdemo


class testDemoYear(unittest.TestCase):
    def setUp(self) -> None:
        """ 测试前的准备工作"""
        self.is_E = "请检查是否输入正确年份。"
        self.is_R = "年是闰年"
        self.is_P = "年是平年"

    def test_teshu(self):
        """特殊字符"""
        self.assertEqual(self.is_E, testdemo(" "))

    def test_zhongwen(self):
        """中文"""
        self.assertEqual(self.is_E, testdemo("中文"))

    def test_yingwen(self):
        """英文"""
        self.assertEqual(self.is_E, testdemo("yes or no？"))

    def test_fushu(self):
        """负数"""
        self.assertEqual(self.is_E, testdemo("-1"))

    def test_qutashuzi(self):
        """其他类型数字"""
        self.assertEqual(self.is_E, testdemo("0"))
        self.assertEqual(self.is_E, testdemo("12"))
        self.assertEqual(self.is_E, testdemo("123"))
        self.assertEqual(self.is_E, testdemo("12345"))

    def test_rnian(self):
        """闰年"""
        self.assertEqual(("1988" + self.is_R), testdemo("1988"))

    def test_pnian(self):
        """平年"""
        self.assertEqual(("1234" + self.is_P), testdemo("1234"))

    def tearDown(self) -> None:
        """测试后的收尾工作"""
        pass


if __name__ == '__main__':
    testDemoYear()