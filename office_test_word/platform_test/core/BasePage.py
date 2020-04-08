#!/usr/bin/env python
# -*- coding: utf-8 -*-


class BasePage(object):
    """
	BasePage封装所有页面都公用的方法，例如driver, url
	"""

    # 初始化driver、url、等
    def __init__(self, selenium_driver):
        self.driver = selenium_driver

    def iopen(self, url):
        # 使用get打开访问链接地址
        self.driver.open(url)
        self.driver.max_window()
