#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : yag8009
# @FileName  : dxt_xinliang_spider
# @Time    : 2020/7/23
import requests

from spider_dxt_BeautifulSoup.header_spider import headers


def dxt_bosszhipin_spider():
    url = "https://www.zhipin.com/job_detail/"
    payload  = {
        "query":"测试",
        "city":"100010000",
        "industry":"",
        "position":""
    }
    Cookies = {
        "cookie": "lastCity=101010100; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1595497407; __zp__pub__=; __c=1595497407; __g=-; _uab_collina=159549740700581381666547; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1595497438; __l=l=%2Fwww.zhipin.com%2F%3Fka%3Dheader-home-logo&r=https%3A%2F%2Fwww.zhipin.com%2Fjob_detail%2F%3Fquery%3D%E6%B5%8B%E8%AF%95%26city%3D100010000%26industry%3D%26position%3D&friend_source=0&friend_source=0; __a=11969542.1595497407..1595497407.2.1.2.2; t=8P6XuC8yahUckaeh; wt=8P6XuC8yahUckaeh",
    }
    headers.update(Cookies)
    # req = requests.session()
    bossres = requests.get(url=url,headers=headers,params=payload,verify=False)
    bossres.encoding='utf-8'
    print(bossres.text)



if __name__ == '__main__':
    dxt_bosszhipin_spider()