from django.urls import include, re_path,path
from django.contrib.auth import views as auth_view
from Registro.views import RegistrateView

app_name = 'Registro'

urlpatterns = [
    path('',RegistrateView.as_view(),name = 'registro'),  
]