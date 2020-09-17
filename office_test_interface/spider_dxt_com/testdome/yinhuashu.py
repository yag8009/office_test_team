#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : yag8009
# @FileName  : yinhuashu
# @Time    : 2020/6/22

import requests
import re
import time
import random
from lxml import etree

# 详细页面的后缀
search_list = 0

# 页码
cd = 1

headers = {
    # 填上你自己登录后的cookie
    "cookie": "",
    "referer": "https://www.zhipin.com/c101010100/?query=%E7%88%AC%E8%99%AB&page={}&ka=page-{}",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
}
headers_1 = {
    # 填上你自己登录后的详情页的cookie
    "cookie": "",
    "referer": "https://www.zhipin.com/c101010100/?query=%E7%88%AC%E8%99%AB&page=3&ka=page-3",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
}

parameters = {
    "query": "爬虫",
    "page": "2",
    "ka": "page-2"
}


# 匹配详细信息
def detailed_information(response):
    # gs(公司),cs(城市),gzyq(岗位职责),rs(招聘人数),gz(工资),name(岗位名字),detail(技能要求)
    try:
        gs = re.findall('<h3>工商信息</h3>(.*?)<div class="level-list">', response, re.S)[0].replace('<div class="name">',
                                                                                                 "").replace('</div>',
                                                                                                             "").replace(
            '\n', "").replace(' ', "")
    except:
        gs = "null"
    html = etree.HTML(response)
    try:
        cs = html.xpath('//*[@id="macin"]/div[1]/div/div/div[2]/p/text()')[0].replace("\n", "").replace(" ", "")
    except:
        cs = "null"
    try:
        yq = html.xpath('//*[@id="main"]/div[3]/div/div[2]/div[2]/div[1]/div/text()')
    except:
        yq = "null"
    rs = random.randint(1, 10)
    try:
        gz = html.xpath('//*[@id="main"]/div[1]/div/div/div[2]/div[2]/span/text()')[0].replace("\n", "").replace(" ",
                                                                                                                 "")
    except:
        gz = "null"
    try:
        name = html.xpath('//*[@id="main"]/div[1]/div/div/div[2]/div[2]/h1/text()')[0].replace("\n", "").replace(" ",
                                                                                                                 "")
    except:
        name = "null"
    if len(cs) == 0:
        cs = "null"
    if len(gz) == 0:
        cs = "null"
    if len(gz) == 0:
        cs = "null"
    if len(name) == 0:
        cs = "null"

    detail = ""
    yq = "".join(yq)
    yq = yq.replace("\n", "").replace(" ", "")
    gzyq = ""
    if len(yq) == 0:
        gzyq = "null"
        detail = "null"
    else:
        data = yq.split("：")
        if len(data) == 1:
            gzyq = data[0]
            detail = "null"
        elif len(data) == 2:
            gzyq = data[1]
            detail = "null"
        elif len(data) == 3:
            gzyq = data[1][:-4]
            detail = data[2]
        else:
            gzyq = "null"
            detail = "null"
    print(gs + "," + cs + "," + gzyq + "," + str(rs) + "," + gz + "," + name + "," + detail)
    with open("Boss直聘.txt", "a", encoding="utf-8") as file:
        file.write((gs + "," + cs + "," + gzyq + "," + str(rs) + "," + gz + "," + name + "," + detail))
        file.write("\n")


def information(urls):
    global search_list
    parameters_1 = {"ka": "search_list_" + str(search_list)}
    headers_1["referer"] = headers["referer"]
    prefix = "https://www.zhipin.com/"
    for url in urls:
        url = prefix + url
        search_list += 1
        response = requests.get(url, headers=headers_1, params=parameters_1).text
        detailed_information(response)
        time.sleep(random.randint(2, 4))


def position_url(response):
    try:
        urls = re.findall(' <a href="(/job_detail/.*?html)"', response, re.S)
        return urls
    except:
        return 0


def main():
    url = "https://www.zhipin.com/c101010100/"

    # cd使用的是全局变量
    for i in range(cd, 6):
        parameters["page"] = str(i)
        parameters["ka"] = "page-" + str(i)
        if i < 1:
            page = str(i - 1)
            headers["referer"] = headers["referer"].format(page, page)
        response = requests.get(url, headers=headers, params=parameters).text
        urls = position_url(response)
        if len(urls) == 0 and i == 5:
            print("出现异常")
            return i
        print("第", i, "页")
        time.sleep(random.randint(2, 4))
        information(urls)
    return 0


if __name__ == '__main__':
    # 写标题
    with open("Boss直聘.txt", "w", encoding="utf-8") as file:
        file.write("公司名称,工作城市,工作要求,招聘人数,工资情况,name(岗位名称),detail")
        file.write("\n")
    while True:
        result = main()
        if result == 0:
            print("完成")
            break
        else:
            cd = result
            headers["cookie"] = input("输入cookie1：")
            headers_1["cookie"] = input("输入cookie2：")
            continue