#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/26 21:34
# @Author  : yag8009
# @File    : IP_int.py
# @Software: PyCharm

"""
请编写一个函数实现将IP地址转换成一个整数。
bin(args) 转换为二进制
"""


class IP_int:
    def __init__(self, ips):
        self.ip = ips.split(".")

    def intip(self):
        try:
            ip_1 = bin(int(self.ip[0]))[2:]
            ip_2 = bin(int(self.ip[1]))[2:]
            ip_3 = bin(int(self.ip[2]))[2:]
            ip_4 = bin(int(self.ip[3]))[2:]
            ip_num = int(ip_1 + ip_2 + ip_3 + ip_4, base=2)
            return ip_num
        except:
            return ("无法转换！！！请检查是否正确输入IP。")


if __name__ == '__main__':
    my_input = "192.168.1.100"
    my_input.strip(" ")
    print("转换为整数：", IP_int(my_input).intip())
