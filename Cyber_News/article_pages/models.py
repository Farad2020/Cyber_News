from django.db import models

# Create your models here.

from django.db import models
from django.forms import ModelForm
from game_pages.models import Game
from django.conf import settings
from users.models import User

# Create your models here.


class Article(models.Model):
    article_name = models.CharField(max_length=1000)
    article_text = models.TextField(default="")
    article_date = models.DateTimeField(auto_now_add=True)  # earlier was written this: 'date published'
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE, null=True)
    article_score = models.ManyToManyField(User, default=None, blank=True, null=True, related_name="article_raters")
    numberOfClicks = models.IntegerField(default=0)
    article_img = models.ImageField(upload_to='article_img/', default='NULL')
    is_active = models.BooleanField(verbose_name="Is Active", default=True)

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

    @classmethod
    def create(self, article_name, article_text, game_id, article_img):
        article = self(article_name=article_name, article_text=article_text, game_id=game_id, article_img=article_img)
        return article


class Thread(models.Model): # later need to add comments to threads
    thread_name = models.CharField(max_length=1000)
    thread_text = models.TextField()
    thread_date = models.DateTimeField(auto_now_add=True)
    thread_author = models.ForeignKey(User, on_delete=models.CASCADE)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    is_active = models.BooleanField(verbose_name="Is Active", default=True)

    def snippet(self):  # returns sneak-peek for article content
        return self.thread_text[:50] + "..."

    def __str__(self):
        return self.thread_author.username


class Blogs(models.Model):
    blog_name = models.CharField(max_length=1000)
    blog_text = models.TextField(default="")
    blog_date = models.DateTimeField(auto_now_add=True)  # earlier was written this: 'date published'
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE, null=True)
    blog_score = models.ManyToManyField(User, default=None, blank=True, null=True, related_name="blog_raters")
    numberOfClicks = models.IntegerField(default=0)
    blog_img = models.ImageField(upload_to='blog_img/', default='NULL')
    is_active = models.BooleanField(verbose_name="Is Active", default=True)

    def __str__(self):
        return self.blog_name

    def snippet(self):  # returns sneak-peek for article content
        return self.blog_text[:50] + "..."


class Comment(models.Model):
    comments_text = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE, default=None, null=True)
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE, default=None, null=True)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, default=None, null=True)
    is_active = models.BooleanField(verbose_name="Is Active", default=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    upvoters = models.ManyToManyField(User, default=None, blank=True, null=True, related_name="comment_raters")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True, related_name="receiver")
    comment_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.comments_text

"""
class LikeSystem(models.Model):
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, default=None, blank=True, null=True)
"""
