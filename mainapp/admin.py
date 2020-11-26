from django.contrib import admin
from .models import Category, News,Comment

admin.site.register(Category)
class NewsAdmin(admin.ModelAdmin):
    list_display= ('title', 'category', 'add_time')
class CommentAdmin(admin.ModelAdmin):
    list_display= ('news', 'email', 'comment','status')   
admin.site.register(News,NewsAdmin)
admin.site.register(Comment,CommentAdmin)

   