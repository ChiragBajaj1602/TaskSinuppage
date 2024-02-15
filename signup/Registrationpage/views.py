from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import SignupForm
# Create your views here.
class homePage(View):
    def get(self,request):
        form = SignupForm()
        return render(request,'Registrationpage/index.html',{
            'form':form
        })
    def post(self,request):
        print("in the post method")
        form=SignupForm(request.POST)
        print("reached the line 14")
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>The form is submitted</h1>")
        else:
            form=SignupForm()
        return render(request,'Registrationpage/index.html',{
            'form':form
        })