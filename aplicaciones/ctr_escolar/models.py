from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.safestring import mark_safe
Usuario = get_user_model()
TIPO_REACTIVO = (
    ('text', 'Respuesta corta' ),
    ('textarea', 'Parrafo' ),
    ('radio', 'Varias opciones' ),
)
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
    
    class Meta:
        verbose_name ='Recurso de materia'
        verbose_name_plural = "Recursos de materia"

class Materia(models.Model):
    materia_id = models.AutoField(primary_key=True)
    materia_aula=models.ForeignKey(Aula, verbose_name='Aula', on_delete=models.CASCADE)
    materia_nombre = models.CharField('Nombre', max_length=150)
    materia_archivos=models.ManyToManyField(Documento, verbose_name="Archivos")
    materia_registro_alumnnos=models.ManyToManyField(Usuario, verbose_name="Registro_materia")
    materia_creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.materia_nombre
    
    class Meta:
        verbose_name ='Materia'
        verbose_name_plural = "Materias"



class Unidad(models.Model):
    unidad_id=models.AutoField(primary_key=True)
    unidad_nombre=models.CharField('Nombre', max_length=500)
    unidad_materia=models.ForeignKey(Materia, verbose_name='Materia', on_delete=models.CASCADE)
    def __str__(self):
        return self.unidad_nombre

class Tarea(models.Model):
    tarea_id=models.AutoField(primary_key=True) 
    tarea_nombre = models.CharField('Nombre', max_length=600)
    tarea_descripcion = models.CharField('Descripcion', max_length=2000)
    tarea_fecha_inicio = models.DateField('Fecha de inicio')
    tarea_fecha_termino = models.DateField('Fecha de Final')
    TIPO_TAREA=(('ENTREGA', 'ENTREGA'), ('PARA CALIFICAR','PARA CALIFICAR'), ('EXAMEN', 'EXAMEN'))
    tarea_tipo=models.CharField('Tipo de tarea', max_length=20, choices=TIPO_TAREA)
    tarea_porcentaje=models.IntegerField('Valor en %', validators=[MinValueValidator(1),MaxValueValidator(100)], default=1)
    tarea_unidad=models.ForeignKey(Unidad, verbose_name='Unidad', on_delete=models.CASCADE)
    tarea_hora_init = models.TimeField("Hora de inicio", help_text=mark_safe('<small class="form-text text-muted">Aplica si es examen</small>'),null=True, blank=True)
    tarea_hora_end = models.TimeField("Hora de finalización", help_text=mark_safe('<small class="form-text text-muted">Aplica si es examen</small>'),null=True, blank=True)
    def __str__(self):
        return self.tarea_nombre


class Reactivo(models.Model):
    rec_nombre = models.CharField("Redacte su pregunta",max_length=900)
    rec_examen = models.ForeignKey(Tarea, verbose_name ="Tarea", on_delete=models.CASCADE)
    rec_tipo = models.TextField('Tipo de reactivo', choices=TIPO_REACTIVO)

    def __str__(self):
        return self.rec_nombre
    def get_eleccion_ok(self):
        id_rlrccion_reactivo = EleccionReactivo.objects.get(el_reactivo=self.id, el_verdadero=True)
        return id_rlrccion_reactivo


class EleccionReactivo(models.Model):
    el_value = models.TextField(verbose_name="Valor eleccion")
    el_reactivo = models.ForeignKey(Reactivo, verbose_name='Reactivo', on_delete=models.CASCADE)
    el_verdadero = models.BooleanField(verbose_name="respuesta correcta")

    def __str__(self):
        return self.el_value

class RespuestaExamen(models.Model): 
    re_reactivo = models.ForeignKey(Reactivo, verbose_name ="Pregunta", on_delete=models.CASCADE)
    re_alumno = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Alumno")
    re_ok = models.BooleanField(verbose_name="¿Correcto?")
    re_text = models.TextField(verbose_name="Respondió")
    def __str__(self):
        return str(self.re_reactivo)
    class Meta:
        unique_together = (("re_reactivo", "re_alumno"),)
        # ordering = ['-tareaDocumento_actualizado']



class TareaDocumento(models.Model):
    tareaDocumento_id=models.AutoField(primary_key=True)
    tareaDocumento_archivo=models.FileField('Archivo', upload_to='documentos_tareas/')
    tareaDocumento_comentario_alumno=models.CharField('Comentario Alumno', max_length=500)
    tareaDocumento_comentario_maestro=models.CharField('Comentario Maestro', max_length=500, null=True, blank=True)
    tareaDocumento_creado=models.DateTimeField('Creado', auto_now_add=True)
    tareaDocumento_pertenece=models.ForeignKey(Usuario, verbose_name='Pertenece a', on_delete=models.CASCADE) 
    tareaDocumento_Tarea=models.ForeignKey(Tarea, verbose_name='Tarea', on_delete=models.CASCADE)
    tareaDocumento_status=models.BooleanField('Status Tarea', default=False)
    tareaDocumento_calificacion=models.FloatField('Calificación', null=True, blank=True, validators=[MinValueValidator(1),MaxValueValidator(10)],help_text="Calificacion valida de 1 a 10")
    tareaDocumento_actualizado=models.DateTimeField(auto_now=True) 

    def porcentaje_tarea(self):
        porcentaje_tarea=self.tareaDocumento_Tarea.tarea_porcentaje
        valor_cada_unidad=porcentaje_tarea / 10
        calificacion_documento= 0 if self.tareaDocumento_calificacion == None else self.tareaDocumento_calificacion
        porcentaje_tarea_entregada=calificacion_documento*valor_cada_unidad
        return round(porcentaje_tarea_entregada, 2) 

    class Meta:
        unique_together = (("tareaDocumento_pertenece", "tareaDocumento_Tarea"),)
        ordering = ['-tareaDocumento_actualizado']

    def __str__(self):
        user=str(self.tareaDocumento_pertenece.first_name)
        archivo=str(self.tareaDocumento_archivo)
        archivo=archivo.replace('documentos_tareas/', '')
        return str(user+' archivo: '+archivo)

class Blog(models.Model):
    blog_id=models.AutoField(primary_key=True)
    blog_titulo =models.CharField('Titulo', max_length=600)
    blog_descripcion =models.CharField('Descripcion', max_length=2000)
    blog_contenido=models.TextField('Contenido', blank=False, null=True,)
    blog_imagen = models.ImageField('Imagen Blog', upload_to='img_blogs/')
    blog_creado=models.DateTimeField('Creado en', auto_now_add=True)
    blog_ultima_actualizacion=models.DateTimeField('Ultima Actualizacion', auto_now=True)
    blog_pertenece=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    blog_materia=models.ManyToManyField(Materia, verbose_name="Relacionar", help_text='Utilize la tecla CTRL y seleccione multiples opciones')

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








    











