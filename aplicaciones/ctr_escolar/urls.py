from django.contrib import admin 
from django.urls import path
from aplicaciones.ctr_escolar import views as view_ctr
app_name='ctr'
urlpatterns = [
    path('dashboard1',view_ctr.index.as_view(), name='index'),
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





    #Nuevas urls
    path('dashboard/', view_ctr.AdminIndex.as_view(), name='dasboard'),    
    path('aula/list/', view_ctr.AulaList.as_view(), name='list_aula'),   
    path('aula/create/', view_ctr.AulaCreateView.as_view(), name='aula_crear'),   
    path('aula/update/<int:pk>/', view_ctr.AulaUpdateView.as_view(), name='aula_update'),   
    path('aula/delete/<int:pk>/', view_ctr.AulaDeleteView.as_view(), name='aula_delete'),   

    path('materia/list/', view_ctr.MateriaListView.as_view(), name='materia_list'),    
    path('materia/create/', view_ctr.MateriaCreateView.as_view(), name='materia_create'),    
    path('materia/update/<int:pk>/', view_ctr.MateriaUpdateView.as_view(), name='materia_update'),    
    path('materia/delete/<int:pk>/', view_ctr.MateriaDeleteView.as_view(), name='materia_delete'),    
    path('materia/recurso/list/', view_ctr.RecursosMateriaView.as_view(), name='materia_recurso_new'),    
    path('materia/recurso/crear/', view_ctr.DocumentoCreateView.as_view(), name='materia_recurso_create'),    
    path('materia/recurso/delete/<int:pk>/', view_ctr.RecursoDelete.as_view(), name='materia_recurso_dell'),   


    path('materia/unidades/list/<int:id_materia>/', view_ctr.UnidadesList.as_view(), name='materia_unidad'),    
    path('materia/unidades/create/<int:id_materia>/', view_ctr.UnidadCreateView.as_view(), name='materia_unidad_create'),    
    path('materia/unidades/update/<int:pk>/<int:id_materia>/', view_ctr.UnidadUpdateView.as_view(), name='materia_unidad_update'),    
    path('materia/unidades/delete/<int:pk>/<int:id_materia>/', view_ctr.UnidadDeleteView.as_view(), name='materia_unidad_delete'),    

    path('materia/unidades/tareas/list/<int:id_materia>/<int:id_unidad>/', view_ctr.TareaListView.as_view(), name='unidad_tareas'),     
    path('materia/unidades/tareas/create/<int:id_materia>/<int:id_unidad>/', view_ctr.TareaCreateView.as_view(), name='tarea_crear'),    
    path('materia/unidades/tareas/delete/<int:pk>/<int:id_materia>/<int:id_unidad>/', view_ctr.TareaDeleteView.as_view(), name='tarea_delete'),    
    path('materia/unidades/tareas/update/<int:pk>/<int:id_materia>/<int:id_unidad>/', view_ctr.TareaUpdateView.as_view(), name='tarea_update'),    
    path('materia/unidades/tareas/copiar/<int:id_tarea>', view_ctr.TareaCopiarExamenView.as_view(), name='tarea_copy'),    
    path('materia/unidades/tareas/copiar/unidad/<int:id_materia>/<int:id_tarea>', view_ctr.TareaCopiarExamenUnidadView.as_view(), name='tarea_copy_unidad'),    
    path('materia/unidades/tareas/copiar/detalle/<int:id_unidad>/<int:id_tarea>', view_ctr.DetalleCopiadoExamenView.as_view(), name='tarea_copy_detail'),    

    
    path('materia/unidades/tareas/calificar/<int:id_tarea>/', view_ctr.CalificarTareaListView.as_view(), name='calificar_tarea'),    
    path('materia/unidades/tareas/calificar/<int:pk>/form/', view_ctr.TareaDocumentoUpdateView.as_view(), name='tarea_update'),    
    path('materia/unidades/tareas/calificar/<int:pk>/delete/', view_ctr.TareaDocumentoDeleteView.as_view(), name='docu_delete'),    
    path('materia/unidades/promediar/<int:id_unidad>/', view_ctr.PromediarUnidadAlumnosView.as_view(), name='promediar_unidad'),    
    path('materia/unidades/promediar/detalle/alumno/<int:id_alumno>/<int:id_unidad>/', view_ctr.DetalleAlumnoUnidadTareas.as_view(), name='detalle_alumno'),    
    path('materia/promediar/alumnos/<int:id_materia>/', view_ctr.PromediarMateriaAlumnoView.as_view(), name='materia_promediar'),     

    path('Blog/List/', view_ctr.BlogListView.as_view(), name='blog_list'),    
    path('Blog/crear/', view_ctr.BlogCreateView.as_view(), name='blog_crear'),    
    path('Blog/leer/<int:pk>/', view_ctr.BlogLerrView.as_view(), name='blog_leer'),    
    path('Blog/update/<int:pk>/', view_ctr.BlogEditarView.as_view(), name='blog_update'),    
    path('Blog/delete/<int:pk>/', view_ctr.BlogDeleteView.as_view(), name='blog_delete'),    

    # path('Examen/list/<int:id_unidad>/', view_ctr.ExamenListView.as_view(), name='examen_listar'),     
    # path('Examen/crear/<int:id_unidad>/', view_ctr.ExamenCreateView.as_view(), name='examen_crear'),     
    # path('Examen/update/<int:pk>/<int:id_unidad>/', view_ctr.ExamenUpdateView.as_view(), name='examen_update'),     
    # path('Examen/delete/<int:pk>/<int:id_unidad>/', view_ctr.ExamenDeleteView.as_view(), name='examen_delete'),   

    path('rectivo/listar/<int:id_tarea>/', view_ctr.ReactivoListView.as_view(), name='reactivo_list'),     
    path('rectivo/update/<int:pk>/<int:id_tarea>/', view_ctr.ReactivoUpdateView.as_view(), name='reactivo_update'),     
    path('rectivo/delete/<int:pk>/<int:id_tarea>/', view_ctr.ReactivoDeleteView.as_view(), name='reactivo_delete'),      
    path('rectivo/eleccion/list/<int:id_reactivo>/', view_ctr.ItemReactivoListView.as_view(), name='eleccion_list'),   


    path('alumno/blogs/list/', view_ctr.BoligAlumnoListView.as_view(), name='al_blog'),     
    path('alumno/materia/list/', view_ctr.MateriaAlumnoListView.as_view(), name='al_materia'),     
    path('alumno/materia/inscribir/', view_ctr.InscripcionAlumnoCreateView.as_view(), name='al_inscribir'),     
    path('alumno/materia/recursos/<int:pk>/', view_ctr.RecursosMateriaListAlumno.as_view(), name='al_recurso'),     
    path('alumno/materia/unidad/tareas/<int:id_unidad>', view_ctr.TareasListViewAlumno.as_view(), name='al_tareas'),   

    path('alumno/materia/unidad/tareas/entrega/<int:id_unidad>/<int:id_tarea>/', view_ctr.EntrgaTareaAlumnoView.as_view(), name='al_tareas_create'),      
    path('alumno/materia/unidad/tareas/delete/<int:pk>/<int:id_unidad>/', view_ctr.EntrgaTareaAlumnoViewDelete.as_view(), name='al_tareas_delete'),      
    path('alumno/materia/unidad/tareas/examen/respuesta/<int:id_examen>/', view_ctr.RespuestaExamenAlumnoView.as_view(), name='al_examen'),      

]