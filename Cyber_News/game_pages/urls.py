from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.conf.urls import url, static
from django.conf import settings
from . import views
from Cyber_News_App import urls

app_name = "game_pages"

urlpatterns = [
    path('', views.get_all_games, name="games_page"),
    path('1create/', views.create_game_page, name="create_game"),
    path('<int:game_id>/', views.game_details, name="game_det"),
    path('<int:game_id>/edit/', views.edit_game_info, name="game_edit"),
]
# BUT FIRST IMGS!
'''
if settings.DEBUG:
    #urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
'''