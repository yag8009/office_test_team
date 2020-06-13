# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from openpyxl import Workbook

class ScrapyDxtQccPipeline:
    def __init__(self):
        # 创建excel，填写表头
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append(['公司名称', '法人', '经营状态', '注册资本', '企业地址', '电话', '邮箱'])  # 设置表头

    def process_item(self, item, spider):  # 具体内容
        line = [item['corporate_name'], item['legal_person'], item['business_status'], item['registered_capital'], item['business_address'], item['phone'], item['email']]  # 把数据中项整理出来
        self.ws.append(line)  # 将数据需要保存的项以行的形式添加到xlsx中
        self.wb.save("qcc.xlsx")  # 保存xlsx文件

        return item