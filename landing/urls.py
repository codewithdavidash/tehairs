from django.contrib.auth.views import LoginView
from django.urls import path
from . import views
from .forms import (
    LoginForm,
)

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/register/', views.register, name='register'),
    path('accounts/login/', LoginView.as_view(template_name='auth/login.html',
         authentication_form=LoginForm), name='login'),
    path('accounts/logout/', views.logoutView, name='logout'),
    path('accounts/logoutPage/', views.logoutPage, name='logoutPage'),
]
