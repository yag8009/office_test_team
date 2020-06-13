# -*- coding: utf-8 -*-
import scrapy


class TychaSpider(scrapy.Spider):
    name = 'tycha'
    allowed_domains = ['tianyancha.com']
    start_urls = ['http://tianyancha.com/']

    def parse(self, response):
        pass
