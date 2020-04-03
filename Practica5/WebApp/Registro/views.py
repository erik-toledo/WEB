from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from Registro.forms import Registro

class RegistrateView(FormView):
    template_name = 'Registro/registroUsuario.html'

    def get(self, request, *args, **kwargs):
        form = Registro(request.GET or None)
        context = {
        'obt' : form
        }
        return render(request, self.template_name, context)

    # POST
    def post(self, request, *args, **kwargs):
        form = Registro(request.POST or None)
        if form.is_valid():
            self.object = form.save(commit = False)
            self.object.set_password(self.object.password)
            self.object.save()
        return redirect('Login:login')
