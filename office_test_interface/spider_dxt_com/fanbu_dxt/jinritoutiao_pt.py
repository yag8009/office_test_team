#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : yag8009
# @FileName  : jinritoutiao_pt
# @Time    : 2020/7/2
from time import sleep

from fanbu_dxt.pyse import Pyse


def jinritoutiao_pt():
    driver = Pyse()
    driver.max_window()
    driver.wait(60)
    # 打开网页
    driver.open("https://mp.toutiao.com/auth/page/login")

    # 点击登录，输入用户名和密码，点提交
    driver.click('xpath=>//*[@id="sso_pwd_login"]/span')
    driver.type('xpath=>//*[@id="sso_container"]/div/div[1]/form/div[1]/div[2]/input',"15235577324")
    driver.type('xpath=>//*[@id="sso_container"]/div/div[1]/form/div[2]/input',"Dxt12345")
    driver.click('xpath=>//*[@id="sso_submit"]')
    sleep(2)
    driver.click('xpath=>//*[@id="sign_in"]')