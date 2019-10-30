from django.db import models

# Create your models here.

#First model
class Article(models.Model):
    article_id = models.CharField(max_length=9999)
    article_text = models.TextField()
    article_date = models.DateTimeField("date published")


class Blog(models.Model):
    blog_id = models.CharField(max_length=9999)
    blog_text = models.TextField()
    blog_date = models.DateTimeField("date published")
    blog_author = models.CharField(max_length=9999)


class Thread(models.Model):
    thread_id = models.CharField(max_length=9999)
    thread_text = models.TextField()
    thread_date = models.DateTimeField("date published")
    thread_author = models.CharField(max_length=9999)


class Comment(models.Model):
    comment_id = models.CharField(max_length=9999)
    comment_text = models.TextField()
    comment_date = models.DateTimeField("date published")


class Editor(models.Model):
    editors_name = models.CharField(max_length=100)
    editors_surname = models.CharField(max_length=100)
    editor_id = models.CharField(max_length=1000)


class User(models.Model):
    user_name = models.CharField(max_length=100)
    user_surname = models.CharField(max_length=100)
    user_id = models.CharField(max_length=1000)
