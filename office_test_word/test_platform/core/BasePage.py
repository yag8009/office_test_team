#!/usr/bin/env python
# -*- coding: utf-8 -*-
class BasePage(object):
	"""
	BasePage封装所有页面都公用的方法，例如driver, url
	"""
	#初始化driver、url、等
	def __init__(self, selenium_driver, base_url, pagetitle):
		self.base_url = base_url
		self.pagetitle = pagetitle
		self.driver = selenium_driver

	def _iopen(self, url, pagetitle):
		# 使用get打开访问链接地址
		self.driver.open(url)
		self.driver.max_window()
		# 使用assert进行校验，打开的链接地址是否与配置的地址一致。调用on_page()方法
		assert self.on_page(pagetitle), u"打开开页面失败 %s" % url

	# 定义open方法，调用_open()进行打开链接
	def iopen(self):
		self._iopen(self.base_url, self.pagetitle)

	# 使用current_url获取当前窗口Url地址，进行与配置地址作比较，返回比较结果（True False）
	def on_page(self, pagetitle):
		return pagetitle in self.driver.get_title()
