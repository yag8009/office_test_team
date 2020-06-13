#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : yag8009
# @FileName  : baidu_pt
# @Time    : 2020/6/13
from fubu_dxt.pyse import Pyse


def baidu_pt():
    driver = Pyse()
    driver.max_window()
    driver.wait(60)
    driver.open("https://www.baidu.com/")
    driver.click('xpath=>//*[@id="u1"]/a[2]')