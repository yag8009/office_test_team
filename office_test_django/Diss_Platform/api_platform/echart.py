#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: echart.py
# @Author: ---
# @Time: 11月 01, 2019
# ---
from pyecharts.charts import Bar, Pie


def API_Bar(title, data):
    bar = Bar(title)
    bar.add(data)
    bar.show_config()
    bar.render()

def API_Pie(title, data):
    pie = Pie(title)
    pie.add(data, is_label_show=True)
    pie.show_config()
    pie.render()