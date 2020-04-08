#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: urls.py
# @Author: ---
# @Time: 11月 04, 2019
# ---
from django.urls import path

from UserSite import views
app_name = "UserSite"
urlpatterns = [
    # path('', views.index),
    path('index/', views.login),
    path('register/', views.register),
    path('', views.login),
    path('forgot/', views.forgot),
    path('logout/', views.logout),
]