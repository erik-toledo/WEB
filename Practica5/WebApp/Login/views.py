from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django

class LoginClass(View):
    template = 'Login/login.html'
    
    template_ok = 'Dashboard/dashboard.html'

    def get(self, request, *args, **kwargs ):
        if request.user.is_authenticated:
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('Dashboard:dashboard')
        return render(request, self.template,{})

    def post(self, request ,*args, **kwargs):

        user_post = request.POST['user']
        password_post = request.POST['password']

        user_session = authenticate(username = user_post, password = password_post)
        if user_session is not None:
            login_django(request, user_session)
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('Dashboard:dashboard')

        else:
            self.message = 'Usuario o contraseña incorrecto'
        return render(request, self.template, self.get_Context())
    
    def get_Context(self):
        return{
            'error': self.message
        }




