from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
User = get_user_model()


class SimpleUserForm(UserCreationForm):
    # password = forms.CharField(widget=forms.PasswordInput())
    class Meta(UserCreationForm.Meta):
        model = User

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username = username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['dublicate_username'])


class SimpleUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class CustomizedAdmin(UserAdmin):
    add_form = SimpleUserForm
    form = SimpleUserChangeForm
    model = User
