# -*- coding: utf-8 -*-
import scrapy

from scrapy_dxt_qcc.items import ScrapyDxtQccItem


class QccspiderSpider(scrapy.Spider):
    name = 'qccspider'
    allowed_domains = ['qcc.com']
    start_urls = ['https://www.qcc.com/g_BJ']
    url = "https://www.qcc.com/g_BJ_"

    offset = 1

    def parse(self, response):
        for each in response.xpath('//*[@id="searchlist"]/table/tbody/tr'):
            if "在业" in each.xpath("./td[3]/span").extract()[0]:
                item = ScrapyDxtQccItem()
                try:
                    item['corporate_name'] = ''.join(each.xpath("./td[2]/a/text()").extract()).replace('\n', '').strip()
                    item['legal_person'] = each.xpath("./td[2]/p[1]/a/text()").extract()[0].replace('\n', '').strip()
                    item['business_status'] = each.xpath("./td[3]/span/text()").extract()[0].replace('\n', '').strip()
                    item['registered_capital'] = each.xpath("./td[2]/p[1]/span[1]/text()").extract()[0].replace('\n',
                                                                                                                '').strip()
                    item['business_address'] = each.xpath("./td[2]/p[3]/text()").extract()[0].replace('\n', '').strip()
                    item['phone'] = each.xpath("./td[2]/p[2]/span/text()").extract()[0].replace('\n', '').strip()
                    item['email'] = each.xpath("./td[2]/p[2]/text()").extract()[0].replace('\n', '').strip()
                except:
                    print("发生错误！！！")

                yield item

        if self.offset < 501:
            self.offset += 1

            # 每次处理完一页的数据之后，重新发送下一页页面请求
            # self.offset自增10，同时拼接为新的url，并调用回调函数self.parse处理Response
        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)