from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
class IndexView(TemplateView):
    template_name = "inicio/inicio.html"


class LoginView(LoginView):
    success_url = reverse_lazy('ctr:dasboard')
    template_name='login_sensei.html'

class LogoutView(LogoutView):
    template_name='logout.html'