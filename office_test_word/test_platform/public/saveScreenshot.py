#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

def saveName(name):
    fp = ".\\result\\image\\"
    time = saveTime()
    type = ".png"
    filename = str(fp)+str(time)+str("_")+str(name)+str(type)
    print(filename)
    return filename

def saveTime():
    #返回当前系统时间以括号中（2014-08-29-15_21_55）展示
    return time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))

def saveScreenshot(driver, name):
    image = driver.get_windows_img(saveName(name))
    return image