from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from users.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class SimpleUserForm(UserCreationForm):
    # password = forms.CharField(widget=forms.PasswordInput())
    class Meta(UserCreationForm.Meta):
        model = User


class SimpleUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class CustomizedAdmin(UserAdmin):
    add_form = SimpleUserForm
    form = SimpleUserChangeForm
    model = User


admin.site.register(User, CustomizedAdmin)
