from django.contrib import admin

# Register your models here.
from office_user.models import UserProfile
# 页面标题
admin.site.site_title="后台管理系统"
# 登录页导航条和首页导航条标题
admin.site.site_header="后台管理"

# class UserProfileAdmin(admin.ModelAdmin):
#     list_display = ('user', 'org', 'telephone')  # 指定要显示的字段
    

# admin.site.register(UserProfile, UserProfileAdmin)
