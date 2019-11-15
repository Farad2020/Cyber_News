from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


# Create your models here.

class User(AbstractUser):
	User = get_user_model()
	def __str__(self):
		return self.username