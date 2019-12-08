from django.db import models
from django import forms
from .models import *

class EditArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'article_name',
            'article_text',
            #'article_date',
            #'author_id',
            'game_id',
            #'rating',
            #'numberOfClicks',
            'article_img',
        ]

class EditBlogForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = [
            'blog_name',
            'blog_text',
            #'blog_date',
            #'author_id',
            'game_id',
            #'rating',
            #'numberOfClicks',
            'blog_img',
        ]


class EditThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = [
            'thread_name',
            'thread_text',
            #'thread_date',
            #'thread_author',
            'game_id',
        ]


class EditCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'comments_text',
        ]

