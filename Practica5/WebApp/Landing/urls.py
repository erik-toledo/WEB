from django.urls import include, re_path,path
from django.contrib.auth import views as auth_view
from Landing.views import LandingClass
from Login.views import LoginClass

app_name = 'Landing'

urlpatterns = [
    path('',LandingClass.as_view(),name = 'landing'),
    path('Login/',LoginClass.as_view(),name = 'login')
]