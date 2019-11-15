from django.contrib import admin
from .forms import *
from .models import *

admin.site.register(User, CustomizedAdmin)
