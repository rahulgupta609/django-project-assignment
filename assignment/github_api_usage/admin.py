from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'created_at', 'updated_at')


admin.site.register(UserProfile, UserProfileAdmin)

