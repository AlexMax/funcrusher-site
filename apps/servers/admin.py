from django.contrib import admin
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from models import PasswordPermission, Server

class ServerAdmin(admin.ModelAdmin):
    fields = ('name', 'address', 'password', 'info')
    list_display = ('name', 'address', 'password')

admin.site.register(Server, ServerAdmin)

class PasswordPermissionAdmin(admin.ModelAdmin):
    fields = ('user', 'server', 'status')
    list_display = ('created', 'requesting_user', 'server', 'status')
    list_editable = ('status',)
    list_filter = ('status', 'server__name')
    search_fields = ('user__username', 'server__name')

    # FIXME: We should be escaping the username ourselves
    def requesting_user(self, obj):
        url = reverse('admin:auth_user_change', args=(obj.user.id,))
        return '<a href="%s">%s</a>' % (url, obj.user.username)
    requesting_user.allow_tags = True
    requesting_user.admin_order_field = 'user'

admin.site.register(PasswordPermission, PasswordPermissionAdmin)
