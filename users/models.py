from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    dob = models.DateField(max_length=8)

    def __str__(self):
        return self.user.username
