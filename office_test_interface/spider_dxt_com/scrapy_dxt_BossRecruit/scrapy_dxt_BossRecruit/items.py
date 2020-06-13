# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyDxtBossrecruitItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 公司名称
    name = scrapy.Field()
    # 行业
    profession = scrapy.Field()
    # 规模
    scale = scrapy.Field()
    # 投资
    touzi = scrapy.Field()
    # 招聘职位
    position = scrapy.Field()
    # 地区
    diqu = scrapy.Field()
    # 招聘薪资
    salary = scrapy.Field()
    # 招聘年限
    years = scrapy.Field()
    # 学历
    education = scrapy.Field()
