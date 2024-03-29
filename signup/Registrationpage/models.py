from django.db import models
from django.core.validators import MinLengthValidator,MaxLengthValidator
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.
class Register(models.Model):
    Fname=models.CharField(max_length=50)
    Lname=models.CharField(max_length=50)
    Email=models.EmailField(max_length=254)
    Phone_number=models.CharField(max_length=10)
    Address1=models.CharField(max_length=500)
    state=models.CharField(max_length=30)
    Password=models.CharField(validators=[MinLengthValidator(8)],max_length=20)
    def __str__(self):
        return f'{self.Fname} {self.Lname} with email {self.Email}'
    
class Userprofile(models.Model):
    phone_number=models.CharField(max_length=10)
    Address=models.CharField(max_length=500)
    state=models.CharField(max_length=30)
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="userprofile")