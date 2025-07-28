from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserApp


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = UserApp
        fields = ("username", "password1", "password2")
