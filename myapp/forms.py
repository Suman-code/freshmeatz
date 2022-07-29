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




class UserProfileForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={

        "class" :'form-control input',
        'type' : '',
        'placeholder' : 'Enter yor first name',
        'id' : 'firstname'

    }))

  

    last_name = forms.CharField(widget=forms.TextInput(attrs={

        "class" :' form-control input',
        'type' : '',
        'id' : 'lastname',
        'placeholder' : 'Enter yor last name'

    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={

        "class" :' form-control input',
        'type' : 'email',
        'id' : 'inputemail',
        'placeholder' : ' e.g. demo@gmail.com '

    }))

    mobile_number = forms.CharField(widget=forms.NumberInput(attrs={

        "class" :' form-control input',
        'type' : 'tel',
        'id' : 'inputphone',
        'placeholder' : '10 digit mobile number'

    }))
    address = forms.CharField(widget=forms.Textarea(attrs={

        "class" :' form-control input',
        'type' : 'textarea',
        'id' : 'inputTextarea',
        'placeholder' : 'Address (Area and street)'

    }))
    locality = forms.CharField(widget=forms.TextInput(attrs={

        "class" :' form-control input',
        'type' : '',
        'id' : 'inputLocality',
        'placeholder' : 'Locality'

    }))

    city = forms.CharField(widget=forms.TextInput(attrs={

        "class" :' form-control input',
        'type' : '',
        'id' : 'inputCity',
        'placeholder' : 'City/Distict/Town'

    }))

    city = forms.CharField(widget=forms.TextInput(attrs={

        "class" :' form-control input',
        'type' : '',
        'id' : 'inputCity',
        'placeholder' : 'City/Distict/Town'

    }))

    landmark = forms.CharField(widget=forms.TextInput(attrs={

        "class" :' form-control input',
        'type' : '',
        'id' : 'inputLandmark',
        'placeholder' : 'Near landmark'

    }))

    state = forms.CharField(widget=forms.TextInput(attrs={

        "class" :' form-control input',
        'type' : '',
        'id' : 'inputState',
        'placeholder' : 'State'

    }))

    pincode = forms.CharField(widget=forms.NumberInput(attrs={

        "class" :' form-control input',
        'type' : '',
        'id' : 'inputPincode',
        'placeholder' : 'Pincode of area'

    }))

    address_type = forms.CharField(widget=forms.NumberInput(attrs={

        "class" :' form-control input',
        'type' : '',
        'id' : 'addressType',
    

    }))




    '''
     widgets = {'first_name' : forms.TextInput(attrs=
        
        { 'id':'fm' ,



        'placeholder' : 'First Name'}),


        'last_name' : forms.TextInput(attrs={'id':'fm' , 'placeholder' : 'Last Name'}),
        'mobile_number' : forms.NumberInput(attrs={'class' : 'form-control customerForm', 'placeholder' : '10 digit mobile number'}),
        'email' : forms.EmailInput(attrs={'class' : 'form-control' 'customerForm' ,  'placeholder' : 'Email' }),       
        'locality' : forms.TextInput(attrs={'class' : 'form-control customerForm' , 'placeholder' : 'Locality'}),
        'address' : forms.Textarea(attrs={'class' : 'form-control customerForm' , 'placeholder' : 'Address (Area and Street)'}),
        'city' : forms.TextInput(attrs={'class' : 'form-control customerForm' , 'placeholder' : 'City/Distict/Town'}),
        'pincode' : forms.NumberInput(attrs={'class' : 'form-control customerForm' , 'placeholder' : 'Pincode'}),
        'landmark' : forms.TextInput(attrs={'class' : 'form-control customerForm', 'placeholder' : 'Landmark'}),
        'state' : forms.TextInput(attrs={'class' : 'form-control customerForm' , 'placeholder' : 'State'}),
        'addres_type' : forms.TextInput(attrs={'class' : 'form-control customerForm'})
        }
    
    '''
       

    class Meta:
        model = UserProfile
        fields = [ 'first_name' , 'last_name' , 'mobile_number' , 'email' , 'locality' , 'address' , 'city'
        , 'pincode' , 'landmark' , 'state' , 'address_type']








