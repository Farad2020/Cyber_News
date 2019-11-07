from django.urls import path
from django.conf.urls import url
from . import views

app_name = "cyber_news"

urlpatterns = [
    # path('', views.index, name='index'),
    url('', views.index, name="index"),
    # created from tutorial, link in models, to use img watch part15

    path('article/<article_id>/', views.article_details, name='article'),
    path('home/', views.homepage),
    path('login/', views.login),


    #path('archive/', views.archive, name = 'archive'),
    #path('article/<int:article_id>/comment', views.addComment, name='addComment'),
    #path('contacts/', views.contacts, name="contacts")
]
