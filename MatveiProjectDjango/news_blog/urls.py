from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include
from . import views







urlpatterns = [
    path('', views.index, name='index'),
    path('get_articles/', views.get_articles, name='article'),
]