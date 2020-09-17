#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : yag8009
# @FileName  : proxy_IP
# @Time    : 2020/7/2
import random

proxy = {
    "http": "http://52.187.162.198:3128",
    "https": "https://52.187.162.198:3128",
    "http": "http://10.10.1.10:3128",
    "https": "https://10.10.1.10:1080",
    "http": "http://10.20.3.10:7071",
    "https": "https://10.20.3.10:7071",
    "http": "http://202.134.202.226:80",
    "https": "https://202.134.202.226:80",
    "http": "http://39.137.2.246:8080",
    "https": "https://39.137.2.246:8080",
    "http": "http://140.227.77.174:3128",
    "https": "https://140.227.77.174:3128",
    "http": "http://202.171.47.254:3128",
    "https": "https://202.171.47.254:3128",
    "http": "http://103.42.213.177:8080",
    "https": "https://103.42.213.177:8080",
    "http": "http://95.137.240.3:35632",
    "https": "https://95.137.240.3:35632",
    "http": "http://117.191.11.74:8080",
    "https": "https://117.191.11.74:8080",
    "http": "http://117.85.105.170:808",
    "https": "https://117.85.105.170:808",
    "http": "http://10.20.3.10:7071",
    "https": "https://10.20.3.10:7071",
    "http": "http://113.117.109.236:4537",
    "https": "https://113.117.109.236:4537",
    "http": "http://14.118.252.64:6666",
    "https": "https://114.99.30.126:18118",
    "http": "http://121.228.8.93:8118",
    "https": "https://121.228.8.93:8118",
    "http": "http://113.117.109.236:4537",
    "https": "https://113.117.109.236:4537",
    "http": "http://163.125.114.117:8118",
    "http": "http://183.129.244.16:11063",
    "http": "http://219.159.38.199:56210",
    "https": "https://163.125.114.117:8118",
    "https": "https://183.129.244.16:11063",
    "https": "https://219.159.38.199:56210",
    "https": "https://58.220.95.30:10174",
    "http": "http://58.220.95.30:10174"
}

proxyip = random.choice(proxy)