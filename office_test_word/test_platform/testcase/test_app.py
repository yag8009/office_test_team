# coding=utf-8
import os
import random

from appium import webdriver
import time

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '6.0.1',
    'deviceName': '127.0.0.1:7555',
    'appPackage': 'com.tencent.mm',
    'appActivity': '.ui.LauncherUI',
    'automationName': 'Uiautomator2',
    'noReset': True,
    'chromeOptions': {'androidProcess': 'com.tencent.mm:tools'}
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# 启动微信
print("启动微信 ...")
driver.implicitly_wait(50)

time.sleep(10)
print("查找捷易保修 ...")
els = "className(\"android.view.View\").text(\"捷易保修\")"
driver.find_element_by_android_uiautomator(els).click()

# 公众号内 - 点击左下键盘 - 输入框 - 发送按钮
time.sleep(2)
print("点击左下键盘 ...")
driver.find_element_by_xpath("//android.widget.ImageView[@content-desc=\"消息\"]").click()

time.sleep(2)
print("点击输入框 ...")
el1 = driver.find_element_by_id("com.tencent.mm:id/aqe")
el1.clear()
time.sleep(2)
el1.send_keys("http://weixin.qq.com/q/02StlrNGAMdNC1P1_iNtcy")


time.sleep(2)
print("点击发送 ...")
el2 = driver.find_element_by_id("com.tencent.mm:id/aql")
el2.click()

# 公众号内 - 点击url - 点击跳转页面X
time.sleep(2)
print("点击URL ...")
adb1 = 'adb shell input tap 650 1260'
os.system(adb1)

time.sleep(10)
print("点击关闭 ...")
el1 = driver.find_element_by_accessibility_id("返回")
el1.click()

time.sleep(10)
print("点击立即购买 ...")
adb2 = 'adb shell input tap 150 1250'
os.system(adb2)

time.sleep(10)
el12 = driver.find_element_by_xpath("//android.widget.FrameLayout[@content-desc='containerFrameLayout']/android.widget.FrameLayout/android.webkit.WebView")
el12.click()
print(driver.contexts)

# driver.find_element_by_xpath("//android.widget.EditText[@content-desc=\"请输入手机号\"]").clear()
# print(driver.window_handles)
# print("输入手机 ...")
# time.sleep(5)
# num = random.randint(1000000, 9999999)
# phone = "151" + str(num)

# time.sleep(5)
# print("输入信息：" + phone)
# adb5 = 'adb shell input tap 370 920'
# os.system(adb5)

# time.sleep(2)
# adb5 = 'adb shell input tap 170 1052'
# os.system(adb5)

time.sleep(5)
print("获取验证码 ...")
adb5 = 'adb shell input tap 610 1052'
os.system(adb5)

time.sleep(5)
print("提交申请 ...")
adb5 = 'adb shell input tap 450 1245'
os.system(adb5)

time.sleep(5)
assdata = driver.find_element_by_id("android:id/text1").text
print("获取信息：" + assdata) # 和德保修
driver.quit()
