from django.db import models


class Categoria(models.Model):
    cat_id=models.AutoField(primary_key=True)
    cat_nombre =models.CharField('Nombre', max_length=350)
    def __str__(self):
        return self.cat_nombre
class Tag(models.Model):
    tag_id=models.AutoField(primary_key=True)
    tag_nombre =models.CharField('Nombre', max_length=350)
    def __str__(self):
        return self.tag_nombre

# Create your models here.
class Blog(models.Model):
    blog_id=models.AutoField(primary_key=True)
    blog_titulo =models.CharField('Titulo', max_length=250)
    blog_descripcion =models.CharField('Descripcion', max_length=500)
    blog_contenido=models.TextField('Contenido', blank=False, null=True,)
    blog_imagen = models.ImageField('Imagen Blog', upload_to='img_blogs/')
    blog_creado=models.DateTimeField('Creado en', auto_now_add=True)
    blog_ultima_actualizacion=models.DateTimeField('Ultima Actualizacion', auto_now=True)
    blog_categoria = models.ForeignKey(Categoria, verbose_name='Categorias', on_delete=models.CASCADE)
    blog_tags = models.ManyToManyField(Tag, verbose_name="Tags", help_text='Utilize la tecla CTRL y seleccione multiples opciones')

    def __str__(self):
        return self.blog_titulo