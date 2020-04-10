#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: urls.py
# @Author: ---
# @Time: 11月 04, 2019
# ---
from django.urls import path

from office_user import views
app_name = "office_user"
urlpatterns = [
    # path('', views.index),
    path('index/', views.login),
    path('register/', views.register),
    path('', views.login),
    path('forgot/', views.forgot),
    path('logout/', views.logout),
]