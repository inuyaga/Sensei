from django.db import models
from django.contrib.auth import get_user_model
Usuario = get_user_model()

# Create your models here.
class Aula(models.Model):
    aula_nombre = models.CharField('Nombre', max_length=50)
    aula_pertenece = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    aula_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.aula_nombre 
class Documento(models.Model):
    doc_id=models.AutoField(primary_key=True)
    doc_nombre = models.CharField('Nombre', max_length=100)
    doc_pertenece = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    doc_archivo=models.FileField('archivo', upload_to='documentos_meteria/')
    def __str__(self):
        return self.doc_nombre

class Materia(models.Model):
    materia_id = models.AutoField(primary_key=True)
    materia_aula=models.ForeignKey(Aula, verbose_name='Aula', on_delete=models.CASCADE)
    materia_nombre = models.CharField('Nombre', max_length=150)
    materia_archivos=models.ManyToManyField(Documento, verbose_name="Archivos", blank=True, null=True)
    materia_registro_alumnnos=models.ManyToManyField(Usuario, verbose_name="Registro_materia")
    materia_creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.materia_nombre



class Unidad(models.Model):
    unidad_id=models.AutoField(primary_key=True)
    unidad_nombre=models.CharField('Nombre', max_length=500)
    unidad_materia=models.ForeignKey(Materia, verbose_name='Materia', on_delete=models.CASCADE)
    def __str__(self):
        return self.unidad_nombre

class Tarea(models.Model):
    tarea_id=models.AutoField(primary_key=True)
    tarea_nombre = models.CharField('Nombre', max_length=400)
    tarea_descripcion = models.CharField('Descripcion', max_length=800)
    tarea_fecha_inicio = models.DateField('Fecha de inicio')
    tarea_fecha_termino = models.DateField('Fecha de Final')
    TIPO_TAREA=(('ENTREGA', 'ENTREGA'), ('PARA CALIFICAR','PARA CALIFICAR'))
    tarea_tipo=models.CharField('Tipo de tarea', max_length=20, choices=TIPO_TAREA)
    tarea_unidad=models.ForeignKey(Unidad, verbose_name='Unidad', on_delete=models.CASCADE)
    def __str__(self):
        return self.tarea_nombre


class TareaDocumento(models.Model):
    tareaDocumento_id=models.AutoField(primary_key=True)
    tareaDocumento_archivo=models.FileField('Archivo', upload_to='documentos_tareas/')
    tareaDocumento_comentario_alumno=models.CharField('Comentario Alumno', max_length=500)
    tareaDocumento_comentario_maestro=models.CharField('Comentario Maestro', max_length=500, null=True, blank=True)
    tareaDocumento_creado=models.DateTimeField('Creado', auto_now_add=True)
    tareaDocumento_pertenece=models.ForeignKey(Usuario, verbose_name='Pertenece a', on_delete=models.CASCADE)
    tareaDocumento_Tarea=models.ForeignKey(Tarea, verbose_name='Tarea', on_delete=models.CASCADE)
    tareaDocumento_status=models.BooleanField('Status Tarea', default=False)
    tareaDocumento_calificacion=models.FloatField('Calificación', null=True, blank=True)
    tareaDocumento_actualizado=models.DateTimeField(auto_now=True)


    class Meta:
        unique_together = (("tareaDocumento_pertenece", "tareaDocumento_Tarea"),)
        ordering = ['-tareaDocumento_actualizado']

    def __str__(self):
        return str(self.tareaDocumento_id)

class Blog(models.Model):
    blog_id=models.AutoField(primary_key=True)
    blog_titulo =models.CharField('Titulo', max_length=250)
    blog_descripcion =models.CharField('Descripcion', max_length=500)
    blog_contenido=models.TextField('Contenido', blank=True, null=True)
    blog_imagen = models.ImageField('Imagen Blog', upload_to='img_blogs/')
    blog_creado=models.DateTimeField('Creado en', auto_now_add=True)
    blog_ultima_actualizacion=models.DateTimeField('Ultima Actualizacion', auto_now=True)
    blog_pertenece=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    blog_materia=models.ManyToManyField(Materia, verbose_name="Relacionar")

    def __str__(self):
        return self.blog_titulo

class ComentarioBlog(models.Model):
    comentario_blogID=models.AutoField(primary_key=True)
    comentario_comentario=models.TextField('Deje aqui su comentario')
    comentario_blog=models.ForeignKey(Blog, verbose_name='ID Blog', on_delete=models.CASCADE)
    comentario_creado=models.DateTimeField('Creado', auto_now_add=True)
    comentario_comentado_by=models.ForeignKey(Usuario, verbose_name='Comentado por', on_delete=models.CASCADE)




class CalificacionUnidad(models.Model):
    calU_id=models.AutoField(primary_key=True)
    calU_Materia_nombre = models.CharField('Materia', max_length=500)
    calU_unidadNombre=models.CharField('Unidad', max_length=600)
    calU_unidadID=models.IntegerField("Unidad id")
    calU_materiaID=models.IntegerField("Materia id")
    calU_calificacion=models.FloatField()
    calU_entrego=models.CharField('Entrego', max_length=50)
    calU_falta_calificar=models.CharField('Falta Calificar', max_length=50, default='no')
    calU_pertenece=models.ForeignKey(Usuario, verbose_name='Usuario', on_delete=models.CASCADE)

class CalificacionMateria(models.Model):
    calM_id=models.AutoField(primary_key=True)
    calM_nombre_materia=models.CharField('Materia Nombre', max_length=400)
    calM_materiaID=models.CharField('Materia Nombre', max_length=400)
    calM_calificacionFinal=models.FloatField('Calificación')
    calM_alumno=models.ForeignKey(Usuario, verbose_name='alumno', on_delete=models.CASCADE)




"""
MODELOS PARA LAS VISTAS DE ALUMNOS
############################################################################################################
############################################################################################################
############################################################################################################
"""









