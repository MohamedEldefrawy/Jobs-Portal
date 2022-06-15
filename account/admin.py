from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

User = get_user_model()

# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)


class UserAdmin(BaseUserAdmin):
    list_display = ['email', 'admin']
    list_filter = ['admin']
    fieldsets = (
        (None, {'fields': ('username', 'email')}),
        ('Developer fields',
         {'fields': ('gender', 'date_of_birth', 'tags', 'applied_job', 'allow_mail_notification', 'cv')}),
        ('Company fields', {'fields': ('address', 'history')}),
        ('Permissions', {'fields': ('admin', 'company', 'developer')}),
        ('Is Activated By Admin', {'fields': ('is_activated',)}),
    )
    ordering = ['email']
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
