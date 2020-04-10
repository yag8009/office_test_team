from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect


def login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            request.session['is_active'] = user.is_active
            request.session['user'] = username
            return render(request, 'user/home.html', locals())
        else:
            return render(request, 'user/index.html', {'error': '* 请正确填写用户名和密码！'})
    return render(request, 'user/index.html', locals())


def reset(request):
    user = request.user
    err_msg = ''
    if request.method == 'GET':
        old_password = request.GET.get('old_password', '')
        new_password = request.GET.get('new_password', '')
        repeat_password = request.GET.get('repeat_password', '')
        # 检查旧密码是否正确
        if user.check_password(old_password):
            if not new_password:
                err_msg = '新密码不能为空'
            elif new_password != repeat_password:
                err_msg = '两次密码不一致'
            else:
                user.set_password(new_password)
            user.save()
            return redirect("/home/")
        else:
            err_msg = '原密码输入错误'
            content = {'err_msg': err_msg, }
            return render(request, 'user/forgot.html', content)


def forgot(request):
    return


def register(request):
    msg = ''
    if request.session.get('is_active', None):
        # 登录状态不允许注册。你可以修改这条原则！
        return render(request, 'user/home.html')
    # 内置注册普通 用户
    if request.method == "GET":
        username = request.GET.get('username')
        password = request.GET.get('password')
        if username is not User.objects.filter(username=username):
            User.objects.create_user(username=username, password=password)
            msg = "注册成功"
            return redirect('/home/', msg)
        else:
            msg = "用户名已存在"
            return redirect('/register/', msg)
    else:
        return redirect('/register/')


def logout(request):
    auth.logout(request)
    return redirect("/index/")
