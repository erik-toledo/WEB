from django.urls import include, re_path,path
from django.contrib.auth import views as auth_view
from Login.views import LoginClass
#from Dashboard.views import DashboardClass

app_name = 'Login'

urlpatterns = [
    path('Login/',LoginClass.as_view(),name = 'login'),
    #path('Dashboard', DashboardClass.as_view(),name = 'dashboard'),
    
]