from django.db import models

# Create your models here.

#First model
class Article(models.Model):
    article_id = models.CharField(max_length=9999)
    article_text = models.TextField()
    article_date = models.DateTimeField("date published")


class Editor(models.Model):
    editors_name = models.CharField(max_length=100)
    editors_surname = models.CharField(max_length=100)
    editor_id = models.CharField(max_length=1000)

