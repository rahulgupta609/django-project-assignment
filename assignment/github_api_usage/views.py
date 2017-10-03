# views.py

from django.shortcuts import render, HttpResponse
from django.views import View
from .models import UserProfile
import requests


def profile(request):
    parsedData = []
    if request.method == 'POST':
        username = request.POST.get('user')
        req = requests.get('https://api.github.com/users/' + username)
        jsonList = []
        jsonList.append(req.json())
        userData = {}
        for data in jsonList:
            userData['name'] = data['name']
            userData['username'] = data['login']
            userData['image_url'] = data['avatar_url']
            userData['company'] = data['company']
            userData['email'] = data['email']
        parsedData.append(userData)
        try:
            obj = UserProfile.objects.get(username=userData['username'])
        except UserProfile.DoesNotExist:
            obj = None
        if obj is None:
            UserProfile.objects.create(username=userData['username'],
                                       image_url=userData['image_url'],
                                       name=userData['name'],
                                       company=userData['company'],
                                       email=userData['email'])
        else:
            obj.username = userData['username']
            obj.image_url = userData['image_url']
            obj.name = userData['name']
            obj.company = userData['company']
            obj.email = userData['email']
            obj.save()
    return render(request, 'userProfile/profile.html', {'data': parsedData})

