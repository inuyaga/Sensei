
from django.urls import path
from aplicaciones.apirest import views as web_views
from rest_framework.authtoken import views as tokenview
app_name='apirest' 
urlpatterns = [
    path('v1/app/login/', web_views.AutenticacionUser.as_view(), name='login'),  
    path('v1/app/aula/docente', web_views.GetAulaMaestro.as_view(), name='aulas'),  
    path('v1/app/aula/delete/<int:id>/', web_views.DeleteAulaMaestro.as_view(), name='aulas_delete'),  
    path('v1/app/materias/<int:idaula>/', web_views.MateriasMateriasView.as_view(), name='materias'),  
]