#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging

logger = logging.getLogger("simple_example")
logger.setLevel(logging.DEBUG)

#输出到屏幕
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
#输出到文件
fh = logging.FileHandler(r"./result/log.txt")
fh.setLevel(logging.INFO)
#设置日志格式
fomatter = logging.Formatter('%(asctime)s -%(name)s-%(levelname)s-%(module)s:%(message)s')
ch.setFormatter(fomatter)
fh.setFormatter(fomatter)
logger.addHandler(ch)
logger.addHandler(fh)

# logger.debug("debug message")
# logger.info("info message")
# logger.warning("warning message")
# logger.error("error message")
# logger.critical("critical message")