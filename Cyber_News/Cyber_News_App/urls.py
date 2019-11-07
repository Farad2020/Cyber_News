from django.urls import path
from django.conf.urls import url
from . import views

app_name = "cyber_news"

urlpatterns = [
    # path('', views.index, name='index'),
    url('', views.articles_page, name="list"),
    # created from tutorial, link in models, to use img watch part15
    url(r'^(?P<slug>[-\w]+)/$', views.articles_details, name="detail"),
]
