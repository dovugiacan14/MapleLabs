from django.urls import path 
from . import views 

urlpatterns = [
    path('show_image/', views.show_image, name= 'show_image'), 
]