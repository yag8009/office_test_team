# -*- coding: utf-8 -*-
# @Time    : 2018/11/27 11:40
# @Author  : yag8009
# @File    : lambda_bds.py
# @Software: PyCharm
"""
lambda表达式格式
map   遍历序列，对序列中每个元素进行操作，最终获取新的序列。
filter     对于序列中的元素进行筛选，最终获取符合条件的序列
reduce          对于序列内所有元素进行累计操作
"""

from functools import reduce

my_lambda = lambda arg: arg + 1
result = my_lambda(123)
print(result)

li = [11, 22, 33]
sl = [1, 2, 3]
new_list = map(lambda a, b: a + b, li, sl)
print(list(new_list))

li = [11, 22, 33]
new_list1 = filter(lambda arg: arg > 22, li)
print(list(new_list1))

lis = [11, 22, 33]
result1 = reduce(lambda arg1, arg2: arg1 + arg2, lis)
print(result1)
