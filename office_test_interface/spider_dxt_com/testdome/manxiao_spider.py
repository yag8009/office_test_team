#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : yag8009
# @FileName  : manxiao_spider
# @Time    : 2020/7/15
import os
import random
import re
from time import sleep

from bs4 import BeautifulSoup
import requests

user_agent = [
    "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1 Fennec/7.0a1",
    "JUC (Linux; U; 2.3.7; zh-cn; MB200; 320*480) UCWEB7.9.3.103/139/999",
    "Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/1A542a Safari/419.3",
    "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_0 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8A293 Safari/6531.22.7",
    "Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10",
    "Opera/12.02 (Android 4.1; Linux; Opera Mobi/ADR-1111101157; U; en-US) Presto/2.9.201 Version/12.02",
    "Mozilla/5.0 (iPhone; U; CPU like Mac OS X; en) AppleWebKit/420+ (KHTML, like Gecko) Version/3.0 Mobile/1A543 Safari/419.3",
    "Mozilla/5.0 (iPhone; U; CPU iPhone OS 5_1_1 like Mac OS X; en) AppleWebKit/534.46.0 (KHTML, like Gecko) CriOS/19.0.1084.60 Mobile/9B206 Safari/7534.48.3",
    "Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19",
    "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Mobile Safari/537.36"
]
header = {
    'User-Agent': random.choice(user_agent),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Host": "www.manxiaosi.com",
}


# 首页列表
def login_booklist(page):
    url = "http://www.manxiaosi.com/booklist"
    payload = {
        "tag": "全部",
        "area": "-1",
        "end": "1",
        "page": page
    }
    code = 0
    while code != 200:
        try:
            res = requests.get(url=url, params=payload, headers=header, timeout=(5, 10))
            code = int(res.status_code)
            print("进入列表页面...", code)
            return res.text
        except Exception as err:
            print("错误信息：{}".format(err))
            print("重新启动列表页面...")
            code = 0
            sleep(random.randint(60, 180))


# 介绍页面
def book_list(base_url):
    url = "http://www.manxiaosi.com/{}".format(base_url)
    code = 0
    while code != 200:
        try:
            res = requests.get(url=url, headers=header, timeout=(3, 10))
            code = int(res.status_code)
            print("进入介绍页面...", code)
            return res.text
        except Exception as err:
            print("错误信息：{}".format(err))
            print("重新启动介绍页面...")
            code = 0
            sleep(random.randint(60, 180))


# 图片列表
def img_list(base_url):
    url = "http://www.manxiaosi.com/{}".format(base_url)
    code = 0
    while code != 200:
        try:
            res = requests.get(url=url, headers=header, timeout=(3, 10))
            code = int(res.status_code)
            print("进入图片页面...", code)
            return res.text
        except Exception as err:
            print("错误信息：{}".format(err))
            print("重新启动图片页面...")
            code = 0
            sleep(random.randint(60, 180))


# 下载
def upload_list(base_url, firstname, secname):
    print("开始下载...")
    code = 0
    while code != 200:
        try:
            uploadres = requests.get(url=base_url, headers=header, timeout=(3, 10))
            code = int(uploadres.status_code)
            path = 'C:\\Users\\admin\\Downloads\\'
            title = firstname
            huashu = secname
            one_path = os.path.join(path, title)
            new_path = os.path.join(one_path, huashu)
            if not os.path.isdir(new_path):
                os.makedirs(new_path)
            imgname = base_url[-10:]

            with open(new_path + imgname, 'wb') as file:
                file.write(uploadres.content)
                file.close()
            print(secname + imgname, "下载完成！！！")
        except Exception as err:
            print("错误信息：{}".format(err))
            code = 0
            print("重新开始下载...")
            sleep(random.randint(60, 180))


def run(errorlist):
    # 图书列表
    for i in range(1, 999):
        sleep(random.randint(5, 15))
        login = login_booklist(i)
        soup = BeautifulSoup(login, features="lxml")
        booklists = soup.findAll('p', attrs={"class": "manga-list-2-title"})  # p class="manga-list-2-title"
        re_data = re.compile('<a href="(.*)">')
        booklist = re_data.findall(str(booklists))

        # 图书内容
        for x in booklist:
            sleep(random.randint(5, 15))
            book_nr = book_list(x)
            book_gz = BeautifulSoup(book_nr, features="lxml")
            titles = re.compile('<title>(.+?)韩国漫画无遮挡免费在线阅读_')
            booknames = ''.join(titles.findall(str(book_gz)))
            bookname = re.sub('\W+', '', str(booknames)).replace("_", '')  # 只要字符串中的中文，字母，数字
            errorlists = re.sub('\W+', '', str(errorlist)).replace("_", '')  # 只要字符串中的中文，字母，数字
            if bookname in errorlists:
                print("跳过{}".format(booknames))
                continue
            else:
                book_lists = book_gz.findAll('ul')
                re_book = re.compile('<a class="chapteritem" href="(.*)" title')
                booknrlist = re_book.findall(str(book_lists))

                # 图书页面信息
                ig = 0
                for y in booknrlist:
                    sleep(random.randint(5, 15))
                    img_url = img_list(y)
                    soup = BeautifulSoup(img_url, features="lxml")
                    imgsoup = soup.findAll('div')
                    imgtu = re.compile('<img class="lazy" data-original="(.*)"')
                    imgurl = imgtu.findall(str(imgsoup))
                    findnamere = re.compile('<meta content="(.*)" name="Description"')
                    findnames = soup.findAll('head')
                    findnamestr = findnamere.findall(str(findnames))
                    re_secname = findnamestr[0][-5:]
                    try:
                        num = int("".join(re.findall("\d+", re_secname)))
                        secname = "第%d話" % num
                        ig = num
                    except Exception as err:
                        print("错误信息：{}".format(err))
                        secname = "第%d話" % (ig + 1)

                    for ji in imgurl:
                        sleep(random.randint(5, 15))
                        upload_list(ji, bookname, secname)


if __name__ == '__main__':
    errorlist = ["絕倫公公的人妻調教", "27歲穿制服愛愛!", "H書大冒險", "是說讓我用身體賠償嗎…？",
                 "正在插入的事…會被大家發現的！", "扭曲的復仇式性愛", "絕倫扭蛋遊戲", "性溢房屋",
                 "奴家思想", "我的M屬性學姐", "療育女孩(完結)", "公寓啪啪趴", "捕獵母豬(完結)",
                 "猜不透的心", "軍人的誘惑", "我要睡你的女人", "叢林愛愛法則", "你劈腿了嗎?", "騙局",
                 "同居捉迷藏", "神秘貝殼島", "哪裡壞壞(完結)", "教練教教我(完結)", "啪啪啪調教所",
				 "凌辱販賣機", "紅杏出牆", "10億風騷老闆娘", "Revenge（复仇无删减）",
				 "湘亞積極追求攻勢","同居完結","小野貓馴服手冊","人家說的你都做吼","老婆回來了",
				 "今天的老公完結","新生淫亂日記","我的色色夜說","覺醒完結","感性變態完結"]
    run(errorlist)
