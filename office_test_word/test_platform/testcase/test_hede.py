#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import random
import time
import unittest
import xlrd
from appium import webdriver
from public import saveScreenshot
from public.log import logger


class HeDe(unittest.TestCase):
    def setUp(self):
        desired_caps = {
            'platformName': 'Android',
            'deviceName': '127.0.0.1:7555',
            'platformVersion': '6.0.1',
            'appPackage': 'com.tencent.mm',
            'appActivity': 'com.tencent.mm.ui.LauncherUI',
            "automationName": "Uiautomator2",
            'noReset': True,
            'chromeOptions': {'androidProcess': 'com.tencent.mm'}
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(50)

    def action_login(self, case_id='case_0000', case_summary=u'正确验证', base_url=u'18611688269'):
        driver = self.driver
        logger.info("测试开始...")
        logger.info(u"======== 【" + case_id + u"】" + case_summary + u" ========")
        # 启动微信
        logger.info("启动微信 ...")
        driver.implicitly_wait(50)

        time.sleep(20)
        logger.info("查找捷易保修 ...")
        els = "className(\"android.view.View\").text(\"捷易保修\")"
        driver.find_element_by_android_uiautomator(els).click()

        # 公众号内 - 点击左下键盘 - 输入框 - 发送按钮
        time.sleep(2)
        logger.info("点击左下键盘 ...")
        driver.find_element_by_xpath("//android.widget.ImageView[@content-desc=\"消息\"]").click()

        time.sleep(2)
        logger.info("点击输入框 ...")
        el1 = driver.find_element_by_id("com.tencent.mm:id/aqe")
        el1.clear()
        time.sleep(2)
        el1.send_keys(base_url)

        time.sleep(2)
        logger.info("点击发送 ...")
        el2 = driver.find_element_by_id("com.tencent.mm:id/aql")
        el2.click()

        # 公众号内 - 点击url - 点击跳转页面X
        time.sleep(2)
        logger.info("点击URL ...")
        adb1 = 'adb shell input tap 650 1260'
        os.system(adb1)

        time.sleep(10)
        logger.info("点击关闭 ...")
        el1 = driver.find_element_by_accessibility_id("返回")
        el1.click()

        time.sleep(10)
        logger.info("点击立即购买 ...")
        adb2 = 'adb shell input tap 150 1250'
        os.system(adb2)

        time.sleep(10)
        el12 = driver.find_element_by_xpath(
            "//android.widget.FrameLayout[@content-desc='containerFrameLayout']/android.widget.FrameLayout/android.webkit.WebView")
        el12.click()
        logger.info(driver.contexts)

        time.sleep(5)
        logger.info("获取验证码 ...")
        adb5 = 'adb shell input tap 610 1052'
        os.system(adb5)

        time.sleep(5)
        logger.info("提交申请 ...")
        adb5 = 'adb shell input tap 450 1245'
        os.system(adb5)

        time.sleep(5)
        self.assdata = driver.find_element_by_id("android:id/text1").text
        logger.info("获取信息：" + self.assdata)  # 和德保修

        time.sleep(2)
        # saveScreenshot.saveScreenshot(driver, u"-_-!")
        try:
            assert self.assdata == "和德保修"
            logger.info(u"成功")
        except:
            logger.info(u"失败")

    @staticmethod
    def getTestFunc(case_id, case_summary, base_url):
        def func(self):
            self.action_login(case_id, case_summary, base_url)
            time.sleep(20)
        return func

    def tearDown(self):
        self.driver.quit()


def __generateTestCases():
    data = xlrd.open_workbook(r"./data/hede_data.xls")
    # 通过索引顺序获取Excel表
    table = data.sheets()[0]
    for args in range(1, table.nrows):
        txt = table.row_values(args)
        setattr(HeDe, 'test_login_%s' % txt[1], HeDe.getTestFunc(*txt))


__generateTestCases()
if __name__ == '__main__':
    unittest.TextTestRunner.run()
