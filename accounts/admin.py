from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile

# Re-register default User and Group admin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
admin.site.register(Group)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'address', 'is_customer', 'is_admin')
    list_filter = ('is_customer', 'is_admin')
    search_fields = ('user__username', 'phone', 'address')
