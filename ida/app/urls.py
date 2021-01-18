from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.images_list,name='images'),
    path('upload/', views.upload_image, name='upload'),
    path('resize/<slug:filename>/', views.edit_image, name='edit'),
]
