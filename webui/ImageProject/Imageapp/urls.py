from django.contrib import admin 
from django.urls import path, include 
from Imageapp.views import ImagePage
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('', ImagePage.as_view(), name= 'ImagePage')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)