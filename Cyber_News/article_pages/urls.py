from django.urls import path
from django.conf.urls import url
from . import views

app_name = "article_pages"

urlpatterns = [
    path('articles/', views.get_all_articles, name = "article_pages")
]