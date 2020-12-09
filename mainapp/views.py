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
from django.contrib.auth.decorators import login_required
from .models import News,Category


@login_required
def home(request):
    latest=News.objects.first()
    corresponding=News.objects.all()[1:4]
    #We have fetched the latest article in the news object
    #Then we fetcjed the next 3 latest articles stored in corresponding
    categories=Category.objects.all()
    #This is used for the dropdown in nac
    x=request.user.userprofile.favourite.all()
    #Used to filter the users articles
    return render(request,'articles.html',{
        'latest':latest,
        'corresponding':corresponding,
        'cats':categories,
        'favcats':x
 
    })


def description(request, id):
    news=News.objects.get(pk=id)
    category=Category.objects.get(id=news.category.id)
    similar=News.objects.filter(category=category).exclude(id=id)
    #Used to filter articles to those similar to the current cateogry
    comments = Comment.objects.filter(news=news, reply=None).order_by('-id')
    #Used to order comments
    categories=Category.objects.all()
    is_liked = False
    if news.likes.filter(id=request.user.id).exists():
        is_liked = True
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            body = request.POST.get('body')
            reply_id = request.POST.get('comment_id')
            comment_qs= None
            if reply_id:
                comment_qs = Comment.objects.get(id=reply_id)
            comment = Comment.objects.create(news=news, user=request.user, body=body, reply=comment_qs)
            comment.save()
            #Saves a comment in the db
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
    

