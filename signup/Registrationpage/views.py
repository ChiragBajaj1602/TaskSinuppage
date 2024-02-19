from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views import View
from .forms import SignupForm,siginform
from .models import Register
from django.contrib import messages
import re
# Create your views here.
class homePage(View):
    def get(self,request):
        form = SignupForm()
        return render(request,'Registrationpage/index.html',{
            'form':form
        })
    def post(self,request):
        form=SignupForm(request.POST)
        if form.is_valid():
            print("The registration page is validated")
            form.save()
            return HttpResponseRedirect('login')
        else:
            form=SignupForm()
            print("The registrtaion page is invalid in the post view of signup page")
        return render(request,'Registrationpage/index.html',{
            'form':form
        })

class login(View):
    def get(self,request):
        form = siginform()
        return render(request,'Registrationpage/login.html',{
            'form':form
        })
    def post(self,request):
        print("In the post view")
        form = siginform(request.POST)
        if form.is_valid():
            print("The login page is valid")
            return HttpResponse("<h1>Login is Success</h1>")
        else:
            form = siginform()
        return render(request,'Registrationpage/login.html',{
            'form':form
        })

