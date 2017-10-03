from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'email', 'company', 'image_url')


admin.site.register(UserProfile, UserProfileAdmin)

