#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path

from office_user import views
app_name = "office_user"
urlpatterns = [
    # path('', views.index),
    path(r'login/', views.login, name='login'),
    path(r'register/', views.register),
    path('', views.register),
    path(r'forgot/', views.forgot),
    path(r'logout/', views.logout),
    path(r'reset/', views.reset),
]

