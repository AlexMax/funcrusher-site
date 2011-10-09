from django.contrib import admin
from models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'aliases', 'location')
    search_fields = ('user__username', 'aliases')

admin.site.register(Profile, ProfileAdmin)
