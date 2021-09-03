from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm, UsernameField
from django.contrib.auth.models import User
from django.forms import ModelForm
from dal import autocomplete
from django import forms

from userfollows.models import Userfollow


class UserfollowForm(ModelForm):
    class Meta:
        model = Userfollow
        fields = ('followed_user',)
        labels = {"followed_user": "nom d'utilisateur"}
        widgets = {
            'followed_user': autocomplete.ModelSelect2(url='user-autocomplete')
        }

