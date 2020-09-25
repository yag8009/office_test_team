from django import forms
from django.contrib.auth.models import User
#引入密码模块
from django.contrib.auth.hashers import make_password

class RegisterForm(forms.Form):
    user_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '用户名', 'required': True}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': '邮箱', 'required': True}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '密码', 'required': True}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '确认密码', 'required': True}))

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password and confirm_password:
            if password != confirm_password:
                raise forms.ValidationError(u'两次密码输入不一致，请重新输入')

    def save(self):
        user = User()
        user.user_name = self.cleaned_data['user_name']
        user.email = self.cleaned_data['email']
        #密码更改处
        user.password =make_password(self.cleaned_data['password']) 
        user.save()
