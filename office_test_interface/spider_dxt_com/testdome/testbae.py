#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : yag8009
# @FileName  : testbae
# @Time    : 2020/7/15
import re


def replace_all_blank(value):
  """
  去除value中的所有非字母内容，包括标点符号、空格、换行、下划线等
  :param value: 需要处理的内容
  :return: 返回处理后的内容
  """
  # \W 表示匹配非数字字母下划线
  result = re.sub('\W+', '', value).replace("_", '')
  print(result)
  return result


if __name__ == '__main__':
    print(replace_all_blank("Powe, on；the 2333, 。(哈哈) ！！看看可以吗？一行代码就可以了！^_^"))