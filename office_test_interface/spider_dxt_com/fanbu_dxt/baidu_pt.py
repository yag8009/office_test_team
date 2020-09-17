#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : yag8009
# @FileName  : baidu_pt
# @Time    : 2020/6/13
from time import sleep

from fubu_dxt.pyse import Pyse
from fubu_dxt.read_word import read_word


def baidu_pt():
    driver = Pyse()
    driver.max_window()
    driver.wait(60)

    # 打开网页
    driver.open("https://tieba.baidu.com/f?ie=utf-8&kw=%E8%BF%9B%E9%94%80%E5%AD%98")

    # 点击登录，输入用户名和密码，点提交
    driver.click('xpath=>//*[@id="com_userbar"]/ul/li[4]/div/a')
    driver.click('xpath=>//*[@id="TANGRAM__PSP_12__footerULoginBtn"]')
    driver.type('xpath=>//*[@id="TANGRAM__PSP_12__userName"]', "15101014687")
    driver.type('xpath=>//*[@id="TANGRAM__PSP_12__password"]', "you4687")
    driver.click('xpath=>//*[@id="TANGRAM__PSP_12__submit"]')
    sleep(2)

    # 写文章
    driver.js("window.scrollTo(0,document.body.scrollHeight);")
    driver.click('xpath=>/html/body/ul/li[2]/a')
    doc = read_word('word_data//夜市摆地摊用什么收银软件和管理库存好.docx')
    driver.type('xpath=>//*[@id="tb_rich_poster"]/div[3]/div[1]/div[2]/input', doc[0])
    driver.type('xpath=>//*[@id="ueditor_replace"]', doc)
    driver.click('xpath=>//*[@id="tb_rich_poster"]/div[3]/div[5]/div/button[1]')
    sleep(20)


if __name__ == '__main__':
    baidu_pt()
