from django.contrib.auth.forms import UserCreationForm as\
    BaseUserCreationForm, UsernameField
from django.contrib.auth.models import User


class UserCreationForm(BaseUserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email")
        field_classes = {'username': UsernameField}
