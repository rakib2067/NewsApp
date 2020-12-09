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
from users.models import UserProfile
from .models import Comment
from .forms import *

from .models import News,Category

def loggedin(view):
    ''' Decorator that tests whether user is logged in '''
    def mod_view(request):
        if 'username' in request.session:
            username = request.session['username']
            try: user = UserProfile.objects.get(username=username)
            except UserProfile.DoesNotExist: raise Http404('User does not exist')
            return view(request, user)
            #This is a decorator which will check the value of username in the session
            #If the username matches a user in db, then it will return the view function, along with the current user in the session
            #Otherwise, if the user does not exist, then an error is raised
        else:
            return render(request,'not-logged-in.html',{})
    return mod_view
def home(request):
    latest=News.objects.first()
    corresponding=News.objects.all()[1:4]
    categories=Category.objects.all()
    if 'username' in request.session:
        username = request.session['username']
        try: user = UserProfile.objects.get(username=username)
        except UserProfile.DoesNotExist: raise Http404('User does not exist')
        favcats=UserProfile.favourite
        return render(request,'articles.html',{
        'latest':latest,
        'corresponding':corresponding,
        'cats':categories,
        'favcats':favcats
        })   
    #Fetches the first news article in the db
    #Then fetches the next 3, setting a limit, skipping the already getched first and up to 3
    else:
        return render(request,'articles.html',{
            'latest':latest,
            'corresponding':corresponding,
            'cats':categories,
        })

def description(request, id):
    news=News.objects.get(pk=id)
    category=Category.objects.get(id=news.category.id)
    similar=News.objects.filter(category=category).exclude(id=id)
    comments = Comment.objects.filter(news=news).order_by('-id')
    categories=Category.objects.all()
    is_liked = False
    if news.likes.filter(id=request.user.id).exists():
        is_liked = True
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            body = request.POST.get('body')
            comment = Comment.objects.create(news=news, user=request.user, body=body)
            comment.save()
    else:
        comment_form = CommentForm()

    return render(request,'description.html',
    {
          'news':news,
          'similar':similar,
          'cats':categories,
          'comments': comments,
          'comment_form': comment_form,
          'is_liked': is_liked,
          'total_likes': news.total_likes()
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
    
def like(request, pk):
    news = News.objects.get(id=pk)
    is_liked = False
    if news.likes.filter(id=request.user.id).exists():
        news.likes.remove(request.user)
        is_liked = False
    else:
        news.likes.add(request.user)
        is_liked = True
    #Like has been assigned from that user to that news object
    return HttpResponseRedirect(reverse('description', args=[str(pk)]))

