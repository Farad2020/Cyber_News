from django.urls import path
from django.conf.urls import url
from . import views as v1
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views

app_name = "cyber_news"

urlpatterns = [
    path('article/<article_id>/', v1.article_details, name='article'),
    path('home/', v1.homepage),
    path('contacts/', v1.contacts, name="contacts"),
    url('index/', v1.index, name="index"),
]
urlpatterns += staticfiles_urlpatterns()