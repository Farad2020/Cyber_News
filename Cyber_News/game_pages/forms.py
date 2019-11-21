from django.db import models
from django import forms
from .models import *

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime #for checking renewal date range.

class EditGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = [
            'game_name',
            'game_developer',
            'game_text',
            'game_publisher',
            'game_rd',
            'game_rating',
            #game_img
        ]