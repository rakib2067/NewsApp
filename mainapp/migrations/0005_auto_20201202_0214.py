# Generated by Django 3.1.4 on 2020-12-02 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20201202_0032'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='detail',
            new_name='description',
        ),
    ]
