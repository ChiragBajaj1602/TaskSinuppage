from django import forms
from .models import Register
import re
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Register
def validate_password(password):
    pattern=r'^(?=.*[A-Z])(?=.*\d)(?=.*[^a-zA-Z0-9]).{8,}$'
    return bool(re.match(pattern,password))
def validatephone(phonenumber):
    pattern = r'^\d{10}$'
    return bool(re.match(pattern,phonenumber))
def validateEmail(email):
    try:
        dbemail= Register.objects.get(Email=email)
    except:
        return True
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
    def clean(self):
        cleaned_data = super().clean()
        phone_number = cleaned_data.get('Phone_number')
        email=cleaned_data.get('Email')
        if not validateEmail(email):
            raise forms.ValidationError({'Email':"The Email already exists"})
        if not validatephone(phone_number):
            raise forms.ValidationError({'Phone_number':"The Phone number must be 10 characters long and there must be no characters"})
        password=cleaned_data.get('Password')
        if not validate_password(password):
            raise forms.ValidationError({'Password':"Password must be atleast 8 chracters long one upper case character and one lower case character and one digit atleast"})
        return cleaned_data

def checkforuser(email):
    try:
        user1=Register.objects.get(Email=email)
        return True
    except:
        return False

class siginform(forms.ModelForm):
    class Meta:
        model=Register
        fields=['Email','Password']
        labels={
            'Email':"Enter your Registered Email",
            'Password':"Enter your Password"
        }
    def clean(self):
        cleaned_data=super().clean()
        email=cleaned_data.get('Email')
        if checkforuser(email):
            user1=Register.objects.get(Email=email)
            user1passcode=user1.Password
            passcode=cleaned_data.get('Password')
            if passcode==user1passcode:
                pass
            else:
                raise forms.ValidationError({'Password':"Password for the given mail is invalid"})
        else:
            raise forms.ValidationError({'Email':"The email is not registered"})
        return cleaned_data
    





