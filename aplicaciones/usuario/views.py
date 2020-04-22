from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView
# from aplicaciones.usuario.models import User
from aplicaciones.usuario.forms import UserForm, UserFormEdit, UserFormUpdatePassForm
from aplicaciones.usuario.models import User
from django.contrib.auth.admin import UserAdmin
from aplicaciones.ctr_escolar.models import TareaDocumento, Tarea
from django.contrib.auth.views import PasswordChangeView, PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.
class CreateUser(CreateView):
    model = UserAdmin
    form_class = UserForm
    template_name = 'registrar.html'
    success_url = reverse_lazy('web:login')
    def form_valid(self, form):
        instancia = form.save(commit=False)
        if form.data['tipo_de_usuario'] == '1':
            instancia.is_maestro=True
            
        elif form.data['tipo_de_usuario'] == '2':
            instancia.is_alumno=True
            
        instancia.save()
        return super(CreateUser, self).form_valid(form)

class PerfilList(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = User
    template_name = 'perfil_user.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class PerfilUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = User
    form_class = UserFormEdit
    template_name = 'admin/actualiza_perfil.html'
    success_url = reverse_lazy('perfil_user')

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            if self.request.user.id != self.kwargs.get('pk'):
                return redirect('/')
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
       
        return context

class ChaguePasswordUser(LoginRequiredMixin, PasswordChangeView): 
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = User
    form_class = UserFormUpdatePassForm
    template_name = 'changuepassword.html'
    success_url = '/perfil-usuario/'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        return context

