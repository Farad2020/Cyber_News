from django.db import models

# Create your models here.

from django.db import models
from django.forms import ModelForm
from game_pages.models import Game

# Create your models here.


class Article(models.Model):
    article_name = models.CharField(max_length=1000)
    article_text = models.TextField(default="")
    article_date = models.DateTimeField(auto_now_add=True)  # earlier was written this: 'date published'
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    rating = models.FloatField(default=0.0)
    numberOfClicks = models.IntegerField(default=0)
    isBlog = models.BooleanField(True)
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


