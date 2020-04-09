#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/27 21:37
# @Author  : yag8009
# @File    : paixun.py
# @Software: PyCharm

"""
题目:输入三个整数xyz,请把这三个数由小到大输出
1程序分析:我们想办法把最小的数放到x上,先将ⅹ与y进行比较,如果xy则将x与y的值进行交换,然后再用ⅹ与z进行比较,如果xz则将ⅹ与z的值进行交换,这样能使ⅹ最
"""

class paixun(object):
	"""docstring for paixun"""
	def __init__(self, arg):
		super(paixun, self).__init__()
		self.arg = arg

	def paixun1(self):
		self.arg.sort(reverse=True)
		return self.arg

if __name__ == '__main__':
	print(paixun(["4","1","e","r","0"]).paixun1())
