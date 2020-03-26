from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class DashboardClass(View):
    templates = 'Dashboard/dashboard.html'
    def get(self,request,*args, **kwargs):
       return render(request,self.templates,{})