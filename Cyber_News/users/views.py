from django.shortcuts import render, redirect, get_object_or_404
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
    active_users = User.objects.filter(is_active = True)
    deactive_users = User.objects.exclude(is_active = True)
    return render(request, 'users/profile.html', {'games': games, 'users': users, 'active_users': active_users, 'deactive_users': deactive_users})


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


def other_user_profile(request, id):
    user = get_object_or_404(User, pk=id)
    moder_user = request.user
    if request.method == 'POST':
        if 'ban' in request.POST:
            user.is_active = False
            user.save()
            return redirect('/profile')
    return render(request, 'users/another_user_profile.html', {'user': user, 'moder_user': moder_user})

