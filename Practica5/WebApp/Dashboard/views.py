from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class DashboardClass(LoginRequiredMixin,View):
    templates = 'Dashboard/dashboard.html'
    def get(self,request,*args, **kwargs):
       return render(request,self.templates,{})