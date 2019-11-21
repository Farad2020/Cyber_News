from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
#User = get_user_model()
from users.models import User


class SimpleUserForm(UserCreationForm):
    # password = forms.CharField(widget=forms.PasswordInput())
    class Meta(UserCreationForm.Meta):
        model = User


class SimpleUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User

