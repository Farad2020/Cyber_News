from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import SimpleUser

class SimpleUserForm(UserCreationForm):

    # password = forms.CharField(widget=forms.PasswordInput())
    class Meta(UserCreationForm.Meta):
        model = SimpleUser
        #fields = ('email','username', 'userImg')
        

class SimpleUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = SimpleUser
        #fields = ('email','username', 'userImg')
