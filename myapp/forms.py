from cProfile import label
from dataclasses import fields
from pyexpat import model
from socket import fromshare
from tkinter import Widget

from django import forms 
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext , gettext_lazy as _




class UserRegistration(UserCreationForm):
    username = forms.CharField(required = True , label = 'Email address' , widget = forms.EmailInput( attrs= {'class': 'form-control'}))
    password1 = forms.CharField(label='Password' , widget= forms.PasswordInput(attrs={'class' : 'form-control'}))
    password2 = forms.CharField(label= 'Confirm password(again)', widget= forms.PasswordInput(attrs={'class' : 'form-control'}))

    class Meta:
        model = User
        fields = ['username' , 'password1' , 'password2']


class LoginForm(AuthenticationForm):
    username = UsernameField(widget= forms.EmailInput(attrs={'class' : 'form-control' , 'autofocus' : True}))
    password = forms.CharField(label=_("Password"), strip = False , widget= forms.PasswordInput(attrs= {'autocomplete' : 'current-password' , 'class' : 'form-control' }) )

