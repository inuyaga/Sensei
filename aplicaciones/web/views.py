from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from aplicaciones.ctr_escolar.models import Blog
from aplicaciones.web.models import Blog as BlogWeb, Categoria
from django.db.models import Count
class IndexView(TemplateView):
    template_name = "inicio/inicio.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs']=BlogWeb.objects.all().order_by('blog_creado')[:3] 
        return context

class DocumentacionListView(ListView):   
    model = BlogWeb
    paginate_by = 15
    template_name = "inicio/list_documentation.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['blog']=BlogWeb.objects.first()
    #     context['blogs']=BlogWeb.objects.all()
    #     return context 

class DocumentacionViewPost(DetailView):  
    model = BlogWeb
    template_name = "inicio/documentacion.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs']=BlogWeb.objects.all().order_by('blog_ultima_actualizacion')[:6]
        context['categoria']=BlogWeb.objects.values('blog_categoria', 'blog_categoria__cat_nombre').annotate(count_blog=Count('blog_id')).order_by('blog_categoria')
        return context
    


class LoginView(LoginView):
    success_url = reverse_lazy('ctr:dasboard')
    template_name='login_sensei.html'

class LogoutView(LogoutView):
    template_name='logout.html'