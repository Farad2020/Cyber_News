from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class SimpleUser(AbstractUser):
	#userImg = models.ImageField(upload_to='user_avas/', default='NULL')

	def __str__(self):
		return self.username