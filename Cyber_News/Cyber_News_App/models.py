from django.db import models

# Create your models here.

#First model
class Article(models.Model):
    article_id = models.CharField(max_length=9999)
    article_text = models.TextField()
    article_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.article_text + self.article_date


class Blog(models.Model):
    blog_id = models.CharField(max_length=9999)
    blog_text = models.TextField()
    blog_date = models.DateTimeField(auto_now_add=True)
    blog_author = models.CharField(max_length=9999)

    def __str__(self):
        return self.blog_author + self.blog_text + self.blog_date


class Thread(models.Model):
    thread_id = models.CharField(max_length=9999)
    thread_text = models.TextField()
    thread_date = models.DateTimeField(auto_now_add=True)
    thread_author = models.CharField(max_length=9999)

    def __str__(self):
        return self.thread_author + self.thread_text + self.thread_date


class Comment(models.Model):
    comment_id = models.CharField(max_length=9999)
    comment_text = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_text + self.comment_date


class Editor(models.Model):
    editors_name = models.CharField(max_length=100)
    editors_surname = models.CharField(max_length=100)
    editor_id = models.CharField(max_length=1000)

    def __str__(self):
        return self.editors_name + self.editors_surname


class User(models.Model):
    user_name = models.CharField(max_length=100)
    user_surname = models.CharField(max_length=100)
    user_id = models.CharField(max_length=1000)

    def __str__(self):
        return self.user_name + self.user_surname
