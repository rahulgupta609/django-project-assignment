# app/urls.py

from django.conf.urls import url

from assignment.github_api_usage import views

urlpatterns = [
    url(r'^$', views.profile, name='profile'),
]