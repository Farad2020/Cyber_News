from django.contrib import admin
from django.urls import path, include
from Cyber_News_App import views, urls
import Cyber_News_App
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', Cyber_News_App.views.homepage),
    path('articles', Cyber_News_App.views.articles_page),
    path('login', Cyber_News_App.views.login),

]

urlpatterns += staticfiles_urlpatterns()