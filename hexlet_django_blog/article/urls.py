from django.urls import path, include

from hexlet_django_blog.article import views

urlpatterns = [
    path('', views.index),
    path('articles/', include('hexlet_django_blog.article.urls')),
]
