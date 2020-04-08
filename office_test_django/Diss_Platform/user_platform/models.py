from django.db import models

# Create your models here.
from Diss_Platform.models import ModelBase


class base_dictionary(ModelBase):
    label = models.CharField(max_length=150, unique=True, verbose_name="标签")
    value = models.CharField(max_length=150, unique=True, verbose_name="键值")
    type = models.CharField(max_length=150, verbose_name="类型")
    description = models.CharField(max_length=300,blank=True,null=True,verbose_name="描述")
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')
    remarks = models.CharField(max_length=500, blank=True, null=True, verbose_name="备注")

    def __str__(self):
        return self.label

    class Meta:
        db_table = "base_dictionary"
        verbose_name = "字典"
        verbose_name_plural = verbose_name

class user_platfrom(ModelBase):
    username = models.CharField(max_length=20, verbose_name="用户名")
    password = models.CharField(max_length=200, verbose_name="密码")
    phone = models.CharField(max_length=11, verbose_name="手机")
    email = models.EmailField(max_length=50, blank=True, null=True, verbose_name="邮箱")
    address = models.CharField(max_length=300, blank=True, null=True, verbose_name="地址")
    type = models.ForeignKey(to="base_dictionary",blank=True, null=True,on_delete=models.DO_NOTHING,verbose_name="证件类型")
    identification = models.CharField(max_length=50, blank=True, null=True, verbose_name="证件号")
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')
    remarks = models.CharField(max_length=500, blank=True, null=True, verbose_name="备注")


    def __str__(self):
        return self.username

    class Meta:
        db_table = "user_platfrom"
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name