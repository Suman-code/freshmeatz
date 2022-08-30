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


# sign up form

class UserRegistration(UserCreationForm):
    username = forms.CharField( label= 'Username', widget=forms.TextInput( attrs={'class': 'input', 'placeholder': 'Your username'}))
    email = forms.CharField(required = True , label = 'Email address' , widget = forms.EmailInput( attrs= {'class': 'input', 'placeholder': 'e.g. demo@gmail.com '}))
    password1 = forms.CharField(label='Password' , widget= forms.PasswordInput(attrs={'class' : 'input', 'placeholder': 'Password'}))
    password2 = forms.CharField(label= 'Confirm password(again)', widget= forms.PasswordInput(attrs={'class' : 'input', 'placeholder': 'Confrim passwor'}))

    class Meta:
        model = User
        fields = ['username' , 'email',  'password1' , 'password2']


class LoginForm(AuthenticationForm):
    username = UsernameField(widget= forms.TextInput(attrs={'class' : 'input' , 'placeholder': 'Your username', 'autofocus' : True}))
    password = forms.CharField(label=_("Password"), strip = False , widget= forms.PasswordInput(attrs= {'autocomplete' : 'current-password' , 'class' : 'input' , 'placeholder': '********' }) )


# user address form

class UserProfileForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={

        "class" :' input',
        'type' : 'text',
        'placeholder' : 'Enter your first name',
        'id' : 'firstname',
        

    }))

  

    last_name = forms.CharField(widget=forms.TextInput(attrs={

        "class" :' input',
        'type' : '',
        'id' : 'lastname',
        'placeholder' : 'Enter yor last name'

    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={

        "class" :' input',
        'type' : 'email',
        'id' : 'inputemail',
        'placeholder' : ' e.g. demo@gmail.com '

    }))

    mobile_number = forms.CharField(widget=forms.NumberInput(attrs={

        "class" :' input',
        'type' : 'tel',
        'id' : 'inputphone',
        'placeholder' : '10 digit mobile number'

    }))
    address = forms.CharField(widget=forms.Textarea(attrs={

        "class" :'  input',
        'type' : 'textarea',
        'id' : 'inputTextarea',
        'placeholder' : 'Address (Area and street)'

    }))
    locality = forms.CharField(widget=forms.TextInput(attrs={

        "class" :'  input',
        'type' : '',
        'id' : 'inputLocality',
        'placeholder' : 'Locality'

    }))

    city = forms.CharField(widget=forms.TextInput(attrs={

        "class" :' input',
        'type' : '',
        'id' : 'inputCity',
        'placeholder' : 'City/Distict/Town'

    }))

    city = forms.CharField(widget=forms.TextInput(attrs={

        "class" :'input',
        'type' : '',
        'id' : 'inputCity',
        'placeholder' : 'City/Distict/Town'

    }))

    landmark = forms.CharField(widget=forms.TextInput(attrs={

        "class" :' input',
        'type' : '',
        'id' : 'inputLandmark',
        'placeholder' : 'Near landmark'

    }))

    state = forms.CharField(widget=forms.TextInput(attrs={

        "class" :'  input',
        'type' : '',
        'id' : 'inputState',
        'placeholder' : 'State'

    }))

    pincode = forms.CharField(widget=forms.NumberInput(attrs={

        "class" :'  input',
        'type' : '',
        'id' : 'inputPincode',
        'placeholder' : 'Pincode of area'

    }))

    address_type = forms.CharField(widget=forms.NumberInput(attrs={

        "class" :' input',
        'type' : '',
        'id' : 'addressType',
    

    }))



    class Meta:
        model = UserProfile
        fields = [ 'first_name' , 'last_name' , 'mobile_number' , 'email' , 'locality' , 'address' , 'city'
        , 'pincode' , 'landmark' , 'state' , 'address_type']








