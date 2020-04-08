from django.shortcuts import render, redirect

from user_platform.forms import UserForm, RegisterForm
from user_platform.models import user_platfrom
from . import models
import hashlib


def index(request):

    return render(request, 'login/../../EasyPlatform/templates/user/index.html')


def login(request):
    if request.session.get('is_login', None):
        return redirect("/index/")
    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.user_platfrom.objects.get(username=username)
                if user.password == hash_code(password):  # 哈希值和数据库内的值进行比对
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.username
                    return redirect('/index/')
                else:
                    message = "密码不正确！"
            except BaseException:
                message = "用户不存在！"
        return render(request, 'login/../../EasyPlatform/templates/user/login.html', locals())

    login_form = UserForm()
    return render(request, 'login/../../EasyPlatform/templates/user/login.html', locals())


def register(request):
    if request.session.get('is_login', None):
        # 登录状态不允许注册。你可以修改这条原则！
        return redirect("/index/")
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            phone = register_form.cleaned_data['phone']
            email = register_form.cleaned_data['email']
            type = register_form.cleaned_data['type']
            identification = register_form.cleaned_data['identification']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = models.user_platfrom.objects.filter(
                    username=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'login/register.html', locals())
                same_email_user = models.user_platfrom.objects.filter(
                    email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'login/register.html', locals())

                # 当一切都OK的情况下，创建新用户

                password = hash_code(password1)
                # joe = models.base_dictionary.objects.get(type=type)
                new_user = user_platfrom(
                    username=username,
                    password=password,
                    phone=phone,
                    email=email,
                    type_id=int(type),
                    identification=identification)
                new_user.save()
                return redirect('/login/')  # 自动跳转到登录页面
    register_form = RegisterForm()
    return render(request, 'login/register.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        return redirect('/index/')
    request.session.flush()

    return redirect('/index/')


def hash_code(s, salt='Diss_Platform'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())  # update方法只接收bytes类型
    return h.hexdigest()
