from django.urls import path
from django.conf.urls import url
from . import views

app_name = "cyber_news"

urlpatterns = [
    # GIANT QUESTION!!! why replacing urls with positions fixed the program?
    path('article/<article_id>/', views.article_details, name='article'),
    # path('signup/', views.sign_up, name='sign_up'),
    path('home/', views.homepage),
    #path('login/', views.login_view, name = 'login'),
    #path('userpage/', views.user_page, name = 'user_page'),
    #path('games_page/', views.games_page, name="games"),
    #path('games_page/<game_id>/', views.game_details, name='game_det'),
    # some trouble with path games_page/create_game/
    #path('games_page//create_game/', views.create_game_page, name='game_creation'),
    url('', views.index, name="index"),
]
# path('archive/', views.archive, name = 'archive'),
# path('article/<int:article_id>/comment', views.addComment, name='addComment'),
# path('contacts/', views.contacts, name="contacts")
