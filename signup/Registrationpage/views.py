from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views import View
from .forms import SignupForm,siginform
from .forms1 import UserProfileForm,otherdetailform,combinedformset
from .models import Register
from django.contrib import messages
import re
from django.views.generic.edit import FormView
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
            pass
            
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
            return HttpResponse("<h1>Login is Success</h1>")
        else:
            pass
        return render(request,'Registrationpage/login.html',{
            'form':form
        })

class signupapgeusingauth(FormView):
    form_class=UserProfileForm
    template_name='Registrationpage/index.html'
    success_url='/login'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class MyFormView(FormView):
    template_name = 'Registrationpage/index.html'
    form_class = UserProfileForm
    success_url = '/login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(combinedformset(self.request.POST), "1111111111111111111")
        if self.request.POST:
            context['formset'] = combinedformset(self.request.POST)
            
        else:
            context['formset'] = combinedformset()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            print("the form is invalid")
            return self.render_to_response(self.get_context_data(form=form,formset=combinedformset))



