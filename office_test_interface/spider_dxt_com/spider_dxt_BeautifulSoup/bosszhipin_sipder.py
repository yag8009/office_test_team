#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : yag8009
# @FileName  : bosszhipin_sipder
# @Time    : 2020/6/28
import requests
from bs4 import BeautifulSoup

from spider_dxt_BeautifulSoup.header_spider import headers


def bosszhipin_sipder():
    '''获取第page的数据，搜索关键字kw'''
    kw ="python开发"
    page = "1"
    url = "https://www.zhipin.com/c101020100/?query=" + kw + "&page=" + str(page) + "&ka=page-" + str(page)
    cookies = {
        "lastCity": "101010100",
        "_uab_collina": "156594127160811552815566",
        "sid": "sem_pz_bdpc_dasou_title",
        "__c": "1566178735",
        "__g": "sem_pz_bdpc_dasou_title",
        "__l": "l=%2Fwww.zhipin.com%2F%3Fsid%3Dsem_pz_bdpc_dasou_title&r=https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fDIFkY0IWPB0KZEgsA_ON-I00000Kd7ZNC00000Irp6hc.THdBULP1doZA80K85yF9pywdpAqVuNqsusK15yRLPH6zuW-9nj04nhRLuhR0IHYYn1mzwW9AwHIawWmdrRN7P1-7fHN7wjK7nRNDfW6Lf6K95gTqFhdWpyfqn1czPjmsPjnYrausThqbpyfqnHm0uHdCIZwsT1CEQLILIz4lpA-spy38mvqVQ1q1pyfqTvNVgLKlgvFbTAPxuA71ULNxIA-YUAR0mLFW5Hfsrj6v%26tpl%3Dtpl_11534_19713_15764%26l%3D1511867677%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253DBoss%2525E7%25259B%2525B4%2525E8%252581%252598%2525E2%252580%252594%2525E2%252580%252594%2525E6%252589%2525BE%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E6%252588%252591%2525E8%2525A6%252581%2525E8%2525B7%25259F%2525E8%252580%252581%2525E6%25259D%2525BF%2525E8%2525B0%252588%2525EF%2525BC%252581%2526xp%253Did(%252522m3224604348_canvas%252522)%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D8%26wd%3Dboss%25E7%259B%25B4%25E8%2581%2598%26issp%3D1%26f%3D8%26ie%3Dutf-8%26rqlang%3Dcn%26tn%3Dbaiduhome_pg%26sug%3Dboss%2525E7%25259B%2525B4%2525E8%252581%252598%2525E5%2525AE%252598%2525E7%2525BD%252591%26inputT%3D4829&g=%2Fwww.zhipin.com%2F%3Fsid%3Dsem_pz_bdpc_dasou_title",
        "Hm_lvt_194df3105ad7148dcf2b98a91b5e727a": "1565941272,1566178735",
        "__zp_stoken__": "c839%2FbUp4y%2FcG59Q1lQU84czePIXK3dDRi%2F3AGRWQ6KVQWUNKQa4lxpn2jAVyXKDRxk0g3H19loBTLIK4KtUfLuxbQ%3D%3D",
        "__a": "74852898.1565941271.1565941271.1566178735.32.2.3.3",
        "Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a": "1566178748",
    }
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
        "referer": "https://www.zhipin.com/c101020100/?query=python%E5%BC%80%E5%8F%91&page=1&ka=page-1"
    }
    r = requests.get(url, headers=headers, cookies=cookies)
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.text, "lxml")
    return soup


if __name__ == '__main__':
    print(bosszhipin_sipder().text)