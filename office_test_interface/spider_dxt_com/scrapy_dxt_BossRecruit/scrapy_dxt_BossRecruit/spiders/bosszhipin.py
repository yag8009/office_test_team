# -*- coding: utf-8 -*-
import scrapy

from scrapy_dxt_BossRecruit.items import ScrapyDxtBossrecruitItem


class BosszhipinSpider(scrapy.Spider):
    name = 'bosszhipin'
    # allowed_domains = ['zhipin.com']
    # start_urls = ['http://zhipin.com/job_detail/']


    def start_requests(self):
        search_key = ['测试']
        for key in search_key:
            start_url = "https://www.zhipin.com/job_detail/?query=" + key + "&city=101010100&industry=&position="
            yield scrapy.Request(start_url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        for each in response.xpath('//*[@id="main"]/div/div[2]/ul/li'):
            items = ScrapyDxtBossrecruitItem()
            try:
                items['name'] = each.xpath("./div/div[1]/div[2]/div/h3/a/text()").extract().replace('\n', '').strip()
                items['profession'] = each.xpath("./div/div[1]/div[2]/div/p/a/text()").extract()[0].replace('\n', '').strip()
                items['scale'] = each.xpath("./div/div[1]/div[2]/div/p/text()[2]").extract()[0].replace('\n', '').strip()
                items['touzi'] = each.xpath("./div/div[1]/div[2]/div/p/text()[1]").extract()[0].replace('\n', '').strip()
                items['position'] = each.xpath("./div/div[1]/div[1]/div/div[1]/span[1]/a/text()").extract()[0].replace('\n', '').strip()
                items['diqu'] = each.xpath("./div/div[1]/div[1]/div/div[1]/span[2]/span/text()").extract()[0].replace('\n', '').strip()
                items['salary'] = each.xpath("./div/div[1]/div[1]/div/div[2]/span/text()").extract()[0].replace('\n', '').strip()
                items['years'] = each.xpath("./div/div[1]/div[1]/div/div[2]/p/text()[1]").extract()[0].replace('\n', '').strip()
                items['education'] = each.xpath("./div/div[1]/div[1]/div/div[2]/p/text()[2]").extract()[0].replace('\n', '').strip()
            except:
                print("发生错误！！！")
