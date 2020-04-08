#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: url.py
# @Author: ---
# @Time: 10月 16, 2019
# ---
from django.urls import include, path

from user_platform import views
app_name = "user_platform"
urlpatterns = [
    path('', views.index),
    path('index/', views.index),
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),
]