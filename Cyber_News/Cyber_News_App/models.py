from django.db import models

# Create your models here.

from django.db import models
from django.forms import ModelForm
#from game_pages.models
from users.models import User


# Create your models here.

class Editor(models.Model):
    editors_name = models.CharField(max_length=100)
    editors_surname = models.CharField(max_length=100)

    def __str__(self):
        return self.editors_name + self.editors_surname
