from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('User_Account.urls')),
    path('games/', include('game_pages.urls')),
    path('', include('Cyber_News_App.urls')),
    path('', include('django.contrib.auth.urls')),
]
#urlpatterns += staticfiles_urlpatterns()