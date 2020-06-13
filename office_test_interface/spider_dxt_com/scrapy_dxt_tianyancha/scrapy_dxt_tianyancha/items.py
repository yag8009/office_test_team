# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyDxtTianyanchaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 公司名称
    corporate_name = scrapy.Field()
    # 法人
    legal_person = scrapy.Field()
    # 经营状态
    business_status = scrapy.Field()
    # 注册资本
    registered_capital = scrapy.Field()
    # 企业地址
    business_address = scrapy.Field()
    # 电话
    phone = scrapy.Field()
    # 邮箱
    email = scrapy.Field()
