from django.contrib.auth.decorators import permission_required

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from .forms import *
from article_pages.models import *
from django.urls import reverse
import datetime

from django.core.files.storage import FileSystemStorage

# Create your views here.
def get_all_games(request):
    games = Game.objects.filter(is_active=True).order_by('game_name')
    box_genres = ["Action", "Action RPG", "Adventure", "Battle Royale",
                "Beat 'em up", "Fighting", "FPS", "Interactive movie",
                "JRPG", "Metroidvania", "MMO", "MMORPG", "MOBA", "Platformer",
                "Quest", "Racing", "Rhythm games", "Roguelikes", "RPG", "RTS",
                "Sandbox", "Shooter", "Simulator", "Soulslike", "Sports", "Stealth",
                "Strategy", "Survival", "Survival horror", "TBS", "Tower defense",
                "Visual novels", "Hack and slash",]
    if request.method == "POST":
        chosen_genres = request.POST.get('box_genres')
        if chosen_genres:
            new_game_list = []
            for game in games:
                if str(game.game_genre).__contains__(chosen_genres):
                    new_game_list.append(game)
            games = new_game_list
    return render(request, "game_pages/games_page.html", {'games': games,
                                                          'box_genres': box_genres})


def create_game_page(request):
    form = EditGameForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        form = EditGameForm()
        return redirect('game_pages:games_page')
    return render(request, "game_pages/game_creation_page.html", {'form': form})


def game_details(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    game.save()
    related_articles = Article.objects.filter(game_id=game)
    game_rating = calculate_rating(request, game_id)
    if request.method == 'POST':
        if 'remove' in request.POST:
            game.is_active = False
        elif 'return' in request.POST:
            game.is_active = True
        elif 'edit' in request.POST:
            return redirect('game_pages:game_edit',game_id)
        elif 'follow' in request.POST:
            game.followers.add(request.user)
        elif 'unfollow' in request.POST:
            game.followers.remove(request.user)
        elif 'rate' in request.POST:
            given_score = request.POST.get("rating")
            try:
                new_rate = RatingSystem.objects.get(rater_id=request.user,game_id=game)
                new_rate.score = given_score
                new_rate.save()
            except:
                new_rate = RatingSystem.objects.get_or_create(rater_id=request.user, game_id=game,score=given_score)
                new_rate.save()
            game_rating = calculate_rating(request, game_id)
    game.save()
    return render(request, "game_pages/game_details_page.html", {'game': game,
                                                                 'game_rating':game_rating,
                                                                 'related_articles': related_articles,
                                                                 })

def calculate_rating(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    game_rates = RatingSystem.objects.filter(game_id=game)
    game_rating = 0.0
    for rate in game_rates:
        game_rating += rate.score
    if len(game_rates) > 0:
        game_rating = game_rating / len(game_rates)
    return game_rating


#maybe delete from edit?
#@permission_required()
def edit_game_info(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    # request.POST, request.FILES or None
    form = EditGameForm(request.POST or None, request.FILES or None, instance=game)
    if request.method == 'POST':
        if 'edit' in request.POST:
            form.save()
            return redirect('game_pages:games_page')
    return render(request, "game_pages/edit_game_info.html", {'form': form})
