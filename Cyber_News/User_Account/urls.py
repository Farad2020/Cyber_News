from django.urls import path
from django.conf.urls import url
from django.contrib.auth.views import auth_login
from . import views

app_name = "user_accounts"

urlpatterns = [
    path('', auth_login, name="login"),

    path("register", views.registerView.as_view(), name="registration"),

    path("user/", views.profile, name="profile"),
]
