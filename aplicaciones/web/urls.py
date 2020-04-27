from django.contrib import admin 
from django.urls import path
from aplicaciones.web import views as web_views
from aplicaciones.usuario.views import CreateUser
app_name='web'
urlpatterns = [
    path('',web_views.IndexView.as_view(), name='index'),
    path('documentacion/',web_views.DocumentacionListView.as_view(), name='documentacion'),
    path('documentacion/view/<int:pk>/',web_views.DocumentacionViewPost.as_view(), name='documentacion_view_post'),
    path('login/',web_views.LoginView.as_view(), name='login'),
    path('salir/', web_views.LogoutView.as_view(), name="salir"), 
    path('registro/', CreateUser.as_view(),name='registro'),
]