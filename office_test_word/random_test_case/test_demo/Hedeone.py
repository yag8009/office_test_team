#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : yag8009
# @FileName  : Hedeone
# @Time    : 2020/4/28
from public_random.random_ID_card import random_ID_card
from public_random.random_num_digit import random_num_digit


def hede():
    with open('C:\\Users\\admin\\Downloads\\hededata1.csv', 'w+') as f:  # 设置文件对象
        for lix in range(0,150000):
            IDcard = random_ID_card()
            IMEi = random_num_digit(15)
            f.write('VIVO@382@BeiJing@Hei@' + IDcard + '@' + IMEi + '@X27@SongQuanZheng@13717770521@4999@TianMiao@QiJianDian' + "\n")


if __name__ == "__main__":
    hede()
    print("数据生成成功！！！")
