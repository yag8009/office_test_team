from django.contrib import admin

# Register your models here.
from api_platform.models import *

admin.site.site_title = "后台管理系统"
admin.site.site_header = "后台管理"

class SignAdmin(admin.ModelAdmin):
    list_display = ('sign_id', 'sign_name', 'update_time')
    search_fields = ('sign_name',)
    ordering = ('-update_time',)

admin.site.register(Sign, SignAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('prj_id', 'prj_name', 'sign', 'update_time')
    search_fields = ('prj_name',)
    ordering = ('-update_time',)

admin.site.register(Project, ProjectAdmin)

class EnvironmentAdmin(admin.ModelAdmin):
    list_display = ('env_id', 'env_name', 'project', 'url', 'private_key', 'update_time')
    search_fields = ('env_name',)
    ordering = ('-update_time',)

admin.site.register(Environment, EnvironmentAdmin)

class InterfaceAdmin(admin.ModelAdmin):
    list_display = ('if_id', 'if_name', 'url', 'method', 'data_type', 'project', 'is_sign', 'request_header_param', 'request_body_param', 'response_header_param', 'response_body_param', 'update_time')
    search_fields = ('if_name',)
    ordering = ('-update_time',)

admin.site.register(Interface, InterfaceAdmin)

class CaseAdmin(admin.ModelAdmin):
    list_display = ('case_id', 'case_name', 'project', 'content', 'update_time')
    search_fields = ('case_name',)
    ordering = ('-update_time',)

admin.site.register(Case, CaseAdmin)

class PlanAdmin(admin.ModelAdmin):
    list_display = ('plan_id', 'plan_name', 'project', 'environment', 'content', 'update_time')
    search_fields = ('plan_name',)
    ordering = ('-update_time',)

admin.site.register(Plan, PlanAdmin)

class ReportAdmin(admin.ModelAdmin):
    list_display = ('report_id', 'report_name', 'plan', 'content', 'case_num', 'pass_num', 'fail_num', 'error_num', 'update_time')
    search_fields = ('report_name',)
    ordering = ('-update_time',)

admin.site.register(Report, ReportAdmin)
