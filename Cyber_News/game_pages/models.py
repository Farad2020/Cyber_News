from django.db import models
from users.models import User
from multiselectfield import MultiSelectField
#from article_pages.models import Article

genres = (
    ("Action", "Action"), ("FPS", "FPS"), ("Strategy", "Strategy"), ("Shooter", "Shooter"),
    ("Platformer", "Platformer"), ("Fighting", "Fighting"), ("Beat 'em up", "Beat 'em up"),
    ("Stealth", "Stealth"), ("Survival", "Survival"), ("Battle Royale", "Battle Royale"),
    ("Rhythm games", "Rhythm games"), ("Survival horror", "Survival horror"),
    ("Metroidvania", "Metroidvania"), ("Visual novels", "Visual novels"),
    ("Interactive movie", "Interactive movie"), ("Action RPG", "Action RPG"),("RPG", "RPG"),
    ("JRPG", "JRPG"), ("MMORPG", "MMORPG"), ("Quest", "Quest"), ("Roguelikes", "Roguelikes"),
    ("Simulator", "Simulator"), ("Strategy", "Strategy"), ("MOBA", "MOBA"), ("RTS", "RTS"),
    ("Tower defense", "Tower defense"), ("TBS", "TBS"), ("Sports", "Sports"),
    ("Racing", "Racing"), ("MMO", "MMO"), ("Soulslike", "Soulslike"),
    ("Sandbox", "Sandbox"), ("Adventure", "Adventure"), ("Hack and slash", "Hack and slash"),
)

platforms = (
    ("PC", "PC"), ("Xbox One", "Xbox One"), ("PlayStation 4", "PlayStation 4"), ("Nintendo Switch", "Nintendo Switch"),
    ("PlayStation 3", "PlayStation 3"), ("Wii U", "Wii U"), ("Xbox 360", "Xbox 360"), ("3DS", "3DS"),
    ("PlayStation Vita", "PlayStation Vita"),
)

age_range = (
    ("E", "E"), ("E 10+", "E 10+"), ("T", "T"), ("M", "M"),
    ("A", "A"),
)


class Game(models.Model):
    game_name = models.CharField(max_length=1000)
    game_developer = models.CharField(max_length=1000)
    game_text = models.TextField(default="")
    game_publisher = models.CharField(max_length=1000)
    game_platforms = MultiSelectField(choices=platforms, default=None)
    game_genre = MultiSelectField(choices=genres, max_choices=5, default=None)
    game_rd = models.DateField('date published') # released date
    game_age_rating = MultiSelectField(choices=age_range, max_choices=1, default=None)
    game_img = models.ImageField(upload_to='game_img/', default=None, null=True)
    game_trailer = models.URLField(max_length=200, default=None, blank=True, null=True)
    followers = models.ManyToManyField(User, default=None, blank=True, null=True)
    #related_articles = models.ManyToManyField(Article, default=None, blank=True, null=True)
    #related_blogs = models.ManyToManyField(Blog, default=None, blank=True, null=True)
    #related_threads = models.ManyToManyField(Thread, default=None, blank=True, null=True)
    # link to articles, blogs, threads

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


class RatingSystem(models.Model):
    score = models.FloatField(default=0.0)
    rater_id = models.ForeignKey(User, on_delete=models.CASCADE)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)