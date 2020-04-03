from django.urls import include, re_path,path
from django.contrib.auth import views as auth_view
from Login.views import LoginClass

app_name = 'Login'

urlpatterns = [
    path('',LoginClass.as_view(),name = 'login'),  
]