from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Blogs)
admin.site.register(Thread)