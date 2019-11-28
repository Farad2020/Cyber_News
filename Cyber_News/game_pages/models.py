from django.db import models
from users.models import User


class Game(models.Model):
    game_name = models.CharField(max_length=1000)
    game_developer = models.CharField(max_length=1000)
    game_text = models.TextField(default="")
    game_publisher = models.CharField(max_length=1000)
    game_platforms = models.CharField(max_length=1000)
    game_rd = models.DateField('date published') # released date
    game_rating = models.FloatField(default=0.0)
    game_img = models.ImageField(upload_to='game_img/', default=None, null=True)
    game_trailer = models.URLField(max_length=200, default=None, blank=True, null=True)
    # link to articles, blogs, threads
    # image(ImageField), platforms(list of strings)

    def __str__(self):
        return self.game_name

    def rate_game(self, new_rate):
        if self.rating == 0.0:
            self.rating = new_rate
            return self.rating
        else:
            return (self.rating + new_rate) / 2

    @classmethod
    def create(self, game_name, game_developer, game_text, game_publisher, game_rd, game_rating):
        game = self(game_name=game_name, game_developer=game_developer, game_text=game_text,
                    game_publisher=game_publisher, game_rd=game_rd, game_rating=game_rating)
        return game


class Followers(models.Model):
    followers = models.ManyToManyField(User)
    followed_games = models.ManyToManyField(Game)
