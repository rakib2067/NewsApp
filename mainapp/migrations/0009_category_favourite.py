# Generated by Django 3.1.4 on 2020-12-08 00:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0008_auto_20201205_2341'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='favourite',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
