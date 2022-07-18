from cProfile import label
from dataclasses import fields
from pyexpat import model
from socket import fromshare
from tkinter import Widget
from myapp.models import *

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

'''
class CoustomerDetails(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [ 'first_name' , 'last_name' , 'mobile_number' , 'email' , 'locality' , 'address' , 'city'
        , 'pincode' , 'landmark' , 'state']

        widgets = {'first_name' : forms.TextInput(attrs={'class' : 'form-control , customerForm' ,'placeholder' : 'First Name'}),
        'last_name' : forms.TextInput(attrs={'class' : 'form-control customerForm', 'placeholder' : 'Last Name'}),
        'mobile_number' : forms.NumberInput(attrs={'class' : 'form-control customerForm', 'placeholder' : '10 digit mobile number'}),
        'email' : forms.EmailInput(attrs={'class' : 'form-control' 'customerForm' ,  'placeholder' : 'Email' }),       
        'locality' : forms.TextInput(attrs={'class' : 'form-control customerForm' , 'placeholder' : 'Locality'}),
        'address' : forms.Textarea(attrs={'class' : 'form-control customerForm' , 'placeholder' : 'Address (Area and Street)'}),
        'city' : forms.TextInput(attrs={'class' : 'form-control customerForm' , 'placeholder' : 'City/Distict/Town'}),
        'pincode' : forms.NumberInput(attrs={'class' : 'form-control customerForm' , 'placeholder' : 'Pincode'}),
        'landmark' : forms.TextInput(attrs={'class' : 'form-control customerForm', 'placeholder' : 'Landmark'}),
        'state' : forms.TextInput(attrs={'class' : 'form-control customerForm' , 'placeholder' : 'State'})}
'''




