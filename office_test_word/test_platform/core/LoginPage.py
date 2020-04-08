#!/usr/bin/env python
# -*- coding: utf-8 -*-
#继承BasePage类
from core.BasePage import BasePage


class LoginPage(BasePage):
    """
    登录页面模型
    """
    def type_username(self, username):
        self.driver.type("id=>username", username)

    def type_password(self, password):
        self.driver.type("id=>password", password)

    def submit(self):
        self.driver.click("xpath=>//form[@id='loginForm']/input[3]")


def test_user_login(driver, username, password):
    """
    测试获取的用户名密码 是否可以登录
    """
    login_page = LoginPage(driver)
    login_page.iopen()
    login_page.type_username(username)
    login_page.type_password(password)
    login_page.submit()