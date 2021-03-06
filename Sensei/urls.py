"""Sensei URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LogoutView
from aplicaciones.usuario.views import CreateUser, PerfilList, PerfilUpdate, ChaguePasswordUser
from ajax_select import urls as ajax_select_urls
from aplicaciones.ctr_escolar.views import IngrsarView
urlpatterns = [
    path('adminsensei/', admin.site.urls), 
    path('login/',IngrsarView.as_view(), name='login'),
    path('salir/', LogoutView.as_view(template_name='logout.html'), name="salir"),
    path('', include('aplicaciones.ctr_escolar.urls'), name='index_sensei'),
    path('registro/', CreateUser.as_view(),name='registro'),
    path('perfil-usuario/', PerfilList.as_view(),name='perfil_user'),
    path('perfil-usuario/edit/<int:pk>/', PerfilUpdate.as_view(),name='perfil_user_update'),
    path('cambiar_pasworduser/', ChaguePasswordUser.as_view(),name='cambiar_password'),
    re_path(r'^ajax_select/', include(ajax_select_urls)),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 