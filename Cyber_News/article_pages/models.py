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
    #author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    rating = models.FloatField(default=0.0)
    numberOfClicks = models.IntegerField(default=0)
    isBlog = models.BooleanField(default = True)
    article_img = models.ImageField(upload_to='article_img/', default='NULL')
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

'''
    @classmethod
    def create(self, article_name, article_text, article_date, author_id, game_id, rating, article_img):
        article = self(article_name=article_name, article_text =article_text, article_date=article_date,
                    author_id=author_id, game_id=game_id, rating=rating, article_img=article_img)
        return article
'''

class Comments(models.Model):
	comments_text = models.TextField()
	article = models.ForeignKey(Article, on_delete = models.CASCADE)
	#user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

	def __str__(self):
		return self.comments_text

