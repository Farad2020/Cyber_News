from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template import RequestContext
from django.db.models import Q

from article_pages.models import *
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
            if len(search_text) > 0:
                search_games = Game.objects.filter(
                    Q(game_name__contains=search_text) | Q(game_genre__contains=search_text)
                    | Q(game_text__contains=search_text) | Q(game_text__contains=search_text))
                search_arts = Article.objects.filter(Q(article_name__contains=search_text)
                                                     | Q(article_text__contains=search_text))
                search_blogs = Blogs.objects.filter(Q(blog_text__contains=search_text)
                                                    | Q(blog_name__contains=search_text))
                search_threads = Thread.objects.filter(Q(thread_text__contains=search_text)
                                                       | Q(thread_name__contains=search_text))
                return render(request, "Cyber_News_App/search.html",
                              {"search_arts": search_arts,
                               "search_games": search_games,
                               "search_blogs": search_blogs,
                               "search_threads": search_threads,
                               "empty_res": "There is no fitting results.", })
            else:
                return render(request, "Cyber_News_App/search.html", {"empty_res": "There is no fitting results.", })
    else:
        return render(request, "Cyber_News_App/search.html",
                      {"empty_res": "There is no fitting results.", })


def contacts(request):
    return render(request, 'Cyber_News_App/contacts.html')
