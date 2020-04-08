from django import forms
from captcha.fields import CaptchaField
from django.forms import widgets

from user_platform.models import base_dictionary


class UserForm(forms.Form):
    username = forms.CharField(label="用户名",max_length=128,widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="密码",max_length=256,widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(label='验证码')


class RegisterForm(forms.Form):
    username = forms.CharField(label="用户名",max_length=20,widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="密码",max_length=16,widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="确认密码",max_length=256,widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label="手机",max_length=11,widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="邮箱地址",widget=forms.EmailInput(attrs={'class': 'form-control'}))
    type = forms.ChoiceField(label='证件类型')
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['type'].choices = ((x.value, x.label) for x in base_dictionary.objects.all().filter(type="id_user"))
    identification = forms.CharField(label="证件号",max_length=30,widget=forms.TextInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(label='验证码')
