from django.shortcuts import render
from django.http import HttpResponse
from .models import  Article
# Create your views here.
def index (request):
    return render(request, 'news_blog/news_list.html',{'articles': articles})
articles = [
    {
        'id':1,
        'title': 'First news',
        'text': 'This is the worst first article'
    },
    {
        'id':2,
        'title': 'Second news',
        'text': 'This is amazing second article'
    }]
def get_article(request, article_id):
    return render(request, 'news_blog/news_article.html', {'article': articles[article_id - 1]})