#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : yag8009
# @FileName  : timeStamp
# @Time    : 2020/2/11
import time
import datetime


# 获取时间戳
def TimeStamp(len=1):
    timestamp = (time.time() * len)
    print(timestamp)
    return timestamp


# 获取本地时间
def LocalTime():
    localTime = time.localtime(time.time())
    print(localTime)
    return localTime


# 本地时间
def FormatTime(whattime):
    FormatTimeStrs = time.strftime("%Y-%m-%d %H:%M:%S", whattime)
    print(FormatTimeStrs)
    return FormatTimeStrs


# 计算时间差
day1 = datetime.datetime(2018, 5, 16)
day2 = datetime.datetime(2018, 4, 16)

# 计算指定时间的间隔
print((day1 - day2).days)


# 获取当前时间
# 当前指定时间
# 获取当前年份
def CurrentTime():
    nowTime = datetime.datetime.now()
    print("nowTime: ", nowTime)
    print(nowTime.year)
    print(nowTime.day)
    print(nowTime.month)
    print(nowTime.hour)
    print(nowTime.minute)
    print(nowTime.second)
    return nowTime

# 当前时间往前推29天计算日期,也就是近30天的其实范围
# beforeTime = nowTime - datetime.timedelta(days=29)

# 往后推就使用 + 号，当然还可以使用 hours（小时） 、minutes(分钟)、seconds(秒）等单位运算。

# print("beforeTime: ",beforeTime)

# 结果输出

# 1526451775.666749
# time.struct_time(tm_year=2018, tm_mon=5, tm_mday=16, tm_hour=14, tm_min=22, tm_sec=55, tm_wday=2, tm_yday=136, tm_isdst=0)
# 2018-05-16 14:22:55
# 30
# nowTime:  2018-05-16 14:22:55.670309
# beforeTime:  2018-04-17 14:22:55.670309
