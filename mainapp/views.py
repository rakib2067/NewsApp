import datetime as D  # datetime library to get time for setting cookie
import sys

from django.shortcuts import render
from django.utils import timezone
from django.urls import path    
from django.template import RequestContext, loader

from django.contrib.auth.hashers import make_password
from django.db import IntegrityError
from django.conf.urls.static import static

from .models import News
def home(request):
    latest=News.objects.first()
    corresponding=News.objects.all()[1:4]
    #Fetches the first news article in the db
    #Then fetches the next 3, setting a limit, skipping the already getched first and up to 3
    return render(request,'home.html',{
        'latest':latest,
        'corresponding':corresponding
    })
