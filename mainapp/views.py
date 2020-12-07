import datetime as D  # datetime library to get time for setting cookie
import sys

from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from django.urls import path, reverse, reverse_lazy 
from django.template import RequestContext, loader
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError
from django.conf.urls.static import static


from .models import News,Category
def home(request):
    latest=News.objects.first()
    corresponding=News.objects.all()[1:4]
    categories=Category.objects.all()
    
    #Fetches the first news article in the db
    #Then fetches the next 3, setting a limit, skipping the already getched first and up to 3
    return render(request,'articles.html',{
        'latest':latest,
        'corresponding':corresponding,
        'cats':categories,
    })

def description(request, id):
    news=News.objects.get(pk=id)
    category=Category.objects.get(id=news.category.id)
    similar=News.objects.filter(category=category).exclude(id=id)
    categories=Category.objects.all()
    return render(request,'description.html',
    {
          'news':news,
          'similar':similar,
          'cats':categories,
    })

def category(request,id):
    
    category=Category.objects.get(id=id)
    news=News.objects.filter(category=category)
    categories=Category.objects.all()
    return render(request,'category.html',
    {
        'catnews':news,
        'category':category,
        'cats':categories,
    })
