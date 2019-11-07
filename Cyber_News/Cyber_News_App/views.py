from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import *


def homepage(request):
    # return HttpResponse("homepage")
    return render(request, 'Cyber_News_App/homepage_test.html')


def index(request):
    articles = Article.objects.all().order_by('article_date')
    return render(request, 'Cyber_News_App/articles.html', {'articles': articles})


def article_details(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    article.numberOfClicks += 1
    article.save()

    author = User.objects.get(pk = article.author_id_id)    # why id_id works!&?
    return render(request, 'Cyber_News_App/article_detail.html', {'article': article,
                                                                  'author': author})


def login(request):
    # return HttpResponse("user login page")
    return render(request, 'Cyber_News_App/logregpage.html')

