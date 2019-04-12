from django.contrib import admin
from django.urls import path
from aplicaciones.ctr_escolar.views import index,CreateAula, UpdateAula, AulaDelete , MateriaCreate, MateriaUpdate, \
MateriaDelete, DocumentoCreate, DocumentoUpdate, DocumentoDelete, UnidadCreate, Consultas_json, UnidadDelete, \
UnidadUpdate, TareaCreate, JsonTareas, TareaDelete, TareaUpdate, BlogCreate, BolgList, BlogUpdate, BlogDelete, \
BlogDetalle, InscripcionCreate, MateriaAlumnoList, DocumentMateriaAlumnoList, BoligAlumnoList, TareaAlumnoCreate, \
ListTareaAlumno, TareaEntregadaList, TareaEntregadaUpdate, PromediarCreate, PromediarMateria, CalificacionesVer, \
ComentarioCreate, MateriaListaAlumno, DownloadExcel, ResponseMaestroAjax
app_name='control_escolar'
urlpatterns = [
    path('',index.as_view(), name='index'),
    path('maestro/crear_aula/', CreateAula.as_view(), name='maestro_create_aula'),
    path('maestro/actualizar_aula/<int:pk>', UpdateAula.as_view(), name='maestro_update_aula'),
    path('maestro/elimina_aula/<int:pk>', AulaDelete.as_view(), name='maestro_delete_aula'),

    path('maestro/materias/', MateriaCreate.as_view(), name='maestro_materias'),
    path('maestro/materias/update/<int:pk>/', MateriaUpdate.as_view(), name='maestro_materias_update'),
    path('maestro/materias/delete/<int:pk>/', MateriaDelete.as_view(), name='maestro_materias_delete'),
    path('maestro/materias/lista/<int:pk>/', MateriaListaAlumno.as_view(), name='maestro_materias_list_alumno'),

    path('maestro/materias/lista_descargar/', DownloadExcel.as_view(), name='maestro_materias_list_download'),

    path('maestro/documento/', DocumentoCreate.as_view(), name='maestro_documento'),
    path('maestro/documento/update/<int:pk>', DocumentoUpdate.as_view(), name='maestro_documento_update'),
    path('maestro/documento/delete/<int:pk>', DocumentoDelete.as_view(), name='maestro_documento_delete'),


    path('maestro/unidad/', UnidadCreate.as_view(), name='maestro_unidad'),
    path('maestro/unidad/delete', UnidadDelete.as_view(), name='maestro_unidad_delete'),
    path('maestro/unidad/update', UnidadUpdate.as_view(), name='maestro_unidad_update'),
    path('maestro/consulta/json/', Consultas_json.as_view(), name='consultas_json'),


    path('maestro/Tarea/', TareaCreate.as_view(), name='maestro_tarea_crear'),
    path('maestro/Tarea/json', JsonTareas.as_view(), name='maestro_tarea_json'),
    path('maestro/Tarea/delete/<int:pk>/', TareaDelete.as_view(), name='maestro_tarea_delete'),
    path('maestro/Tarea/update/<int:pk>/', TareaUpdate.as_view(), name='maestro_tarea_update'),

    path('maestro/blog/', BolgList.as_view(), name='maestro_blog_list'),
    path('maestro/blog/crear/', BlogCreate.as_view(), name='maestro_blog_crear'),
    path('maestro/blog/update/<int:pk>/', BlogUpdate.as_view(), name='maestro_blog_update'),
    path('maestro/blog/delete/<int:pk>/', BlogDelete.as_view(), name='maestro_blog_delete'),
    path('maestro/blog/detalle/<int:pk>/', BlogDetalle.as_view(), name='maestro_blog_detalle'),

    path('comentar/blog/<int:pk>', ComentarioCreate.as_view(), name='comentar_blog'),


    path('maestro/tarea/calificar/', TareaEntregadaList.as_view(), name='maestro_tarea_entregada_list'),
    path('maestro/tarea/entregada/<int:pk>/', TareaEntregadaUpdate.as_view(), name='maestro_tarea_entregada_update'),

    path('maestro/promediar/unidad/', PromediarCreate.as_view(), name='maestro_priomediar'),
    path('maestro/promediar/materia/', PromediarMateria.as_view(), name='maestro_priomediar_materia'),


    path('alumno/registro/', InscripcionCreate.as_view(), name='alumno_registrar'),
    path('alumno/materias/', MateriaAlumnoList.as_view(), name='alumno_materia_list'),
    path('alumno/materias/documentos/<int:pk>/', DocumentMateriaAlumnoList.as_view(), name='doc_materia_alu'),
    path('alumno/blog/', BoligAlumnoList.as_view(), name='alumno_blog'),
    path('alumno/tarea/crear/', TareaAlumnoCreate.as_view(), name='alumno_tarea_create'),

    path('alumno/tarea/script/', ListTareaAlumno.as_view(), name='alumno_tarea_scrip'),
    path('alumno/calificaciones/', CalificacionesVer.as_view(), name='alumno_calificaciones_alu'),



    path('maestro/msn/comentarios/', ResponseMaestroAjax.as_view(), name='msn_maestro_blog'),





]