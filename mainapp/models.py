from django.db import models
from django.contrib.auth.models import User

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
    def total_likes(self):
        return self.likes.count()

class Comment(models.Model):
    news=models.ForeignKey(News, related_name="comments",on_delete=models.CASCADE)
    user=models.ForeignKey(User, related_name="comments",on_delete=models.CASCADE)  
    body=models.TextField()
    reply = models.ForeignKey('Comment', null=True, related_name="replies", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '{}-{}'.format(self.news.title, str(self.user.username))

    