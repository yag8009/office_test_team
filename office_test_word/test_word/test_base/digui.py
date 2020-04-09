#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/26 23:11
# @Author  : yag8009
# @File    : digui.py
# @Software: PyCharm

"""
在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数
递推：像上边递归实现所拆解，递归每一次都是基于上一次进行下一次的执行，这叫递推
回溯：则是在遇到终止条件，则从最后往回返一级一级的把值返回来，这叫回溯

python递归的最大层数
"""


class digui:
    def __init__(self, args):
        self.dg = args

    # 递推
    def digui1(self):
        if self.dg == 1:
            return 1
        else:
            return self.dg * digui(self.dg - 1).digui1()

    # 递推2
    def digui2(self):
        if len(self.dg) == 1:
            return "没有人知道这个地方在哪。"
        name = self.dg.pop(0)
        if name == "狗菲":
            return "狗菲说：长沙的小吃街在天心区南门口！！"
        print("<%s>问：你[%s]好，请问你知道长沙的小吃街在哪吗？" % (name, self.dg[0]))
        print("不好意思，我帮您问一下%s,他可能会知道！！\n" % self.dg[0])
        res = digui(self.dg).digui2()
        if name != "我":
            print("<%s>说：%s" % (name, res))
        return res

    # 回溯
    def digui_huisu(self, lishui=[]):
        for item in self.dg:
            if type(item) is not list:
                lishui.append(item)
            else:
                digui(item).digui_huisu()
        return lishui


if __name__ == '__main__':
    data = digui(5)
    print("递推:", data.digui1())
    # digui(5)=digui(4)+2 第一次进入
    # digui(4)=digui(3)+2 第二次进入
    # digui(3)=digui(2)+2 第三次进入
    # digui(2)=digui(1)+2 第四次进入
    # digui(1)=18 第五次进入，最后判断终止条件

    l = [1, 2, [3, [4, 5, 6, [7, 8, [9, 10, [11, 12, 13, [14, 15, [16, [17, ]], 19]]]]]]]
    lists = digui(l)
    print("回溯:", lists.digui_huisu())

    names = ["我", "刘二", "张三", "李四", "狗菲", "王五"]
    print(digui(names).digui2())
