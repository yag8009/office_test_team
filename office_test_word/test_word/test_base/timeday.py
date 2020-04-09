#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/27 21:37
# @Author  : yag8009
# @File    : timeday.py
# @Software: PyCharm

"""
题目:输入某年某月某日,判断这一天是这一年的第几天?
1程序分析:以3月5日为例,应该先把前两个月的加起来,然后再加上5天即本年的第几天,
特殊情况,闰年且输入月份大于3时需考虑多加一天。

"""

class timeday:
	def __init__(self, data):
		self.data = data

	def timeday1(self):
		year = self.data[:3]
		month = self.data[5:7]
		day = self.data[-2:]

		months = [0,31,59,90,120,151,181,212,243,273,304,334]
		if 0 < int(month) < 12:
			days = months[int(month)-1]
			days += int(day)
		else:
			return "month error"
		if int(year)%4 == 0 and int(year)%100 == 0 or int(year)%400 == 0:
			if int(month) > 2:
				days += 1
			else:
				pass
		else:
			pass

		return days

if __name__ == '__main__':
	print(timeday("2018-11-28").timeday1())