from django.contrib import admin

# Register your models here.
from user_platform.models import base_dictionary, user_platfrom


class DictionaryAdmin(admin.ModelAdmin):
    list_display = (
        'label',
        'value',
        'type',
        'description',
        'remarks',
        'create_time', 'update_time')
    search_fields = ('label',)
    list_filter = ('type',)
    ordering = ('-update_time',)


admin.site.register(base_dictionary, DictionaryAdmin)


class UserplatfromAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'email',
        'phone',
        'address',
        'type',
        'identification',
        'update_time')
    search_fields = ('username',)
    ordering = ('-update_time',)


admin.site.register(user_platfrom, UserplatfromAdmin)