from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.conf import settings
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

app_name = "game_pages"
urlpatterns = [
    path('all/', views.get_all_games, name="games_page"),
    path('1create/', views.create_game_page, name="create_game"),
    path('<int:game_id>/', views.game_details, name="game_det"),
    path('<int:game_id>/edit/', views.edit_game_info, name="game_edit"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
# BUT FIRST IMGS!
'''
if settings.DEBUG:
    #urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
'''