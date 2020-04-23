from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from aplicaciones.ctr_escolar.models import Blog
class IndexView(TemplateView):
    template_name = "inicio/inicio.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs']=Blog.objects.all().order_by('blog_creado')[:3]
        return context
    


class LoginView(LoginView):
    success_url = reverse_lazy('ctr:dasboard')
    template_name='login_sensei.html'

class LogoutView(LogoutView):
    template_name='logout.html'