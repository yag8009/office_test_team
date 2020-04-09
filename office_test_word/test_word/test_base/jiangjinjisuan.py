# -*- coding: utf-8 -*-
# @Time    : 2018/11/27 18:54
# @Author  : yag8009
# @File    : jiangjinjisuan.py
# @Software: PyCharm

"""
题目:企业发放的奖金根据利润提成。
利润低于或等于10万元时,奖金可提10%;
利润高于10万元,低于20万元时,低于10万元的部分按10%提成,高于10万元的部分,可提成7.5%;
20万到40万之间时,高于20万元的部分,可提成5%;
40万到60万之间时,高于40万元的部分,可提成3%;
60万到100万之间时,高于60万元的部分,可提成1.5%;
高于100万元时,超过100万元的部分按1%提成;
从键盘输入当月利润1,求应发放奖金总数?
程序分析:请利用数轴来分界,定位。注意定义时需把奖金定义成长整型。
"""


class jiangjin:
    def __init__(self):
        self.jine = float(input("请输入金额："))
        self.num = 0
        self.num1 = 100000 * 0.1
        print(self.num1)
        self.num2 = self.num1 + 100000 * 0.075
        print(self.num2)
        self.num4 = self.num2 + 200000 * 0.05
        print(self.num4)
        self.num6 = self.num4 + 200000 * 0.03
        print(self.num6)
        self.num10 = self.num6 + 400000 * 0.015
        print(self.num10)

    def jiangjin1(self):
        if self.jine <= 100000:
            self.num = self.jine * 0.1
        elif self.jine <= 200000:
            self.num = self.num1 + (self.jine - 100000) * 0.075
        elif self.jine <= 400000:
            self.num = self.num2 + (self.jine - 200000) * 0.05
        elif self.jine <= 600000:
            self.num = self.num4 + (self.jine - 400000) * 0.03
        elif self.jine <= 1000000:
            self.num = self.num6 + (self.jine - 600000) * 0.015
        else:
            self.num = self.num10 + (self.jine - 1000000) * 0.01
        return self.num


if __name__ == '__main__':
    print(jiangjin().jiangjin1())
