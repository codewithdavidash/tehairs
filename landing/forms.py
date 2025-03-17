from django.contrib.auth.models import User
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
)
from django import forms
from .models import *


class LoginForm(AuthenticationForm):
    pass


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']