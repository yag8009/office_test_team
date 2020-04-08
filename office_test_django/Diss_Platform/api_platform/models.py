import datetime

from django.db import models

# Create your models here.
from Diss_Platform.models import ModelBase
from user_platform.models import base_dictionary


class Sign(ModelBase):
    sign_id = models.AutoField(primary_key=True, null=False)
    sign_name = models.CharField(max_length=50, verbose_name='签名')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')
    remarks = models.CharField(max_length=500, blank=True, null=True, verbose_name="备注")

    def __str__(self):
        return self.sign_name

    class Meta:
        db_table = 'api_sign'
        verbose_name = '签名信息'
        verbose_name_plural = verbose_name

class Project(ModelBase):
    prj_id = models.AutoField(primary_key=True, null=False)
    prj_name = models.CharField(max_length=100, verbose_name='项目名称')
    sign = models.ForeignKey('Sign', on_delete=models.CASCADE, verbose_name='签名信息')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')
    remarks = models.CharField(max_length=500, blank=True, null=True, verbose_name="备注")

    def __str__(self):
        return self.prj_name

    class Meta:
        db_table = 'api_project'
        verbose_name = '项目信息'
        verbose_name_plural = verbose_name

class Environment(ModelBase):
    env_id = models.AutoField(primary_key=True, null=False)
    env_name = models.CharField(max_length=50, verbose_name='环境名称')
    project = models.ForeignKey('Project', on_delete=models.CASCADE, verbose_name='所属项目')
    url = models.CharField(max_length=100, verbose_name='URL')
    private_key = models.CharField(max_length=50, verbose_name='私钥')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')
    remarks = models.CharField(max_length=500, blank=True, null=True, verbose_name="备注")

    def __str__(self):
        return self.env_name

    class Meta:
        db_table = 'api_environment'
        verbose_name = '测试环境'
        verbose_name_plural = verbose_name

class Interface(ModelBase):
    if_id = models.AutoField(primary_key=True, null=False)
    if_name = models.CharField(max_length=50, verbose_name='接口名称')
    url = models.CharField(max_length=50, verbose_name='URL')
    method = models.CharField(max_length=4, verbose_name='请求方式')
    data_type = models.CharField(max_length=4, verbose_name='数据类型')
    project = models.ForeignKey('Project', on_delete=models.CASCADE, verbose_name='所属项目')
    is_sign = models.IntegerField(verbose_name='签名')
    request_header_param = models.TextField(verbose_name='请求头部')
    request_body_param = models.TextField(verbose_name='请求数据')
    response_header_param = models.TextField(verbose_name='返回头部')
    response_body_param = models.TextField(verbose_name='返回数据')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')
    remarks = models.CharField(max_length=500, blank=True, null=True, verbose_name="备注")

    def __str__(self):
        return self.if_name

    class Meta:
        db_table = 'api_interface'
        verbose_name = '接口信息'
        verbose_name_plural = verbose_name

class Case(ModelBase):
    case_id = models.AutoField(primary_key=True, null=False)
    case_name = models.CharField(max_length=50, verbose_name='用例名称')
    project = models.ForeignKey('Project', on_delete=models.CASCADE, verbose_name='所属项目')
    content = models.TextField(verbose_name='内容')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')
    remarks = models.CharField(max_length=500, blank=True, null=True, verbose_name="备注")

    def __str__(self):
        return self.case_name

    class Meta:
        db_table = 'api_case'
        verbose_name = '用例信息'
        verbose_name_plural = verbose_name

class Plan(ModelBase):
    plan_id = models.AutoField(primary_key=True, null=False)
    plan_name = models.CharField(max_length=50, verbose_name='计划名称')
    project = models.ForeignKey('Project', on_delete=models.CASCADE, verbose_name='所属项目')
    environment = models.ForeignKey('Environment', on_delete=models.CASCADE, verbose_name='测试环境')
    content = models.TextField(verbose_name='计划内容')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')
    remarks = models.CharField(max_length=500, blank=True, null=True, verbose_name="备注")

    def __str__(self):
        return self.plan_name

    class Meta:
        db_table = 'api_plan'
        verbose_name = '计划信息'
        verbose_name_plural = verbose_name

class Report(ModelBase):
    report_id = models.AutoField(primary_key=True, null=False)
    report_name = models.CharField(max_length=255, verbose_name='计划名称')
    plan = models.ForeignKey('Plan', on_delete=models.CASCADE, verbose_name='计划名称')
    content = models.TextField(verbose_name='内容')
    case_num = models.IntegerField(null=True, verbose_name='用例')
    pass_num = models.IntegerField(null=True, verbose_name='通过')
    fail_num = models.IntegerField(null=True, verbose_name='失败')
    error_num = models.IntegerField(null=True, verbose_name='错误')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')
    remarks = models.CharField(max_length=500, blank=True, null=True, verbose_name="备注")

    def __str__(self):
        return self.report_name

    class Meta:
        db_table = 'api_report'
        verbose_name = '报告信息'
        verbose_name_plural = verbose_name