from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import *
from .models import *
# Register your models here.

class CustomizedAdmin(UserAdmin):
    add_form = SimpleUserForm
    form = SimpleUserChangeForm
    model = SimpleUser
    #list_display = ['email', 'username', 'userImg']

'''
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('userImg',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('userImg',)}),
    )
'''

admin.site.register(SimpleUser,CustomizedAdmin)
