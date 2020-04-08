#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : yag8009
# @FileName  : testxlsx
# @Time    : 2019/12/11
from public_excel.excel_xlsx import write_excel_xlsx
from public_random.random_ID_card import random_ID_card
from public_random.random_cn_name import random_cn_name
from public_random.random_phone import random_phone
from public_random.random_string import random_string


def core_xlsx(length=1):
    data_list = []
    idname = "case_"
    name = "用例"
    url = "http://apitest.dxtmobile.com/insure/channelPolicy/save"
    for x in range(0,length):
        phone = random_phone()
        cn_name = random_cn_name()
        cn_id = random_ID_card()
        IMEImun = random_string(15)
        data_list.append([idname+str(x),name+str(x),url,{'phone':phone,'cn_name':cn_name,'cn_id':cn_id,'IMEImun':IMEImun},"success"])
    return data_list


if __name__ == "__main__":
    print(core_xlsx(10))
    book_name_xlsx = '../data/xlsx格式测试工作簿.xlsx'
    sheet_name_xlsx = 'xlsx格式测试表'
    value3 = core_xlsx(10)
    write_excel_xlsx(book_name_xlsx, sheet_name_xlsx, value3)