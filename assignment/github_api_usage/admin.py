from django.contrib import admin
from .models import UserProfile
from django.shortcuts import render


class UserProfileAdmin(admin.ModelAdmin):
    """
        Admin for userprofile model
    """
    list_display = ('username', 'name', 'email', 'adding_date', 'company', 'image_url')
    actions = ['download_report']
    list_filter = ('adding_date', 'email',)

    def download_report(self, request, queryset):
        """
            Return a template which report No of users added to the database in a day, week and month.
             Also, how many search API calls has been made in a day, week and month.
        """
        report_data = []
        return render(request, 'userProfile/report.html', {'data': report_data})


admin.site.register(UserProfile, UserProfileAdmin)

