# Diss_Platform
莫明想法

## 环境
- python==3.5.2
- Django==2.1.4
- pip install pyecharts

## 创建django
* django-admin startproject Diss_Platform(项目名)
* python manage.py startapp api_platform(功能模块名)
## 修改srttings
- 修改显示中文
- LANGUAGE_CODE = 'zh-Hans'
- TIME_ZONE = 'Asia/Shanghai'

## 添加simpleui后台美化
> pip install django-simpleui

```
INSTALLED_APPS = [
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api_platform',
    'captcha',
    ...
]
```
## 图片验证码
- pip install django-simple-captcha
  
### 注册captcha
```
INSTALLED_APPS = [
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api_platform',
    'captcha',
    'user_platform',
]
```
## 前端页面下载
- 地址：https://themequarry.com/category/free