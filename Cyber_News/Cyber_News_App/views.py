from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template import RequestContext

from article_pages.models import Article
from game_pages.models import Game


# Here will be placed latest games/news/blogs/threads etc
def index(request):
    articles = Article.objects.all().order_by('article_date')
    recent_games = Game.objects.all().order_by('game_rd')[:3]
    return render(request, 'Cyber_News_App/homepage.html', {'articles': articles, 'recent_games': recent_games})


def search(request):
    if request.method == "POST":
        if 'Search' in request.POST:
            search_text = request.POST.get("search_field")
            if len(search_text)>0:
                search_games = Game.objects.filter(game_name__contains=search_text)
                search_arts = Article.objects.filter(article_text__contains=search_text)
                return render(request, "Cyber_News_App/search.html",
                        {"search_arts": search_arts,
                         "search_games": search_games,
                         "empty_res":"There is no fitting results.",})
            else:
                return render(request, "Cyber_News_App/search.html",{"empty_res":"There is no fitting results.",})
    else:
        return render(request, "Cyber_News_App/search.html",
                      {"empty_res": "There is no fitting results.", })


def contacts(request):
    return render(request, 'Cyber_News_App/contacts.html')
