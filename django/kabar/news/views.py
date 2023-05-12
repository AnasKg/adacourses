from django.shortcuts import render
from news.models import News
from django.http import HttpResponse

# Create your views here.

def index(request):
    news = News.objects.all()
    context = {
        'news': news
    }
    return render(request, 'news/news-list.html', context=context)