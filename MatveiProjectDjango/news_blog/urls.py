from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include
from . import views
from .views import articles






urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_id>/', views.get_article, name='article'),
]