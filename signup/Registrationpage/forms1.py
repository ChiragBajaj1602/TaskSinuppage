from django import forms
from django.contrib.auth.models import User
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'date_joined']
        labels = {
            'first_name': "Enter Your First Name",
            'last_name': "Enter Your Last Name",
            'email': "Enter your Email",
            'date_joined': "Enter the date joined",
            'password': "Create a Strong Password"
        }
        widgets = {
            'password': forms.PasswordInput()
        }
