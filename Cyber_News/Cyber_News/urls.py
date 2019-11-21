from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('register/', user_views.register, name='register'),
                  path('profile/', user_views.profile, name='profile'),
                  path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
                  path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
                  path('games/', include('game_pages.urls')),
                  path('main/', include('Cyber_News_App.urls')),
                  # django is a peace death, empty '' ruins my life and code
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
