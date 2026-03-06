from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

admin.site.unregister(User)

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff', 'get_groups')

    def get_groups(self, obj):
        return ', '.join([g.name for g in obj.groups.all()]) or 'No group'
    get_groups.short_description = 'Groups'