from django.db import models

# Create your models here.

#First model
class Article(models.Model):
    article_id = models.CharField(max_length=9999)
    article_name = models.CharField(max_length=9999)
    article_text = models.TextField()
    article_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.article_id + self.article_name + self.article_text


class Blog(models.Model):
    blog_id = models.CharField(max_length=9999)
    blog_name = models.CharField(max_length=9999)
    blog_text = models.TextField()
    blog_date = models.DateTimeField(auto_now_add=True)
    blog_author = models.CharField(max_length=9999)

    def __str__(self):
        return self.blog_id + self.blog_author + self.blog_name + self.blog_text


class Thread(models.Model): #later need to add comments to threads
    thread_id = models.CharField(max_length=9999)
    thread_text = models.TextField()
    thread_date = models.DateTimeField(auto_now_add=True)
    thread_author = models.CharField(max_length=9999)

    def __str__(self):
        return self.thread_id + self.thread_author + self.thread_text


class Comment(models.Model):
    comment_id = models.CharField(max_length=9999)
    comment_text = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_id + self.comment_text


class Editor(models.Model):
    editors_name = models.CharField(max_length=100)
    editors_surname = models.CharField(max_length=100)
    editor_id = models.CharField(max_length=1000)

    def __str__(self):
        return self.editor_id + self.editors_name + self.editors_surname


class User(models.Model):
    user_name = models.CharField(max_length=100)
    user_surname = models.CharField(max_length=100)
    user_id = models.CharField(max_length=1000)

    def __str__(self):
        return self.user_id + self.user_name + self.user_surname
