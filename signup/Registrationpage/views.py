from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views import View
from .forms import SignupForm,siginform
from .models import Register
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
            form.save()
            return HttpResponseRedirect('login')
        else:
            form=SignupForm()
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
        form = siginform(request.POST)
        if form.is_valid():
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            # We have fetched the email we will check the db 
            # that if it exists or not
            try:
                user1=Register.objects.get(Email=email)
            except Register.DoesNotExist:
                print("Invalid email")
                return HttpResponseRedirect('login')
            if user1.Password == password:
                return HttpResponse("<h1>The Login is Successful</h1>")
            else:
                return HttpResponseRedirect('login')
        else:
            form = siginform()
            return render(request,'Registrationpage/login.html',{
                'form':form
            })

