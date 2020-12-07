from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path,include
from users import views as user_views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', include('mainapp.urls')),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)