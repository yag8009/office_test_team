#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : yag8009
# @FileName  : main
# @Time    : 2020/6/8

from scrapy import cmdline
# cmdline.execute("scrapy crawl qccspider -o qccspider.csv".split())
# cmdline.execute("cd scrapy_dxt_qcc".split())
cmdline.execute("scrapy crawl qccspider".split())