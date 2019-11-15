from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .forms import *
from .models import *

class CustomizedAdmin(UserAdmin):
    add_form = SimpleUserForm
    form = SimpleUserChangeForm
    model = User

admin.site.register(User)