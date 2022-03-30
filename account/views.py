from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views import generic
from django.contrib.auth.views import LoginView, LogoutView
# Create your views here.


class RegisterView(generic.CreateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'password']
    template_name = 'account/register.html'
    success_url = reverse_lazy('home')


class CustomLoginView(LoginView):
    template_name = 'account/login.html'
    success_url = reverse_lazy('home')


class CustomLogoutView(LogoutView):
    pass
