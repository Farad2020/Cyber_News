from django.urls import path
from django.conf.urls import url
from . import views as v1
from django.contrib.auth import views as auth_views

app_name = "cyber_news"

urlpatterns = [
    # GIANT QUESTION!!! why replacing urls with positions fixed the program?
    path('article/<article_id>/', v1.article_details, name='article'),
    # path('signup/', views.sign_up, name='sign_up'),
    path('home/', v1.homepage),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    url('', v1.index, name="index"),
]
# path('archive/', views.archive, name = 'archive'),
# path('article/<int:article_id>/comment', views.addComment, name='addComment'),
# path('contacts/', views.contacts, name="contacts")
'''
    path('games_page/', views.games_page, name="games"),
    path('games_page/<game_id>/', views.game_details, name='game_det'),
    # some trouble with path games_page/create_game/
    path('games_page//create_game/', views.create_game_page, name='game_creation'),
'''