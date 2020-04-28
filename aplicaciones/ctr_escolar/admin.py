from django.contrib import admin
from aplicaciones.ctr_escolar.models import *

# Register your models here.
class AulaConfig(admin.ModelAdmin):
    list_display = (
        'aula_nombre',
        'aula_pertenece',
        'aula_creacion',
    )
    raw_id_fields = ['aula_pertenece']
    search_fields = (
        'aula_nombre',
        'aula_pertenece',
        )
class BlogConfig(admin.ModelAdmin):
    list_display = (
        'blog_titulo',
        'blog_descripcion',
        'blog_pertenece',
    )
    raw_id_fields = ['blog_pertenece', 'blog_materia']
    search_fields = (
        'blog_pertenece', 
        'blog_materia',
        )
class TareaConfig(admin.ModelAdmin):
    list_display = (
        'tarea_nombre',
        'tarea_descripcion',
        'tarea_fecha_inicio',
        'tarea_fecha_termino',
        'tarea_tipo',
        'tarea_porcentaje',
        'tarea_unidad',
    )
    list_filter = (
        'tarea_fecha_inicio',
        'tarea_fecha_termino',
        'tarea_tipo',
        'tarea_unidad',
    )
    search_fields = (
        'tarea_nombre', 
        'tarea_unidad',
        )

class TareaDocumentoConfig(admin.ModelAdmin):
    list_display = (
        'tareaDocumento_creado',
        'tareaDocumento_pertenece',
        'tareaDocumento_Tarea',
        'tareaDocumento_status',
        'tareaDocumento_calificacion',
    )
    raw_id_fields = ['tareaDocumento_pertenece', 'tareaDocumento_Tarea']
    search_fields = (
        'tareaDocumento_pertenece__username',
        'tareaDocumento_Tarea__tarea_nombre',
        )
    list_filter = ['tareaDocumento_status', 'tareaDocumento_creado', 'tareaDocumento_Tarea__tarea_tipo']



class RespuestaExamenConfig(admin.ModelAdmin):
    list_display = (
        're_reactivo',
        're_alumno',
        're_ok',
        're_text',
    )
    list_filter = (
        're_alumno',
    )


admin.site.register(Aula, AulaConfig)
admin.site.register(Blog, BlogConfig)
# admin.site.register(CalificacionMateria)
# admin.site.register(CalificacionUnidad)
admin.site.register(ComentarioBlog)
admin.site.register(Documento)
admin.site.register(Materia)
admin.site.register(Tarea, TareaConfig) 
admin.site.register(TareaDocumento, TareaDocumentoConfig)
admin.site.register(Reactivo)
admin.site.register(EleccionReactivo)
admin.site.register(RespuestaExamen, RespuestaExamenConfig)