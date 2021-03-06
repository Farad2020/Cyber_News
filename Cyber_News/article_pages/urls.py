from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "article_pages"

urlpatterns = [
    path('articles/', views.get_all_articles, name="article_pages"),
    path('create/', views.create_article_page, name="create_article"),
    path('<int:article_id>/', views.article_details, name="article_det"),
    path('<int:article_id>/edit/', views.edit_article, name="article_edit"),
    path('blogs/', views.get_all_blogs, name="blog_pages"),
    path('create_blog/', views.create_blog, name="create_blog"),
    path('blogs/<int:blog_id>/', views.blog_detail, name="blog_det"),
    path('blogs/<int:blog_id>/edit/', views.edit_blog, name="blog_edit"),
    path('threads/', views.get_all_threads, name="thread_pages"),
    path('create_thread/', views.create_thread, name="create_thread"),
    path('threads/<int:thread_id>/', views.thread_detail, name="thread_det"),
    path('threads/<int:thread_id>/edit/', views.edit_thread, name="thread_edit"),     # maybe none editable?
    path('comments/<int:comment_id>/edit/', views.edit_comment, name="comment_edit"),
]
urlpatterns += staticfiles_urlpatterns()