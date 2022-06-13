from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from .forms import UserAdminCreationForm, UserAdminChangeForm

User = get_user_model()

# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ['email', 'admin']
    list_filter = ['admin']
    fieldsets = (
        (None, {'fields': ('username','email', 'password')}),
        ('Developer fields', {'fields': ('gender', 'date_of_birth', 'tags', 'applied_job', 'allow_mail_notification')}),
        ('Company fields', {'fields': ('address', 'history')}),
        ('Permissions', {'fields': ('admin', 'company', 'developer')}),
    )
    ordering = ['email']
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
