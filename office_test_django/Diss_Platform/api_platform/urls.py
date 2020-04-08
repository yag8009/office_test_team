#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: urls.py
# @Author: ---
# @Time: 10月 30, 2019
# ---
from django.urls import path

from api_platform.views import *

urlpatterns = [

    path('project/', project_index),
    path('project_add/', project_add),
    path('project_update/', project_update),
    path('project_delete/', project_delete),

    path('sign/', sign_index),
    path('sign_add/', sign_add),
    path('sign_update/', sign_update),

    path('env/', env_index),
    path('env_add/', env_add),
    path('env_update/', env_update),

    path('interface/', interface_index),
    path('interface_add/', interface_add),

    path('case/', case_index),
    path('case_add/', case_add),
    path('case_run/', case_run),

    path('plan/', plan_index),
    path('plan_add/', plan_add),
    path('plan_run/', plan_run),

    path('report/', report_index),

    path('findata/', findata)
]