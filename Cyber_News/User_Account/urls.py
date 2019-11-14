from django.urls import path
from django.conf.urls import url
from . import views

app_name = "user_accounts"

urlpatterns = [
    path('signup/', views.sign_up, name='sign_up'),
]
