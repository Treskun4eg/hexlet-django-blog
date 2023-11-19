from django.urls import path, include
from django.contrib import admin
from hexlet_django_blog.article import views

urlpatterns = [
    path('', views.index),
]
