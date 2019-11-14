from django.urls import path
from django.conf.urls import url
from . import views

app_name = "game_pages"

urlpatterns = [
    path('', views.get_all_games, name="main_game_pages")
]
