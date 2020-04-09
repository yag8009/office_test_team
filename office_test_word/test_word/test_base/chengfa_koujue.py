#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/27 21:37
# @Author  : yag8009
# @File    : chengfa_koujue.py
# @Software: PyCharm

"""
题目:输出9*9口诀
1程序分析:分行与列考虑,共9行9列,i控制行,j控制列
"""


class chengfa_koujue(object):
	"""docstring for chengfa_koujue"""
	def __init__(self, arg):
		super(chengfa_koujue, self).__init__()
		self.arg = int(arg)

	def chengfa_koujue1(self):
		for i in range(1,self.arg+1):
			for x in range(1,i+1):
				nums = i*x
				print("{}*{}={}".format(i,x,nums), end=" ")
			print(" ")
		
if __name__ == '__main__':
	chengfa_koujue("9").chengfa_koujue1()