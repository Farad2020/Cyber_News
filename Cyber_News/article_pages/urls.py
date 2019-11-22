from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "article_pages"

urlpatterns = [
    path('articles/', views.get_all_articles, name = "article_pages"),
    path('create/', views.create_article_page, name="create_article"),
    path('delete/', views.articles_delete, name="delete_article"),
    path('<int:article_id>/', views.article_details, name="article_det"),
    path('<int:article_id>/edit/', views.edit_article, name="article_edit"),
    path('article/<int:article_id>/comment', views.addComment, name='addComment'),
]
urlpatterns += staticfiles_urlpatterns()