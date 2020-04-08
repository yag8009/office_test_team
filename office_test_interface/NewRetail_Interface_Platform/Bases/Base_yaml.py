#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : yag8009
# @Time    : 2018/12/17 16:54
import os

import yaml

"""
读取、写入yaml信息
"""


class tool_yaml:

    def read_yaml(self, filepath):
        yamlPath = os.path.abspath(filepath)
        f = open(yamlPath, 'r', encoding='utf-8')
        cont = f.read()
        lists = yaml.load(cont)
        return lists

    def write_yaml(self, filepath, data):
        fw = open(filepath, 'a', encoding='utf-8')
        fw_list = []
        for i in data:
            ds = {
                'titlle': i[0].encode().decode('utf-8'),
                'method': i[1].encode().decode('utf-8'),
                'url': i[2].encode().decode('utf-8'),
                'data': i[3].encode().decode('utf-8'),
                'isdata': i[4].encode().decode('utf-8')
            }
            fw_list.append(dict(ds))
        yaml.dump(fw_list, fw)
        return fw_list


if __name__ == '__main__':
    pass
    # data = tool_yaml().read_yaml("..\Config_data\data.yaml")
    # print(data[0]["titlle"])
    # print(data)
    # datas = tool_yaml().read_yaml("..\Config_data\data.yaml")
    # for args in datas:
    #     print(args["method"], args["url"], args["data"], args["isdata"])
    # d = tool_yaml()
    # fdata = base_excel().read_excel("..\\Config_data\\testcase.xlsx")
    # datas = d.write_yaml("..\Config_data\data.yaml", fdata)
    # print(datas)


