from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from mainapp.models import Category
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg',upload_to='profile_pics')
    favourite=models.ManyToManyField(Category)
    dob = models.DateField(max_length=8)

    def __str__(self):
        return self.user.username
