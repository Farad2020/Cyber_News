from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import *


# Create your views here.
def index(request):
    return HttpResponse("emptyness")


def homepage(request):
    # return HttpResponse("homepage")
    return render(request, 'Cyber_News_App/homepage_test.html')


def articles_page(request):
    # return HttpResponse("homepage")
    articles = Article.objects.all().order_by('article_date')
    return render(request, 'Cyber_News_App/articles.html', {'articles': articles})


def articles_details(request, slug):
    # return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request, 'Cyber_News_App/article_detail.html', {'article': article})


def login(request):
    # return HttpResponse("user login page")
    return render(request, 'Cyber_News_App/logregpage.html')


'''
    return render(request, "Cyber_News_App/index.html", {'latest_articles': latest_articles})
    '''
'''return HttpResponse(
        "I hope this will work"
    )'''
'''
def article(request, article_id):
    """Using get_object_or_404() shortcut to return PNF 404"""
    art = get_object_or_404(Article, pk=article_id)
    print(type(art), art)
    return render(request, "myFirstApp/article.html", {"article":art})

    # try:
    #     article = Article.objects.get(pk=article_id)
    # except:
        # """using Http404() to raise an exception of page not found"""
        # raise Http404("No such article by id %i" %article_id)

        # """Using simple HttpResponse to say that there is no such article by given id"""
        # return HttpResponse("No Such Article")
    # return HttpResponse("This article’s desciption is %s" % article.article_text)

def search(request, article_text):
    search_res = list(Article.objects.filter(article_text__contains=article_text).values_list("article_text"))
    try:
        for i in search_res:
            articles = articles + "<h3>%i: "%(search_res.index(i)+1) + str(*i) + "</h3><br>"
        return HttpResponse("<h2>This is the result of search</h2> %s" % articles)
    except:
        return HttpResponse("No such articles")

def archive(request):
    return HttpResponse("This are the articles for the last N years/months/days <br>")

def showComments(request, article_id):
    return HttpResponse("This is all comments to this article %i" % article_id)
    
'''
