from django.contrib import admin
from .models import Register,Userprofile
from django.contrib.auth.models import User
admin.site.register(Register)
admin.site.register(Userprofile)