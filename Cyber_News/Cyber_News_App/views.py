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

    author = User.objects.get(pk=article.author_id_id)    # why id_id works!&?
    return render(request, 'Cyber_News_App/article_detail.html', {'article': article,
                                                                  'author': author})


def login(request):
    # return HttpResponse("user login page")
    return render(request, 'Cyber_News_App/logregpage.html')


def games_page(request):
    games = Game.objects.all().order_by('game_name')
    return render(request, "Cyber_News_App/games_page.html", {'games': games})


def create_game_page(request):
    if request.method == 'POST':
        try:
            game = Game(game_name=request.POST.get("game_name"), game_developer=request.POST.get("game_dev"),
                        game_publisher=request.POST.get("game_pub"), game_text=request.POST.get("game_desc"),
                        game_rd=request.POST.get("game_date"), game_rating=request.POST.get("game_rate"))
            game.save()
        except:
            print('the comments cannot be added')
    return render(request, "Cyber_News_App/game_creation_page.html", {})


def game_details(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    return render(request, "Cyber_News_App/game_details_page.html", {'game': game})



