from django.contrib import admin

from django.urls import path, include
from Cyber_News_App import views, urls
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('Cyber_News_App.urls')),
    path('home/', views.homepage),
    path('login/', views.login),

]

urlpatterns += staticfiles_urlpatterns()