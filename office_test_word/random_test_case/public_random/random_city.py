#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : yag8009
# @FileName  : random_city
# @Time    : 2019/12/11

# 随机选一个市
import random

from city_menu import city_menu


def random_city():
    citys = []
    city_menus = city_menu()
    for i in range(0, 1):
        s = list(city_menus.keys())  # 省列表
        sheng = random.choice(s)  # 随机选一个省
        citys.append(sheng)
        ci = list(city_menus[sheng].keys())
        city = random.choice(ci)  # 随机选一个市
        citys.append(city)
        qu = list(city_menus[sheng][city].keys())
        quyu = random.choice(qu)  # 随机选一个区
        citys.append(quyu)

    return citys


if __name__ == "__main__":
    print("随机 选一个市:" + str(random_city()))
    print("随机 选一个市:", ''.join(random_city()))
