from django.http import HttpResponse
from django.shortcuts import render
from .models import  User


def index(request):
    articles = User.objects.all()
    return render(request, 'news_blog/news_list.html', {'articles': articles})
def get_articles(request):
    return HttpResponse('text')
