from django.db import models

# Create your models here.
"""
'''''''''''''''BIG PLAN''''''''''''''
Everyone gets their own model, and do html for that page to be fully functional
later connect them with each other
'''''''''''''''''''''REMEMBER: WHEN YOU CHANGE MODEL, MAKE MIGRATION!!''''''''''''''''''''

Alua - User, Editor, 
Madina - Article, Blog
Faraby - Game

"""

"""
class Article(models.Model):
    article_name = models.CharField(max_length=9999)
    article_text = models.TextField()
    article_date = models.DateTimeField(auto_now_add=True)
    article_slug = models.SlugField()
    # for url tutorial: https://www.youtube.com/watch?v=c2hbT0uIcOQ&list=PL4cUxeGkcC9ib4HsrXEYpQnTOTZE1x0uc&index=14

    def __str__(self):
        return self.article_name

    def snippet(self):  # returns sneak-peek for article content
        return self.article_text[:50] + "..."


class Blog(models.Model):
    blog_name = models.CharField(max_length=9999)
    blog_text = models.TextField()
    blog_date = models.DateTimeField(auto_now_add=True)
    blog_author = models.CharField(max_length=9999)

    def __str__(self):
        return self.blog_author + self.blog_name + self.blog_text


class Thread(models.Model): #later need to add comments to threads
    thread_text = models.TextField()
    thread_date = models.DateTimeField(auto_now_add=True)
    thread_author = models.CharField(max_length=9999)

    def __str__(self):
        return self.thread_author + self.thread_text


class Comment(models.Model):
    comment_text = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_text


class Editor(models.Model):
    editors_name = models.CharField(max_length=100)
    editors_surname = models.CharField(max_length=100)

    def __str__(self):
        return self.editors_name + self.editors_surname


class User(models.Model):
    user_name = models.CharField(max_length=100)
    user_surname = models.CharField(max_length=100)

    def __str__(self):
        return self.user_name + self.user_surname

"""

from django.db import models
from django.forms import ModelForm


# Create your models here.

class User(models.Model):
    login = models.CharField(max_length=100)
    isEditor = models.BooleanField(False, True)  # rang of the user
    isActive = models.BooleanField(False, True)  # check if use is banned, deleted or not

    # password = models.PasswordField()

    def __str__(self):
        return self.login


class GamePage(models.Model):
    game_name = models.CharField(max_length=1000)
    game_developer = models.CharField(max_length=1000)
    game_publisher = models.CharField(max_length=1000)
    game_rd = models.DateTimeField('date published') # released date
    game_rating = models.FloatField(default=0.0)
    # link to articles, blogs, threads
    # image

    def __str__(self):
        return self.game_name

    def rate_game(self, new_rate):
        if self.rating == 0.0:
            self.rating = new_rate
            return self.rating
        else:
            return (self.rating + new_rate) / 2


class Article(models.Model):
    article_name = models.CharField(max_length=1000)
    article_text = models.TextField(default="")
    article_date = models.DateTimeField(auto_now_add=True)  # earlier was written this: 'date published'
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.FloatField(default=0.0)
    numberOfClicks = models.IntegerField(default=0)
    isBlog = models.BooleanField(False, True)
    # game_link
    # article
    # image optional

    def __str__(self):
        return self.article_name

    def rate_article(self, new_rate):
        if self.rating == 0.0:
            self.rating = new_rate
            return self.rating
        else:
            return (self.rating + new_rate) / 2

    def snippet(self):  # returns sneak-peek for article content
        return self.article_text[:50] + "..."


class Thread(models.Model): #later need to add comments to threads
    thread_text = models.TextField()
    thread_date = models.DateTimeField(auto_now_add=True)
    thread_author = models.ForeignKey(User, on_delete=models.CASCADE)
    #link to the game

    def __str__(self):
        return self.thread_author + self.thread_text


class Comments(models.Model):
    comments_text = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    # comment_author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.comments_text