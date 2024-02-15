from django import forms
from .models import Register
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class SignupForm(forms.ModelForm):
    class Meta:
        model=Register
        fields=['Fname','Lname','Email','Phone_number','Address1','state','Password']
        labels={
            'Fname':"Enter Your First Name",
            'Lname':"Enter Your Last Name",
            'Email':"Enter you Email",
            'Phone_number':"Enter your Phone Number",
            'Address1':"Enter your Address",
            'state':"Enter the name of your State",
            'Password':"Create a Strong Password"
        }
        error_messages={
            "Fname":{
                'required':"The First Name cannot be empty",
                "max_length":"The First name can't be greater than 50 characters"
            },
            "Lname":{
                "required":"The Last Name cannot be empty",
                "max_length":"The Last name can't be greater than 50 characters"
            },
            "Email":{
                "required":"The Email cannot be empty",
                "max_length":"The Email can't be greater than 254 characters"
            },
            "Phone_number":{
                "required":"The Phoe Number cannot be empty",
                "min_value":"The phone Numbers in India start from 6"
            },
            "Address1":{
                "required":"The Address cannot be empty",
                "max_length":"The Address cannot be greater than 500 characters"
            },
            "state":{
                "required":"The state name cannot be empty",
                "max_length":"The state name can't be greater than 30 characters"
            },
            "Password":{
                "required":"You have to create a Password",
                "min_length":"the Password should be atleast 8 characters long"
            }

        }
        



