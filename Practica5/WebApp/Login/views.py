from django.shortcuts import render, redirect
from django.views.generic import View


from django.contrib.auth import authenticate

class LoginClass(View):
    template = 'Login/login.html'
    
    template_ok = 'Dashboard/dashboard.html'

    def get(self, request, *args, **kwargs ):
        return render( request,self.template,{})

    def post(self, request ,*args, **kwargs):

        user_post = request.POST['user']
        password_post = request.POST['password']

        user_session = authenticate(username = user_post, password = password_post)

        if user_session is  None:
          self.messsage = "Usuario y Contraseña no validos" 
        else:
            return redirect('xx:dashboard')

        return render(request,self.template,self.get_Context())
    def get_Context(self):
        return{
            'error': self.messsage
        }

# class LandingClass(View):
#     templates = 'Landing/landing.html'
#     def get(self,request,*args, **kwargs):
#        return render(request,self.templates,{})

# class DashboardClass(View):
#     templates = 'Dashboard/dashboard.html'
#     def get(self,request,*args, **kwargs):
#        return render(request,self.templates,{})



