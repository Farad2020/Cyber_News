from django.contrib import admin

from .models import Article, Thread, Blog, Comment, Editor, User
# Register your models here.
admin.site.register(Article)
admin.site.register(Thread)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Editor)
admin.site.register(User)
