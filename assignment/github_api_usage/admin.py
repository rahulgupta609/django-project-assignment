from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    """
        Admin for userprofile model
    """
    list_display = ('username', 'name', 'email', 'adding_date', 'company', 'image_url')
    list_filter = ('adding_date', 'email',)


admin.site.register(UserProfile, UserProfileAdmin)

