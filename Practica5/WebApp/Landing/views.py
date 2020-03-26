from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class LandingClass(View):
    templates = 'Landing/landing.html'
    def get(self,request,*args, **kwargs):
       return render(request,self.templates,{})