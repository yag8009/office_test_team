
from django.db import models

class UserProfile(models.Model):
    gender = (
        ('male', '男'),
        ('female', '女'),
    )

    username = models.CharField(max_length=128,unique=True,verbose_name="用户昵称")
    password = models.CharField(max_length=256,verbose_name="密码")
    user = models.CharField(max_length=14,verbose_name="用户名称")
    telephone = models.CharField(max_length=11,db_index=True,unique=True,verbose_name="手机号")
    id_card = models.CharField(max_length=18,db_index=True,blank=True,unique=True,verbose_name="身份证")
    sex = models.CharField(max_length=32,choices=gender,default='男')
    email = models.EmailField(max_length=50,blank=True,unique=True,verbose_name="电子邮件")
    is_active = models.BooleanField(max_length=1,verbose_name="活跃用户")
    is_staff = models.BooleanField(max_length=1,verbose_name="关闭用户")
    date_joined = models.DateTimeField(auto_now_add=True,verbose_name="加入日期")
    mod_date = models.DateTimeField(auto_now=True,verbose_name="修改日期")

    class Meta:
        verbose_name = '用户配置'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.__str__()

