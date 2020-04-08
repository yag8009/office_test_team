#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 继承BasePage类
from core.BasePage import BasePage


class LoginPage(BasePage):
    """
    登录页面模型
    """

    def __init__(self, driver, url):
        super(LoginPage, self).__init__(driver)
        self.iopen(url)

    def type_username(self, username):
        self.driver.type("id=>login_field", username)

    def type_password(self, password):
        self.driver.type("id=>password", password)

    def submit(self):
        self.driver.click("xpath=>//*[@id='login']/form/div[3]/input[3]")


    def test_user_login(self, username, password):
        """
        测试获取的用户名密码 是否可以登录
        """

        self.type_username(username)
        self.type_password(password)
        self.submit()
