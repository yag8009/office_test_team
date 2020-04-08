#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: models.py
# @Author: ---
# @Time: 10月 30, 2019
# ---
from django.db import models


class ModelBase(models.Model):
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        abstract = True
