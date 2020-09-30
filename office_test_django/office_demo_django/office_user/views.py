
from django.contrib.auth.hashers import make_password
from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponse

# Create your views here.


from office_user.forms import RegisterForm


def login(request):
    """ 登录页面  """
    if request.method == 'GET':        # 判断发送的请求是否是get请求
        return render(request, 'user/login.html')   # 是的话返回登陆页面
    elif request.method == 'POST':        # 判断发送的请求是否是post请求
        username = request.POST.get('username')        # 获取前端发送过来的账号
        password = request.POST.get('password')        # 获取前端发过来的密码

        #系统自带加密
        # password = make_password(password, None, 'pbkdf2_sha256')

        # 判断获取到的账号和密码与数据库比对 是否一致
        if auth.authenticate(username=username, password=password):
            # 一致则返回页面(写着登陆成功的页面)
            return HttpResponse('登陆成功')
        else:
            # 不一致则返回登陆页面, 给用户提醒说用户名或密码有误
            return render(request, 'user/login.html', {'error': '用户名或密码错误'})

def forgot(request):
    """ 密码重置  """
    return render(request, 'user/forgot.html',{})


def reset(request):
    """ 密码获取  """
    return render(request, 'user/reset.html', {})

def register(request):
    """ 注册页面  """
    if request.method == "GET":
        froms = RegisterForm()
        return render(request, "user/register.html", {'froms': froms})
    elif request.method == "POST":
        data = request.POST
        froms = RegisterForm(data)
        if froms.is_valid():
            user_obj = froms.cleaned_data
            username = user_obj.get('user_name')
            password = user_obj.get('password')
            if not User.objects.filter(username=username).exists():
                new_obj = User.objects.create_user(username=username, password=password)
                return redirect("/login/")
            else:
                # froms.add_error('user_name', '用户名已存在！')
                return render(request, "user/register.html", {'error': '用户名已存在！', 'froms': froms})
        else:
            return render(request, "user/register.html", {'froms': froms})



def logout(request):
    """ 退出  """
    auth.logout(request)
    return redirect("/login/")



