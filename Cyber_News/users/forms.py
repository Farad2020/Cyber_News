from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
User = get_user_model()


class SimpleUserForm(UserCreationForm):
    # password = forms.CharField(widget=forms.PasswordInput())
    class Meta(UserCreationForm.Meta):
        model = User


class SimpleUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User