#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging


def get_log(logFilename='logging.log'):

    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s 测试日志 %(filename)s[line:%(lineno)d]-%(levelname)s: %(message)s',
        datefmt='%Y-%m-%d %A %H:%M:%S',
        filename="../Result/" + logFilename,
        filemode='w')

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s 测试日志 %(filename)s[line:%(lineno)d]-%(levelname)s: %(message)s')
    console.setFormatter(formatter)

    logging.getLogger().addHandler(console)
    return logging


if __name__ == "__main__":
    pass
    # get_log()
	# logging.debug('logger debug message')
    # logging.info('logger info message')
    # logging.warning('logger warning message')
    # logging.error('logger error message')
    # logging.critical('logger critical message')


