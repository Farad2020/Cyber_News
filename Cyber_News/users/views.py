from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
# Create your views here.
from .forms import *
from game_pages.models import Game

from django.contrib.auth import get_user_model

User = get_user_model()


def register(request):
    if request.method == 'POST':
        form = SimpleUserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("cyber_news:index")
    else:
        form = SimpleUserForm()
    return render(request, 'users/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect("cyber_news:index")


@login_required
def profile(request):
    games = Game.objects.all()
    users = User.objects.all()
    return render(request, 'users/profile.html', {'games': games, 'users': users})


def edit_profile(request):
    if request.method == 'POST':
        form = SimpleUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/profile')
    else:
        form = SimpleUserChangeForm(instance=request.user)
    return render(request, 'users/edit_profile.html', {'form': form})


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'users/change_password.html', {'form': form})
