from django.db import models
from django.contrib.auth.models import User
from users.models import UserProfile
class Category(models.Model):
    name= models.CharField(max_length=200)
    category_image= models.ImageField(upload_to='imgs')
    class Meta:
        verbose_name_plural='Categories'
    def __str__(self):
        return self.name

class News(models.Model):
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    title=models.CharField(max_length=300)
    image= models.ImageField(upload_to='imgs/')
    description=models.TextField()
    add_time=models.DateTimeField(auto_now_add=True)
    likes=models.ManyToManyField(User,related_name='article')
    class Meta:
        verbose_name_plural='News'
    def __str__(self):
        return self.title

class Comment(models.Model):
    news=models.ForeignKey(News, on_delete=models.CASCADE) 
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    comment=models.TextField()
    status=models.BooleanField(default=False)
    def __str__(self):
        return self.comment