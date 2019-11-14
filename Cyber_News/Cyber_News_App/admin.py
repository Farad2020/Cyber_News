from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import *
# Register your models here.

admin.site.register(Game)
admin.site.register(Article)
admin.site.register(Thread)
admin.site.register(Comments)

