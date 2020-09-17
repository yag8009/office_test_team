#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : yag8009
# @FileName  : baidu_spider_login
# @Time    : 2020/7/2
import requests
from bs4 import BeautifulSoup as BS
from spider_dxt_BeautifulSoup.header_spider import headers


def baidu_login():
    home_url = "https://www.baidu.com/"
    login_url = "https://passport.baidu.com/v2/api/?login"
    Cookies = {
        "Cookies": "BIDUPSID=E99B17E06D3A0F63FEE6E14E5F21F445; PSTM=1593684249; BAIDUID=CB75C7603DAD55C3B011D638B700FE74:FG=1; HOSUPPORT=1; UBI=fi_PncwhpxZ%7ETaJc0J-lJxrI-gtTjdPAEWftGW9ztYDBU1JJXUo7NBE9Q2k5uf8oQQ%7EV60KqyryzH0CvCaN; HISTORY_BFESS=dedb389a45ee9f68cae29c93b731fe2d7b51c25895eeaca001de6e43954c704adb45f20738; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; USERNAMETYPE=2; SAVEUSERID=060695f4291137680119a035d8590ee7cf8dc4; HISTORY=dedb70cc11e69e6ac592959dbc3db1606f12894294e9a6d001da6b5dce1b254adb45f20738; logTraceID=984cd3803f549e99acbf3aea3282f62fab78ac161a95b3ebb8; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=2; H_PS_PSSID=1444_31669_32141_32139_31254_32046_32230_31322_32110_26350_31639; pplogid=9467HwqtGWvfBgxWoqcxPtzkTctmRe%2FuB0ijrHo2fLjbe4lEYCMHgDYD8QuYXyJjPsCRUFC7ue7j0%2FuwXBeZX0i%2B%2FvP%2B8J23HtXW2iftrLeZJcU%3D",
    }

    headers.update(Cookies)
    print(headers)
    re = requests.get(home_url, headers=headers)
    # print(re.text)
    # 保存cookies信息，以备下次直接访问首页
    # session.cookies.save()
    # 获取首页天气信息
    print(BS(re.text, 'lxml'))


if __name__ == '__main__':
    baidu_login()
