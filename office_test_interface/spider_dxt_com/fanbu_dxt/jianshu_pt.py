#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : yag8009
# @FileName  : jianshu_pt
# @Time    : 2020/6/23
from time import sleep

from fanbu_dxt.pyse import Pyse


def jianshu_pt():
    driver = Pyse()
    driver.max_window()
    driver.wait(60)
    # 打开网页
    driver.open("https://www.jianshu.com/sign_in")

    # 点击登录，输入用户名和密码，点提交
    driver.click('xpath=>//*[@id="sign_in"]')
    driver.type('xpath=>//*[@id="session_email_or_mobile_number"]')
    driver.type('xpath=>//*[@id="session_password"]')
    driver.click('xpath=>//*[@id="sign-in-form-submit-btn"]')
    sleep(3)

    driver.click('xpath=>/html/body/nav/div/a[2]')
    sleep(3)

    driver.click('xpath=>//*[@id="root"]/div/div[2]/div[1]/div/div/div/div[1]/span')
    driver.click('xpath=>//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/input')
    driver.type('xpath=>//*[@id="editor"]/div')
    driver.type ('xpath=>//*[@id="sign-in-form-submit-btn"]')
    driver.click('xpath=>//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/ul/li[1]/a')
    sleep(3)