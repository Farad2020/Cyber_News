from django.urls import path
from django.conf.urls import url
from . import views

app_name = "cyber_news"

urlpatterns = [
    # GIANT QUESTION!!! why replacing urls with positions fixed the program?
    path('article/<article_id>/', views.article_details, name='article'),

    url('', views.index, name="index"),
    path('home/', views.homepage),
    path('login/', views.login),


    #path('archive/', views.archive, name = 'archive'),
    #path('article/<int:article_id>/comment', views.addComment, name='addComment'),
    #path('contacts/', views.contacts, name="contacts")
]
