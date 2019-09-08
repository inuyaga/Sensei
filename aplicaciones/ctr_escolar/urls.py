from django.contrib import admin 
from django.urls import path
from aplicaciones.ctr_escolar import views as view_ctr
app_name='control_escolar'
urlpatterns = [
    path('',view_ctr.index.as_view(), name='index'),
    path('maestro/crear_aula/', view_ctr.CreateAula.as_view(), name='maestro_create_aula'),
    path('maestro/actualizar_aula/<int:pk>', view_ctr.UpdateAula.as_view(), name='maestro_update_aula'),
    path('maestro/elimina_aula/<int:pk>', view_ctr.AulaDelete.as_view(), name='maestro_delete_aula'),

    path('maestro/materias/', view_ctr.MateriaCreate.as_view(), name='maestro_materias'),
    path('maestro/materias/update/<int:pk>/', view_ctr.MateriaUpdate.as_view(), name='maestro_materias_update'),
    path('maestro/materias/delete/<int:pk>/', view_ctr.MateriaDelete.as_view(), name='maestro_materias_delete'),
    path('maestro/materias/lista/<int:pk>/', view_ctr.MateriaListaAlumno.as_view(), name='maestro_materias_list_alumno'),

    path('maestro/materias/lista_descargar/', view_ctr.DownloadExcel.as_view(), name='maestro_materias_list_download'),

    path('maestro/documento/', view_ctr.DocumentoCreate.as_view(), name='maestro_documento'),
    path('maestro/documento/update/<int:pk>', view_ctr.DocumentoUpdate.as_view(), name='maestro_documento_update'),
    path('maestro/documento/delete/<int:pk>', view_ctr.DocumentoDelete.as_view(), name='maestro_documento_delete'),


    path('maestro/unidad/', view_ctr.UnidadCreate.as_view(), name='maestro_unidad'),
    path('maestro/unidad/delete', view_ctr.UnidadDelete.as_view(), name='maestro_unidad_delete'),
    path('maestro/unidad/delete/detalle/<int:pk>/', view_ctr.UnidadDeleteView.as_view(), name='maestro_unidad_delete_detalle'),
    path('maestro/unidad/update', view_ctr.UnidadUpdate.as_view(), name='maestro_unidad_update'), 
    path('maestro/consulta/json/', view_ctr.Consultas_json.as_view(), name='consultas_json'),
 

    path('maestro/Tarea/', view_ctr.TareaCreate.as_view(), name='maestro_tarea_crear'), 
    path('maestro/Tarea/json', view_ctr.JsonTareas.as_view(), name='maestro_tarea_json'),
    path('maestro/Tarea/delete/<int:pk>/', view_ctr.TareaDelete.as_view(), name='maestro_tarea_delete'),
    path('maestro/Tarea/update/<int:pk>/', view_ctr.TareaUpdate.as_view(), name='maestro_tarea_update'), 
    path('maestro/Tarea/updateCamio/<int:pk>/<int:id_unidad>/', view_ctr.TareaUpdateChangue.as_view(), name='maestro_tarea_updateChangue'), 

    path('maestro/blog/', view_ctr.BolgList.as_view(), name='maestro_blog_list'),
    path('maestro/blog/crear/', view_ctr.BlogCreate.as_view(), name='maestro_blog_crear'),
    path('maestro/blog/update/<int:pk>/', view_ctr.BlogUpdate.as_view(), name='maestro_blog_update'),
    path('maestro/blog/delete/<int:pk>/', view_ctr.BlogDelete.as_view(), name='maestro_blog_delete'),
    path('maestro/blog/detalle/<int:pk>/', view_ctr.BlogDetalle.as_view(), name='maestro_blog_detalle'),

    path('comentar/blog/<int:pk>', view_ctr.ComentarioCreate.as_view(), name='comentar_blog'),  


    path('maestro/select/aula/', view_ctr.SelectAula.as_view(), name='select_aula_master'),
    path('maestro/select/<int:aula>/materia/', view_ctr.SelectMateria.as_view(), name='select_materia_master'),
    path('maestro/select/aula/<int:materia>/unidad', view_ctr.SelectUnidad.as_view(), name='select_unidad_master'),
    path('maestro/select/aula/materia/<int:unidad>', view_ctr.SelectTarea.as_view(), name='select_tarea_master'), 

    path('maestro/tarea/calificar/<int:id_tarea>', view_ctr.TareaEntregadaList.as_view(), name='maestro_tarea_entregada_list'),
    path('maestro/tarea/entregada/<int:pk>/<int:id_tarea>/', view_ctr.TareaEntregadaUpdate.as_view(), name='maestro_tarea_entregada_update'),
 
    path('maestro/promediar/unidad/', view_ctr.PromediarCreate.as_view(), name='maestro_priomediar'), 
    path('maestro/promediar/unidad/xls/', view_ctr.PromedioUnidadDetalle_xls.as_view(), name='maestro_priomediar_unidad_xls'), 
    path('maestro/promd/unidad/', view_ctr.PromediarUnidad.as_view(), name='maestro_priomediar_set'), 
    path('maestro/promediar/materia/', view_ctr.PromediarMateria.as_view(), name='maestro_priomediar_materia'),


    path('alumno/registro/', view_ctr.InscripcionCreate.as_view(), name='alumno_registrar'),
    path('alumno/materias/', view_ctr.MateriaAlumnoList.as_view(), name='alumno_materia_list'),
    path('alumno/materias/documentos/<int:pk>/', view_ctr.DocumentMateriaAlumnoList.as_view(), name='doc_materia_alu'),
    path('alumno/blog/', view_ctr.BoligAlumnoList.as_view(), name='alumno_blog'),
    path('alumno/tarea/crear/', view_ctr.TareaAlumnoCreate.as_view(), name='alumno_tarea_create'),

    path('alumno/tarea/script/', view_ctr.ListTareaAlumno.as_view(), name='alumno_tarea_scrip'),
    path('alumno/calificaciones/', view_ctr.CalificacionesVer.as_view(), name='alumno_calificaciones_alu'),



    path('maestro/msn/comentarios/', view_ctr.ResponseMaestroAjax.as_view(), name='msn_maestro_blog'),

    path('maestro/get/materias/', view_ctr.MateriaGet.as_view(), name='get_materias'), 


]