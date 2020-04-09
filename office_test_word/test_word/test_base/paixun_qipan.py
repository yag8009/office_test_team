# -*- coding: utf-8 -*-
# @Time    : 2018/11/27 14:07
# @Author  : yag8009
# @File    : paixun_qipan.py
# @Software: PyCharm

"""
题目:要求输出国际象棋棋盘。
1程序分析:用i控制行,j来控制列,根据j的和的变化来控制输出黑方格,还是白方格。
"""

class paixun_qipan(object):
	"""docstring for paixun_qipan"""
	def __init__(self, arg):
		super(paixun_qipan, self).__init__()
		self.arg = arg
