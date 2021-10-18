from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm, UserCreationForm, UsernameField
)
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _



class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={
        'authfocus': True,
        'placeholder': 'username',
        'class': 'form control'
    }))

    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'placeholder': 'пароль',
        'class': 'form control'
    }),
    strip=False,
    )

    error_messages = {
        'invalid login': 'Введен не правильный Логин или пароль'
    }

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(
        label='пароль',
        strip=False,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'пароль',
            'class': 'form control'
        }),
    )

    password2 = forms.CharField(
        label='подтвердите пароль',
        strip=False,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'подтвердите пароль',
            'class': 'form control'
        }),
        help_text=_('Enter the same password')
    )

    error_messages = {
        'passwod_mismatch': 'Пароли не совпадают'
    }

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError('email должен быть уникальным')
        return email
