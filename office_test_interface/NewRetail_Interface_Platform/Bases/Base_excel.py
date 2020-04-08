#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : yag8009
# @Time    : 2018/12/24 17:56
import xlrd
import xlsxwriter

"""
1、从yaml文件中读取数据，放到EXCEL中
2、从EXCEL文件中读取数据，放到yaml中
"""


class base_excel:
    def __init__(self):
        filepath = "..\\Config_data\\testcase.xlsx"
        self.work_book = xlsxwriter.Workbook(filepath)
        self.work_sheet = self.work_book.add_worksheet()
        self.work_sheet1 = self.work_book.add_worksheet("图表")

    # 设置表格
    def work_fomat(self, data=None):
        title = ['用例名称', '请求方式', '请求地址', '请求数据', '断言']
        work_format = self.work_book.add_format()
        work_format.set_border(1)
        title_formatter = self.work_book.add_format()
        title_formatter.set_border(1)
        title_formatter.set_bg_color('#cccccc')
        title_formatter.set_align('center')
        title_formatter.set_bold()
        self.work_sheet.write_row('A1', title, title_formatter)

        data_formatter = self.work_book.add_format()
        data_formatter.set_border(1)
        if data is not None:
            for i in range(2, len(data) + 2):
                self.work_sheet.write('A{}'.format(i), str(data[i - 2]['titlle']), data_formatter)
                self.work_sheet.write('B{}'.format(i), str(data[i - 2]['method']), data_formatter)
                self.work_sheet.write('C{}'.format(i), str(data[i - 2]['url']), data_formatter)
                self.work_sheet.write('D{}'.format(i), str(data[i - 2]['data']), data_formatter)
                self.work_sheet.write('E{}'.format(i), str(data[i - 2]['isdata']), data_formatter)
        else:
            print("写入失败 or 文件被占用")

    # 读取excel 数据
    def read_excel(self, file_name):
        bk = xlrd.open_workbook(file_name)
        sh = bk.sheet_by_name("Sheet1")
        row_num = sh.nrows
        row_list = []
        for i in range(1, row_num):
            row_data = sh.row_values(i)
            row_list.append(row_data)
        return row_list

    # 关闭数据流
    def work_close(self):
        self.work_book.close()


if __name__ == '__main__':
    pass
    # b = base_excel()
    # data = tool_yaml().read_yaml("..\Config_data\data.yaml")
    # b.work_fomat(data)
    # b.work_close()
    # # print(b.read_excel("..\\Config_data\\testcase.xlsx"))
