from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.models import User
from models import Profile

class ProfileInline(admin.StackedInline):
    can_delete = False
    fields = ('location', 'contact', 'aliases', 'admin_notes')
    max_num = 1
    model = Profile

class UserAdmin(AuthUserAdmin):
    inlines = [ProfileInline]
    list_display = ('username', 'email', 'is_active', 'is_staff')

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
