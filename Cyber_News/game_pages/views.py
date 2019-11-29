from django.contrib.auth.decorators import permission_required

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from .forms import *
from django.urls import reverse
import datetime

from django.core.files.storage import FileSystemStorage

# Create your views here.
def get_all_games(request):
    games = Game.objects.all().order_by('game_name')
    return render(request, "game_pages/games_page.html", {'games': games})


def create_game_page(request):
    form = EditGameForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        form = EditGameForm()
        return redirect('../')
    return render(request, "game_pages/game_creation_page.html", {'form': form})


def game_details(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    game.save()
    if request.method == 'POST':
        if 'delete' in request.POST:
            game.delete()
            return redirect('../')
        elif 'follow' in request.POST:
            game.followers.add(request.user)
        elif 'unfollow' in request.POST:
            game.followers.remove(request.user)
    return render(request, "game_pages/game_details_page.html", {'game': game})



#maybe delete from edit?
#@permission_required()
def edit_game_info(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    # request.POST, request.FILES or None
    form = EditGameForm(  request.POST or None, request.FILES or None, instance=game)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            form = EditGameForm()
            return redirect('../')
    return render(request, "game_pages/edit_game_info.html", {'form': form})
