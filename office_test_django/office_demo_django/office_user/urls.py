#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path

from office_user import views
app_name = "office_user"
urlpatterns = [
    # path('', views.index),
    path('index/', views.login),
    path('register/', views.register),
    path('', views.register),
    path('forgot/', views.forgot),
    path('logout/', views.logout),
]

