from django.contrib import admin 
from django.urls import path
from aplicaciones.web import views as web_views
app_name='web'
urlpatterns = [
    path('',web_views.IndexView.as_view(), name='index'),
]