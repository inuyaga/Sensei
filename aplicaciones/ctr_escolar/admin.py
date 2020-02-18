from django.contrib import admin
from aplicaciones.ctr_escolar.models import Aula, Blog, CalificacionMateria, CalificacionUnidad, ComentarioBlog, Documento, Materia, Tarea

# Register your models here.
admin.site.register(Aula)
admin.site.register(Blog)
admin.site.register(CalificacionMateria)
admin.site.register(CalificacionUnidad)
admin.site.register(ComentarioBlog)
admin.site.register(Documento)
admin.site.register(Materia)
admin.site.register(Tarea)