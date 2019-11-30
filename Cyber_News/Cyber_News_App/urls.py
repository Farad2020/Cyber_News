from django.urls import path
from django.conf.urls import url
from . import views as v1
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

app_name = "cyber_news"

urlpatterns = [
    #path('article/<article_id>/', v1.article_details, name='article'),
    path('contacts/', v1.contacts, name="contacts"),
    path('search/', v1.search, name="search"),
    url('index/', v1.index, name="index"),
]