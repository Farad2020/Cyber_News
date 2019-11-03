from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('home', views.homepage),
    path('articles', views.articles_page),
    path('login', views.login),

]