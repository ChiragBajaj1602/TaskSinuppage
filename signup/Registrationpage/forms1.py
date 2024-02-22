from django import forms
from django.contrib.auth.models import User
from .models import Userprofile
import re
from django.forms.models import inlineformset_factory
def validateEmail(email):
    try:
        dbemail= User.objects.filter(email=email)[0]
        return False
    except:
        return True
def validate_password(password):
    pattern=r'^(?=.*[A-Z])(?=.*\d)(?=.*[^a-zA-Z0-9]).{8,}$'
    return bool(re.match(pattern,password))
def validatephone(phonenumber):
    pattern = r'^\d{10}$'
    return bool(re.match(pattern,phonenumber))
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'date_joined']
        labels = {
            'username':"Enter a unique username",
            'first_name': "Enter Your First Name",
            'last_name': "Enter Your Last Name",
            'email': "Enter your Email",
            'date_joined': "Enter the date joined",
            'password': "Create a Strong Password"
        }
        widgets = {
            'password': forms.PasswordInput()
        }
    def clean(self):
        cleaned_data=super().clean()
        email=cleaned_data.get('email')
        if not validateEmail(email):
            raise forms.ValidationError({'email':"The Email already exists"})
        password=cleaned_data.get('password')
        if password and not validate_password(password):
            raise forms.ValidationError({'password':"Password must be atleast 8 chracters long one upper case character and one lower case character and one digit atleast"})
        return cleaned_data
            
class otherdetailform(forms.ModelForm):
    class Meta:
        model =Userprofile
        fields=['phone_number','Address','state']
        labels={
            'phone_number':"Enter a Phone Number",
            'Address':"Enter your Address",
            'state':"Enter name of your state",
        }
    def clean(self):
        cleaned_data=super().clean()
        phone_number=cleaned_data.get('phone_number')
        print(phone_number)
        if not validatephone(phone_number):
            raise forms.ValidationError({'phone_number':"There should 10 digits in the phone number"})
        return cleaned_data

    


combinedformset=inlineformset_factory(User,Userprofile,form=UserProfileForm,fields=['phone_number','Address','state'],can_delete=False,max_num=1,extra=1)
        