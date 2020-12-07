from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path,include
from users import views as user_views

urlpatterns = [
    path('', include('mainapp.urls')),
    path('admin/', admin.site.urls),
]