from django.urls import path
from django.conf.urls import url
from . import views as v1
from django.contrib.auth import views as auth_views

app_name = "cyber_news"

urlpatterns = [
    path('article/<article_id>/', v1.article_details, name='article'),
    path('home/', v1.homepage),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('contacts/', v1.contacts, name="contacts"),
    url('', v1.index, name="index"),
]